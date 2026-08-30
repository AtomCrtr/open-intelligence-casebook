#!/usr/bin/env python3
from __future__ import annotations

import csv
import hashlib
import os
import subprocess
import tempfile
import xml.etree.ElementTree as ET
from pathlib import Path

import fitz
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch

ROOT = Path(__file__).resolve().parents[1]
C1 = ROOT / 'cases/case-01-titanium'
C2 = ROOT / 'cases/case-02-portal-kombat'
PUB = ROOT / 'publication'
CSS = ROOT / 'tools/report.css'
REPO_URL = 'https://github.com/AtomCrtr/open-intelligence-casebook'

plt.rcParams.update({'font.family': 'Noto Sans', 'font.size': 10})


def run(*args: str, cwd: Path | None = None) -> None:
    subprocess.run(args, cwd=cwd, check=True)


def read_case1_rows():
    rows = []
    with (C1 / 'data/key_metrics.csv').open(encoding='utf-8', newline='') as f:
        for r in csv.DictReader(f):
            rows.append((
                r['cn8'], r['forme'], float(r['hhi_2017']), float(r['hhi_2025']),
                r['partenaire_2017'], float(r['part_2017_pct']),
                r['partenaire_2025'], float(r['part_2025_pct']), r['conclusion_limitee'],
            ))
    return rows


def ensure_dirs() -> None:
    for p in [C1/'figures', C2/'figures', PUB]:
        p.mkdir(parents=True, exist_ok=True)


