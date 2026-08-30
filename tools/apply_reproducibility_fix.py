#!/usr/bin/env python3
from pathlib import Path

p = Path(__file__).with_name('build_publication.py')
s = p.read_text(encoding='utf-8')

old_import = "import xml.etree.ElementTree as ET\nfrom pathlib import Path"
new_import = "import xml.etree.ElementTree as ET\n\n# Reproducible-build epoch: public edition date, 2026-08-30 UTC.\nos.environ.setdefault('SOURCE_DATE_EPOCH', '1788048000')\n\nfrom pathlib import Path"
if new_import not in s:
    if old_import not in s:
        raise RuntimeError('import anchor not found')
    s = s.replace(old_import, new_import, 1)

old_rc = "plt.rcParams.update({'font.family': 'Noto Sans', 'font.size': 10})"
new_rc = "plt.rcParams.update({'font.family': 'Noto Sans', 'font.size': 10, 'svg.hashsalt': 'open-intelligence-casebook-v1'})"
if new_rc not in s:
    if old_rc not in s:
        raise RuntimeError('rcParams anchor not found')
    s = s.replace(old_rc, new_rc, 1)

old_gs = "run('gs','-sDEVICE=pdfwrite','-dCompatibilityLevel=1.7','-dPDFSETTINGS=/screen','-dNOPAUSE','-dQUIET','-dBATCH',f'-sOutputFile={compressed}',str(raw))"
new_gs = "run('gs','-sDEVICE=pdfwrite','-dCompatibilityLevel=1.7','-dPDFSETTINGS=/screen','-dDeterministicID','-dOmitInfoDate=true','-dNOPAUSE','-dQUIET','-dBATCH',f'-sOutputFile={compressed}',str(raw))"
if new_gs not in s:
    if old_gs not in s:
        raise RuntimeError('Ghostscript anchor not found')
    s = s.replace(old_gs, new_gs, 1)

old_save = "        doc.save(out, garbage=4, deflate=True, clean=True)\n        doc.close()"
new_save = """        doc.save(out, garbage=4, deflate=True, clean=True, no_new_id=True)
        doc.close()

        # PyMuPDF preserves the upstream trailer /ID. Ghostscript's /ID may
        # still vary even when every content byte is stable. Normalize only
        # the two fixed-width 16-byte IDs without changing file offsets.
        pdf = out.read_bytes()
        marker = b'/ID[<'
        start = pdf.rfind(marker)
        if start < 0:
            raise RuntimeError(f'{out}: trailer /ID introuvable')
        first_start = start + len(marker)
        first_end = pdf.find(b'>', first_start)
        second_start = pdf.find(b'<', first_end) + 1
        second_end = pdf.find(b'>', second_start)
        if first_end - first_start != 32 or second_end - second_start != 32:
            raise RuntimeError(f'{out}: format /ID inattendu')
        zeros = b'0' * 32
        normalized = (pdf[:first_start] + zeros + pdf[first_end:second_start] +
                      zeros + pdf[second_end:])
        stable_id = hashlib.sha256(normalized).hexdigest()[:32].upper().encode('ascii')
        normalized = (normalized[:first_start] + stable_id + normalized[first_end:second_start] +
                      stable_id + normalized[second_end:])
        out.write_bytes(normalized)"""
if new_save not in s:
    if old_save not in s:
        raise RuntimeError('PDF save anchor not found')
    s = s.replace(old_save, new_save, 1)

p.write_text(s, encoding='utf-8', newline='\n')
Path(__file__).unlink()
print('REPRODUCIBILITY_HARDENING=APPLIED')
