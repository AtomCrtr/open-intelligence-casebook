"""Contrôle de traçabilité d'un dossier de cas (bibliothèque standard uniquement).

Usage :
    python tools/check_case.py osint/XZ-UTILS-2024 [autre_dossier ...]

Vérifie, pour chaque dossier :
- evidence_register.csv (si présent, format de templates/evidence_register.csv) : colonnes,
  identifiants E-NNN uniques, énumérations, fiabilité / confiance justifiées, et
  référence aux preuves sources pour tout élément Derived ;
- citations-ledger.json : schéma (id, url https, title, accessed ISO, quotes non vides),
  identifiants uniques ;
- chaque citation du ledger figure mot pour mot dans source-extracts.md (si présent) ;
- chaque référence [n] des fichiers Markdown existe dans le ledger, et chaque source
  du ledger est citée au moins une fois ;
- aucun identifiant de ligne de tableau (F-, E-, S-, H-, KJ-, C-) n'est dupliqué
  dans un même fichier ;
- les niveaux de confiance utilisés appartiennent au vocabulaire du workspace
  (methodology/CONFIDENCE_LEVELS.md).

Code de sortie : 0 si aucun problème, 1 sinon. Aucun accès réseau.
"""

from __future__ import annotations

import csv
import json
import re
import sys
from datetime import date
from pathlib import Path

CONFIDENCE = {"HIGH", "MEDIUM-HIGH", "MEDIUM", "LOW-MEDIUM", "LOW"}
ROW_ID = re.compile(r"^\|\s*((?:F|E|S|H|KJ|C)-\d+)\s*\|", re.MULTILINE)
REF = re.compile(r"(?<![\w\]])\[(\d+)\](?!\()")
CONF_TOKEN = re.compile(r"\b(?:HIGH|MEDIUM|LOW)(?:-(?:HIGH|MEDIUM|LOW))?\b")
PLACEHOLDER = re.compile(r"HIGH\s*/\s*MEDIUM\s*/\s*LOW|HIGH/MEDIUM/LOW")


def normalize(text: str) -> str:
    text = text.replace("’", "'").replace("“", '"').replace("”", '"')
    return re.sub(r"\s+", " ", text).strip()


REGISTER_COLUMNS = [
    "evidence_id",
    "type",
    "description",
    "source",
    "source_type",
    "primary_secondary",
    "observation_mode",
    "collection_timestamp",
    "timezone",
    "normalized_utc",
    "hash",
    "corroboration",
    "reliability",
    "confidence",
    "notes",
    "provenance",
]
PRIMARY = {"Primary", "Secondary", "Mixed", "Unknown"}
MODES = {"Direct observation", "Reported", "Derived"}
GRADED = re.compile(r"^(HIGH|MEDIUM-HIGH|MEDIUM|LOW-MEDIUM|LOW|UNKNOWN)\s+[—-]\s+\S")


def check_register(folder: Path, problems: list[str]) -> None:
    path = folder / "evidence_register.csv"
    if not path.exists():
        return
    with path.open(encoding="utf-8", newline="") as handle:
        reader = csv.DictReader(handle)
        missing = [c for c in REGISTER_COLUMNS if c not in (reader.fieldnames or [])]
        if missing:
            problems.append(f"{path.name}: colonnes manquantes {missing}")
            return
        rows = list(reader)
    ids = [r["evidence_id"] for r in rows]
    for row in rows:
        eid = row["evidence_id"]
        if not re.fullmatch(r"E-\d{3,}", eid):
            problems.append(f"{path.name}: identifiant invalide {eid!r}")
        if row["primary_secondary"] not in PRIMARY:
            problems.append(f"{path.name} {eid}: primary_secondary hors {sorted(PRIMARY)}")
        if row["observation_mode"] not in MODES:
            problems.append(f"{path.name} {eid}: observation_mode hors {sorted(MODES)}")
        for col in ("reliability", "confidence"):
            if not GRADED.match(row[col]):
                problems.append(f"{path.name} {eid}: {col} doit être 'NIVEAU — justification'")
        if not row["collection_timestamp"].strip():
            problems.append(f"{path.name} {eid}: collection_timestamp vide")
        if row["observation_mode"] == "Derived":
            parents = set(re.findall(r"E-\d{3,}", row["corroboration"] + " " + row["notes"])) - {eid}
            if not parents:
                problems.append(f"{path.name} {eid}: élément Derived sans preuve source référencée")
            elif parents - set(ids):
                problems.append(f"{path.name} {eid}: preuves sources inconnues {sorted(parents - set(ids))}")
    dupes = sorted({i for i in ids if ids.count(i) > 1})
    if dupes:
        problems.append(f"{path.name}: identifiants dupliqués {dupes}")