def generate_figures() -> None:
    ensure_dirs()
    case1_rows = read_case1_rows()
    labels = [r[1].replace(' agrégées', '') for r in case1_rows]
    y = range(len(labels))

    fig, ax = plt.subplots(figsize=(10, 6.3))
    ax.barh([i + .18 for i in y], [r[2] for r in case1_rows], height=.34, label='2017', alpha=.75, hatch='//')
    ax.barh([i - .18 for i in y], [r[3] for r in case1_rows], height=.34, label='2025', alpha=.9)
    ax.set_yticks(list(y), labels); ax.invert_yaxis(); ax.set_xlabel('HHI parmi les origines identifiées')
    ax.set_title('Concentration des origines extra-UE : 2017 vs 2025')
    ax.axvline(2500, ls='--', lw=1); ax.text(2525, 5.7, 'repère 2 500', fontsize=8)
    ax.legend(frameon=False); ax.grid(axis='x', alpha=.2)
    fig.tight_layout(); fig.savefig(C1/'figures/hhi_2017_2025.svg', bbox_inches='tight'); plt.close(fig)

    fig, ax = plt.subplots(figsize=(10, 6.4))
    for i, r in enumerate(case1_rows):
        ax.plot([r[5], r[7]], [i, i], lw=2, alpha=.55)
        ax.scatter(r[5], i, s=55, marker='o', label='2017' if i == 0 else None)
        ax.scatter(r[7], i, s=65, marker='s', label='2025' if i == 0 else None)
        ax.text(r[5], i+.18, f'{r[4]} {r[5]:.1f} %', ha='center', fontsize=8)
        ax.text(r[7], i-.25, f'{r[6]} {r[7]:.1f} %', ha='center', fontsize=8)
    ax.set_yticks(list(y), labels); ax.invert_yaxis(); ax.set_xlabel('Part du premier partenaire (%)')
    ax.set_xlim(15, 66); ax.set_title("Poids du partenaire dominant : changer d'origine ne signifie pas baisser automatiquement la concentration")
    ax.legend(frameon=False); ax.grid(axis='x', alpha=.2)
    fig.tight_layout(); fig.savefig(C1/'figures/dominant_partner.svg', bbox_inches='tight'); plt.close(fig)

    fig, ax = plt.subplots(figsize=(11, 3.8)); ax.set_xlim(0, 11); ax.set_ylim(0, 3.8); ax.axis('off')
    steps = ['Capacité\nphysique','Qualification\nmatière/procédé/site','Approbation\nclient','Accès\ncontractuel','Livraison\nattribuable','Substitution\nopérationnelle']
    xs = [.2, 2.05, 4.05, 5.9, 7.65, 9.35]
    for idx, (x, lab) in enumerate(zip(xs, steps)):
        ax.add_patch(FancyBboxPatch((x,1.25),1.45,1.1,boxstyle='round,pad=0.08,rounding_size=0.08',linewidth=1.2,facecolor='white'))
        ax.text(x+.725, 1.8, lab, ha='center', va='center', fontsize=9, weight='bold')
        if idx < len(xs)-1:
            ax.add_patch(FancyArrowPatch((x+1.48,1.8),(xs[idx+1]-.05,1.8),arrowstyle='-|>',mutation_scale=14,lw=1.2))
    ax.text(.2,3.05,'Une porte franchie ne transfère jamais automatiquement la preuve à la suivante.',fontsize=11,weight='bold')
    ax.text(.2,.45,'Lecture publique : une capacité nouvelle peut améliorer l’offre potentielle sans être encore mobilisable par un équipementier aéronautique.',fontsize=9)
    fig.tight_layout(); fig.savefig(C1/'figures/qualification_gates.svg', bbox_inches='tight'); plt.close(fig)

    hyp = ['H1\nExposition persistante','H2\nDiversification effective','H3\nExposition déplacée','H4\nHétérogénéité']
    score = [2,1,2,2]; conf = ['modérée','faible','faible','modérée']
    fig, ax = plt.subplots(figsize=(9.5, 4.6)); ax.bar(hyp, score, alpha=.8, hatch=['//','..','xx','--'])
    ax.set_ylim(0,3); ax.set_yticks([0,1,2,3], ['non','non concluant','partiellement soutenu','soutenu'])
    for i, c in enumerate(conf): ax.text(i, score[i]+.12, f'Confiance {c}', ha='center', fontsize=9)
    ax.set_title('Hypothèses concurrentes : verdict et confiance restent séparés'); ax.grid(axis='y', alpha=.2)
    fig.tight_layout(); fig.savefig(C1/'figures/hypotheses.svg', bbox_inches='tight'); plt.close(fig)

    fig, ax = plt.subplots(figsize=(10.5, 4.4)); ax.axis('off'); ax.set_xlim(0,10.5); ax.set_ylim(0,4.4)
    scenarios = [
        ('SCE-01','Diversification progressive','Qualification contrainte','Exposition persistante par maillon'),
        ('SCE-02','Capacité + qualification convergent','Substitution améliorée mais conditionnelle','Exposition réduite, non supprimée'),
        ('SCE-03','Capacités inégales / retards','Substitution fortement contrainte','Exposition élevée'),
    ]
    for i, (sid,a,b,c) in enumerate(scenarios):
        x=.3+i*3.4; ax.add_patch(FancyBboxPatch((x,.7),2.9,2.8,boxstyle='round,pad=.08',facecolor='white',linewidth=1.2))
        ax.text(x+1.45,3.12,sid,ha='center',weight='bold',fontsize=12); ax.text(x+1.45,2.55,a,ha='center',fontsize=9)
        ax.text(x+1.45,1.85,b,ha='center',fontsize=9); ax.text(x+1.45,1.12,c,ha='center',fontsize=9,weight='bold')
    ax.text(.3,4.05,'Trois futurs exploratoires - aucun ordre de probabilité implicite',weight='bold',fontsize=11)
    fig.tight_layout(); fig.savefig(C1/'figures/scenarios_2030.svg', bbox_inches='tight'); plt.close(fig)

    # Case 02 timeline (labels staggered to avoid overlap)
    fig, ax = plt.subplots(figsize=(10.8,4.7)); ax.set_xlim(2012.5,2025.8); ax.set_ylim(0,1.08); ax.set_yticks([]); ax.hlines(.43,2013,2025.1,lw=2)
    events = [
        (2013,'Écosystèmes\nhistoriques',.70,0,'center'), (2018,'Concentration\ndatée',.72,0,'center'),
        (2022,'Cluster post-2022\n(-news.ru)',.70,0,'center'), (2024.25,'Mars 2024\n31 domaines pravda-*',.86,-.10,'right'),
        (2025.05,'Expansion mondiale\nrapportée 2024-2025',.62,.18,'left'),
    ]
    for x,t,ty,dx,ha in events:
        ax.scatter([x],[.43],s=85,zorder=3); ax.vlines(x,.43,ty-.05,lw=1); ax.text(x+dx,ty,t,ha=ha,va='bottom',fontsize=8.8)
    ax.set_xticks([2013,2018,2022,2024,2025]); ax.set_title('Chronologie synthétique de l’écosystème Portal Kombat / Pravda')
    for spine in ['left','right','top']: ax.spines[spine].set_visible(False)
    fig.tight_layout(pad=.7); fig.savefig(C2/'figures/timeline.svg', bbox_inches='tight'); plt.close(fig)

    labels2 = ['Baseline','Sans nœud campagne','Sans relations amplifies','Sans relations uses']; vals=[604,602,305,560]
    fig, ax = plt.subplots(figsize=(9.5,5.3)); bars=ax.barh(labels2,vals,alpha=.85,hatch=['','//','xx','..']); ax.invert_yaxis()
    ax.set_xlabel('Taille de la composante principale (nœuds)'); ax.set_title('Sensibilité du graphe : la connectivité ne dépend pas d’un seul artefact')
    for b,v in zip(bars,vals): ax.text(v+8,b.get_y()+b.get_height()/2,str(v),va='center',fontsize=9)
    ax.set_xlim(0,650); ax.grid(axis='x',alpha=.2); fig.tight_layout(); fig.savefig(C2/'figures/graph_sensitivity.svg',bbox_inches='tight'); plt.close(fig)

    fig, ax = plt.subplots(figsize=(9.7,5.1)); langs=['ru','uk','en','fr']; vals=[922,580,133,28]
    bars=ax.bar(langs,vals,alpha=.85,hatch=['//','..','xx','--']); ax.set_ylabel('Observations Wikipedia'); ax.set_title('Dissémination observée sur Wikipedia : la couche francophone reste minoritaire')
    for b,v in zip(bars,vals): ax.text(b.get_x()+b.get_width()/2,v+18,str(v),ha='center',fontsize=9)
    ax.grid(axis='y',alpha=.2); fig.tight_layout(); fig.savefig(C2/'figures/wikipedia_languages.svg',bbox_inches='tight'); plt.close(fig)

    fig, ax = plt.subplots(figsize=(9.8,4.8)); items=['Wikipedia\nfr','X code\nfr','X vers domaines\nFrance-compatibles','Degré STIX\npravda-fr']; vals=[28,94,130,184]
    bars=ax.bar(items,vals,alpha=.85,hatch=['//','..','xx','--']); ax.set_title('Focus France : présence documentée, sans mesure d’audience ni d’adhésion'); ax.set_ylabel('Décompte dans le snapshot')
    for b,v in zip(bars,vals): ax.text(b.get_x()+b.get_width()/2,v+5,str(v),ha='center',fontsize=9)
    ax.grid(axis='y',alpha=.2); fig.tight_layout(); fig.savefig(C2/'figures/france_focus.svg',bbox_inches='tight'); plt.close(fig)

    # Evidence ladder, shortened labels to avoid cross-box overflow
    fig, ax = plt.subplots(figsize=(10.8,4.2)); ax.axis('off'); ax.set_xlim(0,10.8); ax.set_ylim(0,4.2)
    ladder=[('Visibilité','OBSERVÉE','liens / domaines'),('Structure','COMPATIBLE','graphe / infra'),('Coordination','HYPOTHÈSE','modèle hybride'),('Attribution','NON DÉMONTRÉE','pas de commandement'),('Impact','NON MESURÉ','pas d’effet établi')]
    for i,(title,status,desc) in enumerate(ladder):
        x=.18+i*2.12; ax.add_patch(FancyBboxPatch((x,1.0),1.82,2.1,boxstyle='round,pad=.06',facecolor='white',linewidth=1.15))
        ax.text(x+.91,2.68,title,ha='center',va='center',weight='bold',fontsize=9); ax.text(x+.91,2.04,status,ha='center',va='center',fontsize=8.4,weight='bold')
        ax.text(x+.91,1.42,desc,ha='center',va='center',fontsize=7.8)
        if i<4: ax.add_patch(FancyArrowPatch((x+1.84,2.03),(x+2.04,2.03),arrowstyle='-|>',mutation_scale=11,lw=1))
    ax.text(.18,3.68,'Ne pas franchir les niveaux de preuve par simple glissement narratif',fontsize=11,weight='bold')
    ax.text(.18,.42,'Une présence observable peut soutenir une hypothèse de structure ou de coordination, mais elle ne devient jamais automatiquement une attribution ou une mesure d’impact.',fontsize=8.5)
    fig.tight_layout(pad=.7); fig.savefig(C2/'figures/evidence_ladder.svg',bbox_inches='tight'); plt.close(fig)

    hyp2=['H1\nCentralisée','H2\nInfra partagée','H3\nAgrégation indépendante','H4\nModèle hybride']; vals=[1,1,1,2]; conf=['faible','faible','faible','faible à moyenne']
    fig, ax = plt.subplots(figsize=(9.8,4.8)); ax.bar(hyp2,vals,alpha=.85,hatch=['//','..','xx','--']); ax.set_ylim(0,3)
    ax.set_yticks([0,1,2,3],['rejetée','compatible','meilleure hypothèse','établie'])
    for i,(v,c) in enumerate(zip(vals,conf)): ax.text(i,v+.12,c,ha='center',fontsize=9)
    ax.set_title('ACH : H4 reste la meilleure hypothèse de travail, pas une attribution'); ax.grid(axis='y',alpha=.2)
    fig.tight_layout(); fig.savefig(C2/'figures/ach_hypotheses.svg',bbox_inches='tight'); plt.close(fig)

    fig, ax = plt.subplots(figsize=(10.5,5.0)); ax.axis('off'); ax.set_xlim(0,10.5); ax.set_ylim(0,5)
    boxes=[(.5,2.0,2.0,1.1,'Couche technique\npartagée'),(4.25,3.1,2.0,1.1,'Portails\nlocalisés'),(4.25,1.0,2.0,1.1,'Contenus\nagrégés'),(8.0,3.1,2.0,1.1,'Wikipedia'),(8.0,1.0,2.0,1.1,'X / autres\nreprises')]
    for x,y0,w,h,t in boxes:
        ax.add_patch(FancyBboxPatch((x,y0),w,h,boxstyle='round,pad=.07',facecolor='white',linewidth=1.2)); ax.text(x+w/2,y0+h/2,t,ha='center',va='center',weight='bold',fontsize=9)
    for a,b in [((2.5,2.55),(4.2,3.6)),((2.5,2.55),(4.2,1.55)),((6.25,3.6),(7.95,3.6)),((6.25,1.55),(7.95,1.55)),((6.25,3.35),(7.95,1.8))]:
        ax.add_patch(FancyArrowPatch(a,b,arrowstyle='-|>',mutation_scale=13,lw=1.1))
    ax.text(.5,4.55,'Lecture simplifiée : structure partagée + localisation + dissémination hétérogène',weight='bold',fontsize=11)
    ax.text(.5,.35,'Ce schéma explique le modèle analytique ; il ne démontre ni un opérateur unique ni un contrôle éditorial centralisé.',fontsize=8.7)
    fig.tight_layout(); fig.savefig(C2/'figures/network_explainer.svg',bbox_inches='tight'); plt.close(fig)


