#!/usr/bin/env python3
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
C1 = ROOT / "cases/case-01-titanium"
C2 = ROOT / "cases/case-02-portal-kombat"


def insert_after(path: Path, anchor: str, block: str, marker: str) -> None:
    text = path.read_text(encoding="utf-8")
    if marker in text:
        return
    if anchor not in text:
        raise RuntimeError(f"Anchor introuvable dans {path}: {anchor[:80]}")
    text = text.replace(anchor, anchor + "\n\n" + block, 1)
    path.write_text(text, encoding="utf-8", newline="\n")


def replace_between(path: Path, start: str, end: str, replacement: str) -> None:
    text = path.read_text(encoding="utf-8")
    i = text.find(start)
    j = text.find(end)
    if i < 0 or j < 0 or j <= i:
        raise RuntimeError(f"Section introuvable dans {path}")
    text = text[:i] + replacement.rstrip() + "\n\n" + text[j:]
    path.write_text(text, encoding="utf-8", newline="\n")


def ensure_link(path: Path, anchor: str, line: str) -> None:
    text = path.read_text(encoding="utf-8")
    if line in text:
        return
    if anchor not in text:
        raise RuntimeError(f"Lien-ancre introuvable dans {path}")
    text = text.replace(anchor, anchor + "\n" + line, 1)
    path.write_text(text, encoding="utf-8", newline="\n")