def check_ledger(folder: Path, problems: list[str]) -> set[int]:
    path = folder / "citations-ledger.json"
    if not path.exists():
        return set()
    try:
        ledger = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        problems.append(f"{path.name}: JSON invalide ({exc})")
        return set()
    sources = ledger.get("sources")
    if not isinstance(sources, list) or not sources:
        problems.append(f"{path.name}: liste 'sources' absente ou vide")
        return set()
    extracts_path = folder / "source-extracts.md"
    extracts = normalize(extracts_path.read_text(encoding="utf-8")) if extracts_path.exists() else None
    ids: list[int] = []
    for src in sources:
        sid = src.get("id")
        label = f"{path.name} source {sid}"
        if not isinstance(sid, int):
            problems.append(f"{label}: id entier manquant")
            continue
        ids.append(sid)
        if not str(src.get("url", "")).startswith("https://"):
            problems.append(f"{label}: url https manquante")
        if not str(src.get("title", "")).strip():
            problems.append(f"{label}: titre vide")
        try:
            date.fromisoformat(str(src.get("accessed", "")))
        except ValueError:
            problems.append(f"{label}: date 'accessed' non ISO (AAAA-MM-JJ)")
        quotes = src.get("quotes") or []
        if not quotes:
            problems.append(f"{label}: aucune citation")
        for quote in quotes:
            text = str(quote.get("text", ""))
            if extracts is not None and normalize(text) not in extracts:
                problems.append(f"{label}: citation absente de source-extracts.md : « {text[:60]}… »")
    dupes = sorted({i for i in ids if ids.count(i) > 1})
    if dupes:
        problems.append(f"{path.name}: identifiants dupliqués {dupes}")
    return set(ids)


def check_markdown(folder: Path, ledger_ids: set[int], problems: list[str]) -> None:
    cited: set[int] = set()
    for md in sorted(folder.glob("*.md")):
        if md.name == "source-extracts.md":
            continue
        text = md.read_text(encoding="utf-8")
        rows = ROW_ID.findall(text)
        dupes = sorted({r for r in rows if rows.count(r) > 1})
        if dupes:
            problems.append(f"{md.name}: identifiants de ligne dupliqués {dupes}")
        refs = {int(n) for n in REF.findall(text)}
        cited |= refs
        if ledger_ids:
            unknown = sorted(refs - ledger_ids)
            if unknown:
                problems.append(f"{md.name}: références absentes du ledger {unknown}")
        body = PLACEHOLDER.sub("", text)
        bad = sorted({t for t in CONF_TOKEN.findall(body) if t not in CONFIDENCE})
        if bad:
            problems.append(f"{md.name}: niveaux de confiance hors vocabulaire {bad}")
    if ledger_ids:
        orphan = sorted(ledger_ids - cited)
        if orphan:
            problems.append(f"citations-ledger.json: sources jamais citées {orphan}")


def check_case(folder: Path) -> list[str]:
    problems: list[str] = []
    if not folder.is_dir():
        return [f"{folder}: dossier introuvable"]
    ids = check_ledger(folder, problems)
    check_register(folder, problems)
    check_markdown(folder, ids, problems)
    return problems


def main(argv: list[str]) -> int:
    if not argv:
        print(__doc__)
        return 2
    status = 0
    for arg in argv:
        folder = Path(arg)
        problems = check_case(folder)
        if problems:
            status = 1
            print(f"FAIL {folder}")
            for problem in problems:
                print(f"  - {problem}")
        else:
            print(f"PASS {folder}")
    return status


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