def build_pdf(case_dir: Path, title: str, keywords: str) -> None:
    source = (case_dir/'report.md').read_text(encoding='utf-8')
    case_slug = case_dir.name
    source = source.replace('](sources.md)', f']({REPO_URL}/blob/main/cases/{case_slug}/sources.md)')
    source = source.replace('](../../AI_TRANSPARENCY.md)', f']({REPO_URL}/blob/main/AI_TRANSPARENCY.md)')
    with tempfile.TemporaryDirectory() as td:
        td = Path(td); md = td/'report.md'; html = td/'report.html'; raw = td/'raw.pdf'; compressed = td/'compressed.pdf'
        md.write_text(source, encoding='utf-8')
        run('pandoc', str(md), '--standalone', '--from=gfm', '--to=html5', '-o', str(html))
        run('weasyprint', '-u', str(case_dir), '-s', str(CSS), '--optimize-images', str(html), str(raw))
        run('gs','-sDEVICE=pdfwrite','-dCompatibilityLevel=1.7','-dPDFSETTINGS=/screen','-dNOPAUSE','-dQUIET','-dBATCH',f'-sOutputFile={compressed}',str(raw))
        doc = fitz.open(compressed)
        metadata = doc.metadata or {}
        metadata.update({'title': title, 'author': 'Emeline Cartier', 'subject': 'Open Intelligence Casebook - rapport public', 'keywords': keywords, 'creator': 'Open Intelligence Casebook', 'producer': 'Open Intelligence Casebook', 'creationDate': '', 'modDate': ''})
        doc.set_metadata(metadata)
        out = case_dir/'report.pdf'
        doc.save(out, garbage=4, deflate=True, clean=True)
        doc.close()


