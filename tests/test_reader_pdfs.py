"""Reader-facing PDF contracts: usable evidence links and complete integrity coverage."""
import csv
import shutil
import subprocess

import pytest

import fitz

from tools import build_publication as builder


def test_pdf_keeps_evidence_links_on_public_github_and_local_headings_internal(tmp_path, monkeypatch):
    case = tmp_path / 'cases/case-04-xz-utils'
    case.mkdir(parents=True)
    (tmp_path / 'tools').mkdir()
    shutil.copy2(builder.ROOT / 'tools/report.html', tmp_path / 'tools/report.html')
    (case / 'figures').mkdir()
    pixmap = fitz.Pixmap(fitz.csRGB, (0, 0, 20, 20))
    for x in range(20):
        for y in range(20):
            pixmap.set_pixel(x, y, (x * 12, y * 12, (x + y) * 6))
    pixmap.save(case / 'figures/sample.png')
    (case / 'report.md').write_text(
        '---\ntitle: "Essai de lecture"\nlang: fr-FR\n---\n\n'
        '# Comprendre\n\n'
        '[Extraits](source-extracts.md) · [Citations](citations-ledger.json) · '
        '[Registre](evidence-register.md) · [Transparence](../../AI_TRANSPARENCY.md) · '
        '[Section](#limites)\n\n'
        '# Limites\n\nUn lien de preuve doit rester utilisable hors de la machine de construction.\n\n'
        'La confiance finale repose sur des faits vérifiés.\n\n'
        '**Titane : faits vérifiés et limites.**\n\n'
        '![Figure locale](figures/sample.png)\n',
        encoding='utf-8',
    )
    monkeypatch.setattr(builder, 'ROOT', tmp_path)
    builder.build_pdf(case, 'Essai de lecture', 'test')
    with fitz.open(case / 'report.pdf') as doc:
        links = [link for page in doc for link in page.get_links()]
        urls = {link['uri'] for link in links if link.get('uri')}
        assert 'https://github.com/AtomCrtr/open-intelligence-casebook/blob/main/cases/case-04-xz-utils/source-extracts.md' in urls
        assert 'https://github.com/AtomCrtr/open-intelligence-casebook/blob/main/cases/case-04-xz-utils/citations-ledger.json' in urls
        assert 'https://github.com/AtomCrtr/open-intelligence-casebook/blob/main/cases/case-04-xz-utils/evidence-register.md' in urls
        assert 'https://github.com/AtomCrtr/open-intelligence-casebook/blob/main/AI_TRANSPARENCY.md' in urls
        assert not any(link['kind'] == fitz.LINK_LAUNCH for link in links)
        internal = [link for link in links if link['kind'] in {fitz.LINK_GOTO, fitz.LINK_NAMED}]
        assert internal
        assert all(0 <= link.get('page', -1) < len(doc) for link in internal)
        assert doc.resolve_link('#limites')[0] >= 0
        assert doc.get_toc(), 'Le lecteur doit pouvoir naviguer par les signets PDF.'
        assert any(page.get_image_info() for page in doc), 'Les figures doivent rester intégrées au PDF.'
        text = ' '.join(' '.join(page.get_text().split()) for page in doc)
        assert 'La confiance finale repose sur des faits vérifiés.' in text
        assert 'Essai de lecture' in text
        assert 'Titane : faits vérifiés et limites.' in text
        assert not [c for c in text if ord(c) < 32 and c not in '\n\r\t']


def test_checksum_manifest_includes_case4_and_reading_guide(tmp_path, monkeypatch):
    monkeypatch.setattr(builder, 'ROOT', tmp_path)
    publication = tmp_path / 'publication'
    publication.mkdir()
    monkeypatch.setattr(builder, 'PUB', publication)
    for number, slug in enumerate(
        ['case-01-titanium', 'case-02-portal-kombat', 'case-03-gnss-interference', 'case-04-xz-utils'], 1
    ):
        case = tmp_path / 'cases' / slug
        case.mkdir(parents=True)
        (case / 'data').mkdir()
        (case / 'figures').mkdir()
        (case / 'data/key_metrics.csv').write_text('metric,value\nx,1\n', encoding='utf-8')
        (case / 'provenance.csv').write_text('claim_id\nC-1\n', encoding='utf-8')
        (case / 'report.pdf').write_bytes(b'pdf fixture')
        monkeypatch.setattr(builder, f'C{number}', case)
    (tmp_path / 'READING_GUIDE.pdf').write_bytes(b'guide fixture')
    (tmp_path / 'BEGINNER_READING_TEST.pdf').write_bytes(b'test fixture')
    builder.write_publication_files()
    paths = {
        line.split('  ', 1)[1]
        for line in (publication / 'checksums.sha256').read_text(encoding='utf-8').splitlines()
    }
    assert 'cases/case-04-xz-utils/report.pdf' in paths
    assert 'READING_GUIDE.pdf' in paths
    with (publication / 'public-manifest.csv').open(encoding='utf-8') as handle:
        manifest = {row['path']: row for row in csv.DictReader(handle)}
    assert manifest['READING_GUIDE.pdf']['class'] == 'generated_report'


