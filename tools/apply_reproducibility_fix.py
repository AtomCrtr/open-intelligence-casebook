#!/usr/bin/env python3
from pathlib import Path

p = Path(__file__).with_name('build_publication.py')
s = p.read_text(encoding='utf-8')

replacements = [
    (
        "import xml.etree.ElementTree as ET\nfrom pathlib import Path",
        "import xml.etree.ElementTree as ET\n\n# Reproducible-build epoch: public edition date, 2026-08-30 UTC.\nos.environ.setdefault('SOURCE_DATE_EPOCH', '1788048000')\n\nfrom pathlib import Path",
    ),
    (
        "plt.rcParams.update({'font.family': 'Noto Sans', 'font.size': 10})",
        "plt.rcParams.update({'font.family': 'Noto Sans', 'font.size': 10, 'svg.hashsalt': 'open-intelligence-casebook-v1'})",
    ),
    (
        "run('gs','-sDEVICE=pdfwrite','-dCompatibilityLevel=1.7','-dPDFSETTINGS=/screen','-dNOPAUSE','-dQUIET','-dBATCH',f'-sOutputFile={compressed}',str(raw))",
        "run('gs','-sDEVICE=pdfwrite','-dCompatibilityLevel=1.7','-dPDFSETTINGS=/screen','-dDeterministicID','-dOmitInfoDate=true','-dNOPAUSE','-dQUIET','-dBATCH',f'-sOutputFile={compressed}',str(raw))",
    ),
    (
        "doc.save(out, garbage=4, deflate=True, clean=True)",
        "doc.save(out, garbage=4, deflate=True, clean=True, no_new_id=True)",
    ),
]

for old, new in replacements:
    if new in s:
        continue
    if old not in s:
        raise RuntimeError(f'Expected pattern not found: {old[:100]}')
    s = s.replace(old, new, 1)

p.write_text(s, encoding='utf-8', newline='\n')
Path(__file__).unlink()
print('REPRODUCIBILITY_HARDENING=APPLIED')