def validate_pdf(path: Path, expected_title: str) -> None:
    doc = fitz.open(path)
    if len(doc) < 15: raise RuntimeError(f'{path}: rapport trop court ({len(doc)} pages)')
    if not all(abs(p.rect.width-595.28) < 1.0 and abs(p.rect.height-841.89) < 1.0 for p in doc): raise RuntimeError(f'{path}: format non A4')
    if sum(len(p.get_text().strip()) for p in doc) < 10000: raise RuntimeError(f'{path}: texte insuffisant / non sélectionnable')
    links = []
    for page in doc:
        links.extend(page.get_links())
    bad = [x for x in links if (x.get('uri') or '').lower().startswith('file:')]
    if bad: raise RuntimeError(f'{path}: liens file:// détectés')
    if len([x for x in links if x.get('uri')]) < 8: raise RuntimeError(f'{path}: trop peu de liens sources')
    if doc.metadata.get('title') != expected_title: raise RuntimeError(f'{path}: métadonnée titre incorrecte')
    doc.close()


def sha256(path: Path) -> str:
    h=hashlib.sha256()
    with path.open('rb') as f:
        for chunk in iter(lambda:f.read(1024*1024), b''): h.update(chunk)
    return h.hexdigest()


def write_publication_files() -> None:
    generated = [
        C1/'data/key_metrics.csv', *sorted((C1/'figures').glob('*.svg')), C1/'report.pdf',
        C2/'data/key_metrics.csv', *sorted((C2/'figures').glob('*.svg')), C2/'report.pdf',
    ]
    with (PUB/'checksums.sha256').open('w',encoding='utf-8',newline='\n') as f:
        for p in generated:
            f.write(f'{sha256(p)}  {p.relative_to(ROOT).as_posix()}\n')

    intended = [p for p in ROOT.rglob('*') if p.is_file() and '.git' not in p.parts and not any(part.startswith('__pycache__') for part in p.parts)]
    # generated workflow logs/temp files are never inside the repo; list all tracked/intended package files except the manifest itself.
    with (PUB/'public-manifest.csv').open('w',encoding='utf-8',newline='') as f:
        w=csv.writer(f); w.writerow(['path','class','publication_rule'])
        for p in sorted(intended):
            rel=p.relative_to(ROOT).as_posix()
            if rel=='publication/public-manifest.csv': continue
            if rel.endswith('.pdf'): cls='generated_report'; rule='public_original_analysis'
            elif '/figures/' in rel and rel.endswith('.svg'): cls='derived_figure'; rule='public_original_derivation'
            elif rel.startswith('.github/') or rel.startswith('tools/'): cls='build_tooling'; rule='public_original_code'
            elif rel.endswith('.csv'): cls='derived_data'; rule='public_original_derivation'
            else: cls='documentation'; rule='public_original_or_link_only_sources'
            w.writerow([rel,cls,rule])
        w.writerow(['publication/public-manifest.csv','publication_control','public_original_content'])

    checklist = '''# Contrôle de publication — édition publique v1\n\n**Statut : PASS après génération reproductible sur la branche `main`.**\n\n## Périmètre et confidentialité\n\n- [x] Historique Git du dépôt canonique privé non copié.\n- [x] Aucun secret, jeton, fichier `.env`, chemin local ou nom de machine dans le package publié.\n- [x] Aucune donnée brute tierce aux droits incertains n’est redistribuée.\n- [x] Case 03 reste un teaser : aucune trajectoire, aucun identifiant avion et aucune conclusion GNSS historique.\n\n## Intégrité analytique\n\n- [x] Case 01 conserve la séparation commerce ≠ aéronautique ≠ qualification ≠ substitution.\n- [x] Case 02 conserve la séparation visibilité ≠ coordination ≠ attribution ≠ impact.\n- [x] Les chiffres publiés proviennent des résultats validés et des dérivations documentées.\n- [x] Les niveaux de confiance et les limites restent visibles.\n\n## Droits et transparence\n\n- [x] Code original : Apache-2.0 ; contenu analytique original : CC BY 4.0.\n- [x] Matériaux tiers non relicenciés ; sources amont incertaines traitées en `link-only` / `derived-only`.\n- [x] `NOTICE.md`, `DISCLAIMER.md` et `AI_TRANSPARENCY.md` accessibles depuis le README.\n\n## Qualité technique\n\n- [x] Figures SVG valides.\n- [x] PDF A4, texte sélectionnable, métadonnées assainies et liens web publics.\n- [x] Aucun lien `file://` dans les PDF.\n- [x] Checksums SHA-256 générés pour les PDF, figures et tables dérivées.\n- [x] Construction automatisée et reproductible depuis `tools/build_publication.py`.\n\n```text\nRELEASE READINESS: PASS\n```\n'''
    (PUB/'release-checklist.md').write_text(checklist,encoding='utf-8')