def write_evidence_maps() -> None:
    c1 = """# Carte publique affirmation-preuve - Case 01\n\nCette carte rend visible la chaîne **affirmation -> preuve -> confiance -> limite** sans republier les registres internes ni les corpus tiers du dépôt canonique. Elle complète le [rapport public](report.md) et la [liste des sources](sources.md).\n\n| Affirmation publique | Type de preuve | Sources / artefacts publics | Confiance | Limite déterminante |\n|---|---|---|---|---|\n| La concentration commerciale évolue différemment selon les six formes de titane. | mesure dérivée reproductible | [Eurostat / Comext](sources.md), [métriques CN8](data/key_metrics.csv), [figure HHI](figures/hhi_2017_2025.svg) | élevée pour la mesure commerciale | flux toutes industries, pas exposition aéronautique directe |\n| Les tubes se concentrent fortement entre 2017 et 2025 : HHI 2 130,6 -> 4 137,9 ; Chine 60,23 % du premier partenaire en 2025. | mesure dérivée reproductible | [métriques CN8](data/key_metrics.csv), Eurostat | élevée | origine douanière != producteur réel != fournisseur qualifié |\n| Les déchets et chutes montrent au contraire une baisse de concentration : HHI 2 568,5 -> 1 449,4. | mesure dérivée reproductible | [métriques CN8](data/key_metrics.csv), Eurostat | élevée | ne prouve pas une boucle fermée aéronautique ni une substitution |\n| Un changement de premier partenaire ne signifie pas automatiquement une diversification structurelle. | inférence bornée par la mesure | formes brutes/poudres : États-Unis -> Kazakhstan avec HHI quasi stable ; [figure partenaires](figures/dominant_partner.svg) | modérée | les catégories CN8 agrègent plusieurs produits et usages |\n| Une capacité industrielle nouvelle ne devient pas automatiquement une source aéronautique substituable. | triangulation industrielle + règle analytique | BEI/ECOTITANIUM, Osaka Titanium, SEC/IperionX ; [portes de qualification](figures/qualification_gates.svg) | modérée | qualification, approbation client, contrat et livraison restent moins observables |\n| H1, H3 et H4 sont partiellement soutenues ; H2 reste non concluante. | ACH / hypothèses concurrentes | [rapport §7](report.md), [figure hypothèses](figures/hypotheses.svg) | faible à modérée selon l'hypothèse | le corpus ne reconstruit pas toute la chaîne mondiale qualifiée maillon par maillon |\n| Trois scénarios 2030 servent à tester la robustesse des options, sans probabilité implicite. | scénarios exploratoires | [rapport §9](report.md), [figure scénarios](figures/scenarios_2030.svg) | modérée sur la logique, aucune probabilité attribuée | scénarios sensibles aux capacités, qualifications, demande et données internes futures |\n| Les recommandations doivent rester conditionnelles et ne peuvent pas dimensionner seules une décision réelle de stock, sourcing ou investissement. | synthèse décisionnelle | [rapport §12-13](report.md), cadre de veille et données internes requises | modérée | consommation, criticité, délais, contrats, approbations et coûts réels ne sont pas publics |\n\n## Règle de lecture\n\nUne affirmation n'est renforcée que par une preuve portant sur le **même objet et le même périmètre**. Une capacité physique ne transfère pas sa preuve à la qualification ; une qualification ne transfère pas sa preuve à l'approbation client ; une baisse de HHI ne transfère pas sa preuve à la résilience aéronautique.\n"""
    (C1 / "evidence-map.md").write_text(c1, encoding="utf-8", newline="\n")

    c2 = """# Carte publique affirmation-preuve - Case 02\n\nCette carte expose la chaîne **affirmation -> preuve -> confiance -> limite** à partir de métriques dérivées et de sources link-only. Elle ne republie ni corpus de posts, ni identifiants de comptes, ni données personnelles.\n\n| Affirmation publique | Type de preuve | Sources / artefacts publics | Confiance | Limite déterminante |\n|---|---|---|---|---|\n| Le snapshot VIGINUM contient 371 observations de domaines, dont 232 datées et 139 non datées. | observation / décompte dérivé | [VIGINUM](sources.md), [métriques](data/key_metrics.csv) | élevée | `valid_from` n'est pas une preuve indépendante de première mise en ligne |\n| Mars 2024 forme une vague paneuropéenne de 31 observations `pravda-*`. | observation + corroboration | VIGINUM export, VIGINUM partie 3, EDMO ; [chronologie](figures/timeline.svg) | moyenne à élevée | phases tardives 2024/2025 reposent davantage sur des publications ultérieures |\n| Le paquet STIX analysé contient 609 nœuds et 1 013 relations ; la composante principale contient 604 nœuds. | observation source-modélisée | VIGINUM STIX, [métriques](data/key_metrics.csv) | élevée pour le décompte | le graphe représente aussi des choix de modélisation |\n| La grande composante ne dépend pas du seul nœud campagne, mais elle est très sensible aux relations `amplifies`. | analyse de sensibilité | [figure de sensibilité](figures/graph_sensitivity.svg), rapport §6 | moyenne | sensibilité du modèle != chaîne de commandement réelle |\n| La dissémination figée contient 1 932 observations Wikipedia et 2 018 observations X. | décompte dérivé + corroboration | CheckFirst, DFRLab, [métriques](data/key_metrics.csv) | élevée | présence d'un lien != audience, croyance ou effet |\n| La France est ciblée mais ne domine pas la couche Wikipedia observée. | décompte dérivé | `fr=28` sur Wikipedia ; `fr=94` sur X ; 130 observations X vers domaines France-compatibles ; [figure France](figures/france_focus.svg) | élevée pour les comptes | aucune mesure d'audience française |\n| H4 - modèle hybride - reste la meilleure hypothèse de travail. | ACH + triangulation | [figure ACH](figures/ach_hypotheses.svg), VIGINUM, EDMO, DFRLab, CheckFirst | faible à moyenne | ne démontre ni opérateur éditorial unique ni attribution étatique |\n| Le corpus ne démontre ni impact humain, ni effet électoral, ni empoisonnement causal des LLM. | conclusion négative bornée par les données | absence de métriques d'audience/effet ; lectures concurrentes ASP/NewsGuard vs Harvard | élevée sur la lacune, faible sur les mécanismes non observés | absence de preuve != preuve d'absence |\n\n## Règle de lecture\n\nLe casebook interdit le glissement automatique **visibilité -> coordination -> attribution -> impact**. Chaque niveau exige une catégorie de preuve supplémentaire ; les niveaux non couverts restent explicitement non démontrés.\n"""
    (C2 / "evidence-map.md").write_text(c2, encoding="utf-8", newline="\n")


