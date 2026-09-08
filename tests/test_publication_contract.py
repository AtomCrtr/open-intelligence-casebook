import csv
import hashlib
import re
from pathlib import Path

import tools.build_publication as publication_builder

ROOT = Path(__file__).resolve().parents[1]
CASE01 = ROOT / "cases" / "case-01-titanium"
CASE02 = ROOT / "cases" / "case-02-portal-kombat"


def rows(path: Path):
    with path.open(encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


def test_case2_public_text_preserves_units_and_uncertainty():
    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    report = (CASE02 / "report.md").read_text(encoding="utf-8")
    sources = (CASE02 / "sources.md").read_text(encoding="utf-8")
    text = readme + report

    assert "371 observations correspondant à 370 domaines distincts" in text
    assert "44 éditions linguistiques" in text
    assert "31 domaines" not in report
    assert "ne peut pas être rejetée" in report
    assert "publient indépendamment" not in report
    assert "S-031" in sources
    assert "api.github.com/repos/VIGINUM-FR" not in sources


def test_public_provenance_exposes_information_lineages():
    case1 = rows(CASE01 / "provenance.csv")
    case2 = rows(CASE02 / "provenance.csv")
    assert len({row["claim_id"] for row in case1}) >= 8
    assert len({row["claim_id"] for row in case2}) >= 8
    assert all(row["information_lineage"] for row in case1 + case2)

    case1_options = {
        row["source_id"]
        for row in case1
        if row["claim_id"] == "C1-PUB-005"
    }
    assert case1_options == {"S-015", "S-016", "S-020"}
    case1_sources = (CASE01 / "sources.md").read_text(encoding="utf-8")
    assert "S-003 — USGS" in case1_sources
    assert "S-004 — règlement" in case1_sources
    assert "S-015 — SEC, IperionX" in case1_sources
    assert "S-016 — Banque européenne d'investissement" in case1_sources
    assert "S-020 — Osaka Titanium" in case1_sources

    shared = {
        row["source_id"]: row["information_lineage"]
        for row in case2
        if row["source_id"] in {"S-016", "S-030"}
    }
    assert shared == {
        "S-016": "DFRLAB-CHECKFIRST-SHARED-STUDY",
        "S-030": "DFRLAB-CHECKFIRST-SHARED-STUDY",
    }
    assert not [row for row in case2 if row["source_id"] == "S-029" and row["claim_id"] != "C2-PUB-008"]


def test_public_manifest_excludes_local_cache_artifacts():
    manifest = (ROOT / "publication" / "public-manifest.csv").read_text(
        encoding="utf-8"
    )
    ignored = (ROOT / ".gitignore").read_text(encoding="utf-8")
    for cache_name in (".ruff_cache", ".pytest_cache", "__pycache__"):
        assert cache_name not in manifest
        assert cache_name in ignored


def test_manifest_excludes_direct_python_bytecode_cache():
    cache_path = ROOT / ".manifest-test-cache.pyc"
    cache_preexisted = cache_path.exists()
    original_cache = cache_path.read_bytes() if cache_preexisted else None
    control_files = [
        ROOT / "publication" / "checksums.sha256",
        ROOT / "publication" / "public-manifest.csv",
        ROOT / "publication" / "release-checklist.md",
    ]
    originals = {path: path.read_bytes() for path in control_files}

    cache_path.write_bytes(b"bytecode cache fixture")
    try:
        publication_builder.write_publication_files()
        manifest = (ROOT / "publication" / "public-manifest.csv").read_text(
            encoding="utf-8"
        )
        assert cache_path.name not in manifest
    finally:
        if cache_preexisted:
            cache_path.write_bytes(original_cache or b"")
        else:
            cache_path.unlink(missing_ok=True)
        for path, content in originals.items():
            path.write_bytes(content)


def test_checked_in_checksums_match_declared_public_artifacts():
    checksum_file = ROOT / "publication" / "checksums.sha256"
    for line in checksum_file.read_text(encoding="utf-8").splitlines():
        expected, relative_path = line.split("  ", 1)
        actual = hashlib.sha256((ROOT / relative_path).read_bytes()).hexdigest()
        assert actual == expected, relative_path


def test_writable_ci_pins_upload_action_and_scopes_token():
    workflow = (ROOT / ".github" / "workflows" / "build-publication.yml").read_text(
        encoding="utf-8"
    )
    build_guide = (ROOT / "BUILD.md").read_text(encoding="utf-8")

    assert "actions/upload-artifact@ea165f8d65b6e75b540449e92b4886f43607fa02" in workflow
    assert "actions/upload-artifact@v4" not in workflow
    assert workflow.count("GH_TOKEN:") == 2
    assert "weasyprint==68.0" in workflow
    assert "weasyprint==68.0" in build_guide
    assert "git add -A" not in workflow
    assert "PYTHONDONTWRITEBYTECODE: \"1\"" in workflow
    commit_section = workflow.split("- name: Commit publication package", 1)[1]
    assert commit_section.index("python tools/build_publication.py") < commit_section.index(
        "git add --"
    )
    assert "publication/release-checklist.md" in commit_section


def test_changed_timeline_svg_has_no_trailing_whitespace():
    svg = CASE02 / "figures" / "timeline.svg"
    text = svg.read_text(encoding="utf-8")
    lines = text.splitlines()
    assert lines == [line.rstrip() for line in lines]
    assert text.endswith("\n") and not text.endswith("\n\n")


def test_pdf_artifacts_are_declared_binary_for_git_checks():
    attributes = (ROOT / ".gitattributes").read_text(encoding="utf-8")
    assert "*.pdf binary" in attributes.splitlines()


def test_readme_does_not_publish_environment_dependent_pdf_page_counts():
    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    assert not re.search(r"rapport PDF — \d+ pages", readme)
    assert "cases/case-01-titanium/report.pdf" in readme
    assert "cases/case-02-portal-kombat/report.pdf" in readme