@pytest.mark.parametrize('slug, heading', [
    ('case-01-titanium', 'Titane et résilience de la filière aéronautique civile européenne'),
    ('case-02-portal-kombat', "Portal Kombat / Pravda : comprendre un écosystème informationnel par l'OSINT"),
])
def test_full_report_keeps_heading_text_after_pdf_generation(tmp_path, monkeypatch, slug, heading):
    """The actual report/font combination exposed the compression regression."""
    original_root = builder.ROOT
    case = tmp_path / 'cases' / slug
    shutil.copytree(original_root / 'cases' / slug, case)
    (tmp_path / 'tools').mkdir()
    shutil.copy2(original_root / 'tools/report.html', tmp_path / 'tools/report.html')
    monkeypatch.setattr(builder, 'ROOT', tmp_path)
    builder.build_pdf(case, heading, 'test')
    with fitz.open(case / 'report.pdf') as doc:
        text = ' '.join(' '.join(p.get_text().split()) for p in doc)
        assert heading in text
        assert 'L’essentiel en deux minutes' in doc[1].get_text()
        assert 'Sommaire' in doc[2].get_text()
        assert doc.xref_get_key(doc.pdf_catalog(), 'StructTreeRoot')[0] == 'xref'
    if shutil.which('pdftotext'):
        external = subprocess.check_output(['pdftotext', str(case / 'report.pdf'), '-'], text=True)
        assert heading in ' '.join(external.split())
        assert not [c for c in text if ord(c) < 32 and c not in '\n\r\t']


def test_summary_requires_balanced_markers_and_preserves_anchors():
    html = '<header>Cover</header><nav>TOC</nav><!-- READER_SUMMARY_START --><h1 id="lead">Lead</h1><!-- READER_SUMMARY_END --><p>Details</p>'
    result = builder.position_reader_summary(html)
    assert result.index('id="lead"') < result.index('<nav>') < result.index('<p>Details')
    with pytest.raises(ValueError):
        builder.position_reader_summary(html.replace('<!-- READER_SUMMARY_END -->', ''))


def test_delivered_pdfs_have_intact_text_and_summary_before_contents():
    paths = [builder.C1/'report.pdf', builder.C2/'report.pdf', builder.C3/'report.pdf',
             builder.C4/'report.pdf', builder.ROOT/'READING_GUIDE.pdf', builder.ROOT/'BEGINNER_READING_TEST.pdf']
    for path in paths:
        builder.validate_text_layer(path)
        with fitz.open(path) as doc:
            assert doc.get_toc(), path
            if path.name != 'BEGINNER_READING_TEST.pdf':
                assert 'deux minutes' in doc[1].get_text(), path
                assert 'Sommaire' in doc[2].get_text(), path


def test_pdf_table_tags_are_stable_across_builds(tmp_path, monkeypatch):
    case = tmp_path / 'case'
    case.mkdir()
    (tmp_path / 'tools').mkdir()
    shutil.copy2(builder.ROOT / 'tools/report.html', tmp_path / 'tools/report.html')
    (case / 'report.md').write_text(
        '# Lecture\n\n| Fait | Limite |\n|---|---|\n| Observation | Attribution non démontrée |\n',
        encoding='utf-8',
    )
    monkeypatch.setattr(builder, 'ROOT', tmp_path)
    builder.build_pdf(case, 'Tableau accessible', 'test')
    first = (case / 'report.pdf').read_bytes()
    builder.build_pdf(case, 'Tableau accessible', 'test')
    assert (case / 'report.pdf').read_bytes() == first
    with fitz.open(case / 'report.pdf') as doc:
        identifiers = {doc.xref_get_key(x, 'ID')[1] for x in range(1, doc.xref_length())
                       if doc.xref_get_key(x, 'Type')[1] == '/StructElem'
                       and doc.xref_get_key(x, 'ID')[0] == 'string'}
        assert identifiers
        for x in range(1, doc.xref_length()):
            if doc.xref_get_key(x, 'Type')[1] != '/StructElem':
                continue
            kind, value = doc.xref_get_key(x, 'A/Headers')
            if kind == 'array':
                assert any(fitz.get_pdf_str(identifier) in value for identifier in identifiers)