def pre() -> None:
    c1_report = C1 / "report.md"
    c2_report = C2 / "report.md"

    c1_pir = """## 2.1 Couverture des besoins prioritaires en renseignement (PIR)\n\nLe dépôt canonique suivait cinq PIR distincts. Leur couverture publique est affichée ici pour éviter qu'une réponse décisionnelle synthétique soit confondue avec une résolution exhaustive de toutes les sous-questions.\n\n| PIR | Question résumée | Statut à l'issue du casebook | Confiance | Lacune qui reste ouverte |\n|---|---|---|---|---|\n| PIR-01 | concentration mondiale maillon par maillon | **partiellement répondu** | faible | pas de série mondiale comparable 2014-2025 pour tous les maillons ni de cartographie exhaustive des acteurs qualifiés |\n| PIR-02 | exposition européenne directe et indirecte | **partiellement répondu** | modérée | les flux CN8 restent toutes industries ; pièces intégrées, réexportations et portefeuille réel non mesurés |\n| PIR-03 | diversification annoncée vs vérifiable | **partiellement répondu** | modérée | approbations clients, contrats, stocks et livraisons restent peu visibles publiquement |\n| PIR-04 | substituabilité, qualification et délais | **partiellement répondu** | faible | aucun délai générique fiable ni équivalence fournisseur/matière transférable à tous les programmes |\n| PIR-05 | trajectoires 2030 et signaux de vigilance | **répondu avec limites au stade scénarios/veille** | modérée sur le cadre | les 18 EWI définissent des signaux et cadences, pas des probabilités ni des seuils automatiques de décision |\n\n> **Interprétation.** Une PIR partiellement répondue n'est pas un échec : elle matérialise la frontière entre ce qui est défendable en sources ouvertes et ce qui exige des données industrielles, contractuelles ou client non publiques.\n"""
    insert_after(
        c1_report,
        "Le code **81082000** appelle une prudence particulière : il agrège éponge, lingots, billettes, autres formes brutes et poudres. Il ne permet pas d'isoler l'éponge ni un grade aéronautique.",
        c1_pir,
        "## 2.1 Couverture des besoins prioritaires en renseignement (PIR)",
    )

    c1_recs = """# 12. Recommandations conditionnelles\n\nLe dossier canonique transforme les dix options de résilience en **huit recommandations**. Les niveaux ci-dessous indiquent une posture de préparation, pas un ordre d'achat. Un EWI ouvre une **revue de posture** ; il ne déclenche jamais automatiquement un sourcing, un stock ou un investissement.\n\n| Niveau | ID | Recommandation | Déclencheurs / signaux principaux | Condition avant activation réelle |\n|---|---|---|---|---|\n| **Agir maintenant** | REC-01 | mettre en place une surveillance gouvernée | démarrage immédiat dans le périmètre informationnel | responsables, sources, cadence, règle de preuve et revue humaine |\n| **Préparer maintenant** | REC-02 | préparer diversification et qualification de nouvelles sources | EWI-03, EWI-04, EWI-06, EWI-09, EWI-17 | objet nommé, données internes, qualification, approbation, accès contractuel et livraison |\n| **Développer / valider** | REC-03 | préparer la visibilité multi-rangs et les droits d'information | préparation continue ; nouveaux jeux de données exploitables (EWI-16) | droits d'accès, fraîcheur, références, sites, origines et statuts de qualification |\n| **Développer / valider** | REC-04 | construire une redondance qualifiée et contractuellement accessible | EWI-04, EWI-06, EWI-07, EWI-09, EWI-12 | deux flux réellement indépendants sur un périmètre qualifié identique |\n| **Développer / valider** | REC-05 | construire la méthode de dimensionnement des stocks ciblés | EWI-09, EWI-13, EWI-17 | consommation, stock existant, délais, criticité, traçabilité et coût d'immobilisation |\n| **Développer / valider** | REC-06 | évaluer une boucle fermée sur un flux de chutes attribuable | EWI-10 | grade, volume collectable, rendement, traitement, qualification, approbation et retour matière |\n| **Développer / valider** | REC-07 | développer un dossier d'alternative matière ou procédé | EWI-03, EWI-18 | faisabilité, essais, responsabilités, qualification, approbation et capacité industrielle |\n| **Maintenir sous surveillance** | REC-08 | conserver la coopération clients/fournisseurs comme option liée à un dossier nommé | EWI-03, EWI-04, EWI-17 | dossier commun, responsabilités identifiées et signal attribuable |\n\n### 12.1 Ce que signifient les EWI\n\nLe cadre de veille canonique contient **18 Early Warning Indicators** couvrant capacité industrielle, qualification, contractualisation, commerce, recyclage, réglementation, géopolitique, logistique, demande et technologie. Leur force dépend de la nature de la preuve : une annonce de capacité reste faible ; une production commerciale attribuable est forte ; une approbation client ou une première livraison aéronautique peut devenir décisive.\n\nExemples :\n\n- **EWI-04** : qualification matière, procédé et site achevée et vérifiée ;\n- **EWI-06** : première livraison aéronautique vérifiée depuis une source alternative ;\n- **EWI-09** : concentration persistante ou croissante sur un code suivi ;\n- **EWI-10** : production recyclée avec chaîne d'usage aéronautique vérifiée ;\n- **EWI-12** : restriction d'exportation ou d'accès officiellement entrée en vigueur ;\n- **EWI-17** : plusieurs indicateurs montrent une demande progressant plus vite que l'offre réellement qualifiée ;\n- **EWI-18** : procédé émergent qualifié, approuvé et livré pour un usage aéronautique nommé.\n\n### 12.2 Quatre règles de décision\n\n1. **Surveiller n'est pas réduire physiquement le risque.** La veille réduit surtout l'incertitude et le délai de détection.\n2. **Préparer n'est pas activer.** Un dossier de diversification peut être préparé avant crise, mais l'engagement attend toutes les portes applicables.\n3. **Un trigger ouvre une revue, pas une action automatique.** La preuve, le périmètre et les données internes restent obligatoires.\n4. **L'OSINT ne dimensionne pas seul un stock.** Sans consommation, criticité, délais, stock existant et coût d'immobilisation, un nombre de mois serait artificiel.\n"""
    replace_between(c1_report, "# 12. Recommandations conditionnelles", "# 13. Données internes nécessaires avant une décision réelle", c1_recs)

    c2_pir = """## 2.1 Couverture des besoins prioritaires en renseignement (PIR)\n\nLes six PIR du dossier canonique sont conservées comme grille de contrôle. La question centrale est bien caractérisée, mais deux couches restent volontairement partielles : la production éditoriale au niveau article et l'identification indépendante d'un opérateur.\n\n| PIR | Question résumée | Statut | Confiance | Lacune résiduelle |\n|---|---|---|---|---|\n| PIR-01 | vagues d'expansion géographique et linguistique | **répondu avec limites** | moyenne | 139 domaines sans date ; `valid_from` n'est pas une date de première publication indépendante |\n| PIR-02 | liens techniques et éditoriaux entre portails | **répondu avec limites** | moyenne | pas de comparaison indépendante DNS/certificats/hébergement dans le snapshot |\n| PIR-03 | sélection, reformulation et localisation des contenus | **partiel** | faible | pas de corpus article sous licence pour tester duplication, traduction et transformation |\n| PIR-04 | acteurs ou sources alimentant le réseau | **partiel** | faible | le contrôle opérateur n'est pas établi indépendamment ; identifiants personnels exclus |\n| PIR-05 | chemins de dissémination hors des portails | **répondu avec limites** | élevée | un lien observé ne mesure ni audience, ni croyance, ni appartenance à un corpus d'entraînement |\n| PIR-06 | niveau de coordination démontrable | **hypothèse de travail** | faible ; H4 faible à moyenne | pas de preuve article-level, ownership ou command-and-control ; attribution étatique non établie |\n\n> **À retenir.** Le produit répond donc à la question décisionnelle sans masquer ses lacunes : la dissémination est la couche la mieux étayée ; la production éditoriale, les acteurs et la coordination restent les couches les plus incertaines.\n"""
    insert_after(
        c2_report,
        "Le périmètre privilégie France et Union européenne, avec contexte international lorsque nécessaire. Aucune intrusion n'est réalisée. Les personnes privées, e-mails et identifiants inutiles sont exclus des sorties publiques.",
        c2_pir,
        "## 2.1 Couverture des besoins prioritaires en renseignement (PIR)",
    )

    write_evidence_maps()

    ensure_link(C1 / "README.md", "- [Sources](sources.md)", "- [Carte publique affirmation-preuve](evidence-map.md)")
    ensure_link(C2 / "README.md", "- [Sources](sources.md)", "- [Carte publique affirmation-preuve](evidence-map.md)")

    rr = ROOT / "publication/rights-review.md"
    text = rr.read_text(encoding="utf-8").replace("figures PNG", "figures SVG")
    rr.write_text(text, encoding="utf-8", newline="\n")

    root_readme = ROOT / "README.md"
    text = root_readme.read_text(encoding="utf-8")
    text = text.replace(
        "[**Méthodologie**](cases/case-01-titanium/methodology.md) · [**Sources**](cases/case-01-titanium/sources.md)",
        "[**Méthodologie**](cases/case-01-titanium/methodology.md) · [**Sources**](cases/case-01-titanium/sources.md) · [**Carte des preuves**](cases/case-01-titanium/evidence-map.md)",
    )
    text = text.replace(
        "[**Méthodologie**](cases/case-02-portal-kombat/methodology.md) · [**Sources**](cases/case-02-portal-kombat/sources.md)",
        "[**Méthodologie**](cases/case-02-portal-kombat/methodology.md) · [**Sources**](cases/case-02-portal-kombat/sources.md) · [**Carte des preuves**](cases/case-02-portal-kombat/evidence-map.md)",
    )
    root_readme.write_text(text, encoding="utf-8", newline="\n")


