"""Reader-facing PDF contracts: usable evidence links and complete integrity coverage."""
import csv
import shutil

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
        assert any(link['kind'] == fitz.LINK_GOTO for link in links)
        assert doc.get_toc(), 'Le lecteur doit pouvoir naviguer par les signets PDF.'
        assert any(page.get_image_info() for page in doc), 'Les figures doivent rester intégrées au PDF.'
        text = ' '.join(' '.join(page.get_text().split()) for page in doc)
        assert 'La confiance finale repose sur des faits vérifiés.' in text


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