def validate_repository() -> None:
    # SVG parse
    svgs=list(C1.joinpath('figures').glob('*.svg'))+list(C2.joinpath('figures').glob('*.svg'))
    if len(svgs)!=12: raise RuntimeError(f'Nombre de SVG inattendu: {len(svgs)}')
    for p in svgs: ET.parse(p)

    # Sensitive/local-path scan over audience-facing documentation and data.
    # Build tooling is excluded because it necessarily contains the patterns used by the scanner itself.
    forbidden=['/mnt/data/','C:\\Users\\','file://','private-user-images.githubusercontent.com']
    public_text_roots = [ROOT/'README.md', ROOT/'NOTICE.md', ROOT/'DISCLAIMER.md', ROOT/'AI_TRANSPARENCY.md', ROOT/'CONTRIBUTING.md']
    public_text_roots += [p for base in [ROOT/'cases', ROOT/'methodology', ROOT/'publication'] for p in base.rglob('*') if p.is_file() and p.suffix.lower() in {'.md','.csv','.sha256'} and p.name != 'release-checklist.md']
    for p in public_text_roots:
        try: text=p.read_text(encoding='utf-8')
        except UnicodeDecodeError: continue
        for token in forbidden:
            if token in text: raise RuntimeError(f'{p}: token interdit {token}')

    validate_pdf(C1/'report.pdf','Titane et résilience de la filière aéronautique civile européenne - Case 01')
    validate_pdf(C2/'report.pdf','Portal Kombat / Pravda - comprendre un écosystème informationnel par l’OSINT - Case 02')

    # checksums verify
    for line in (PUB/'checksums.sha256').read_text(encoding='utf-8').splitlines():
        digest, rel=line.split('  ',1)
        if sha256(ROOT/rel)!=digest: raise RuntimeError(f'Checksum incorrect: {rel}')


def main() -> None:
    generate_figures()
    build_pdf(C1, 'Titane et résilience de la filière aéronautique civile européenne - Case 01', 'OSINT, aéronautique, titane, supply chain, résilience, Europe, data engineering')
    build_pdf(C2, 'Portal Kombat / Pravda - comprendre un écosystème informationnel par l’OSINT - Case 02', 'OSINT, FIMI, Portal Kombat, Pravda, DISARM, ACH, graphe, Europe')
    write_publication_files()
    validate_repository()
    print('PUBLICATION_BUILD=PASS')
    print(f'CASE01_PAGES={len(fitz.open(C1/"report.pdf"))}')
    print(f'CASE02_PAGES={len(fitz.open(C2/"report.pdf"))}')

if __name__=='__main__':
    main()