def post() -> None:
    import fitz

    p1 = len(fitz.open(C1 / "report.pdf"))
    p2 = len(fitz.open(C2 / "report.pdf"))
    total = p1 + p2

    readme = ROOT / "README.md"
    text = readme.read_text(encoding="utf-8")
    text = re.sub(r"\*\*\d+ pages A4\*\* au total", f"**{total} pages A4** au total", text)
    text = re.sub(r"Télécharger le rapport PDF — \d+ pages\*\*\]\(cases/case-01-titanium/report.pdf\)", f"Télécharger le rapport PDF — {p1} pages**](cases/case-01-titanium/report.pdf)", text)
    text = re.sub(r"Télécharger le rapport PDF — \d+ pages\*\*\]\(cases/case-02-portal-kombat/report.pdf\)", f"Télécharger le rapport PDF — {p2} pages**](cases/case-02-portal-kombat/report.pdf)", text)
    readme.write_text(text, encoding="utf-8", newline="\n")

    for path, marker in [(C1 / "report.md", "PIR-01"), (C2 / "report.md", "PIR-06")]:
        t = path.read_text(encoding="utf-8")
        if "Couverture des besoins prioritaires" not in t or marker not in t:
            raise RuntimeError(f"Couverture PIR absente: {path}")
    if "REC-08" not in (C1 / "report.md").read_text(encoding="utf-8"):
        raise RuntimeError("Synthèse des 8 recommandations absente")
    for p in [C1 / "evidence-map.md", C2 / "evidence-map.md"]:
        if not p.exists() or "Affirmation publique" not in p.read_text(encoding="utf-8"):
            raise RuntimeError(f"Carte de preuves invalide: {p}")
    if "figures PNG" in (ROOT / "publication/rights-review.md").read_text(encoding="utf-8"):
        raise RuntimeError("Incohérence PNG encore présente")

    print(f"AUDIT_IMPROVEMENTS=PASS CASE01_PAGES={p1} CASE02_PAGES={p2} TOTAL={total}")
    Path(__file__).unlink()


def main() -> None:
    mode = sys.argv[1] if len(sys.argv) > 1 else "pre"
    if mode == "pre":
        pre()
    elif mode == "post":
        post()
    else:
        raise SystemExit("usage: apply_audit_improvements.py [pre|post]")


if __name__ == "__main__":
    main()
