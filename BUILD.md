# Construire l'édition publique

## Sources de vérité

- Chaque `cases/case-*/report.md` porte le texte de son rapport ; `READING_GUIDE.md` porte le guide de découverte.
- Les introductions expliquent les sujets ; les corps analytiques, sources et niveaux de confiance restent distincts de cette clarification éditoriale.
- `tools/report.html` et `tools/report.css` définissent le sommaire, les signets, la pagination et la présentation commune des cinq PDF.
- `data/key_metrics.csv` porte les métriques publiées.
- `provenance.csv` porte les liens publics affirmation-source et les lignées informationnelles.
- `tools/build_publication.py` génère les figures, les PDF, les checksums, le manifeste et la checklist de publication (dérivée des contrôles exécutés).

Le texte analytique ne doit pas être recopié dans le générateur PDF.

## Environnement Linux de référence

Python **3.12.12** (épinglé dans la CI par `actions/setup-python`), sur `ubuntu-24.04`.

```bash
sudo apt-get update
sudo apt-get install -y pandoc ghostscript fonts-noto-core fonts-noto-extra
python -m pip install \
  matplotlib==3.10.8 \
  pymupdf==1.26.7 \
  weasyprint==68.0 \
  pytest==8.4.1
```

## Construire et contrôler

```bash
PYTHONDONTWRITEBYTECODE=1 python -m pytest tests -q -p no:cacheprovider
python tools/build_publication.py
sha256sum -c publication/checksums.sha256
```

Le générateur produit les quatre rapports et `READING_GUIDE.pdf`. Il valide notamment le format A4, le texte sélectionnable, les liens publics, les métadonnées PDF, le schéma de provenance et les checksums.

Pour contrôler la reproductibilité binaire, exécuter deux constructions successives et comparer les empreintes des quatre rapports PDF et du guide. La CI Linux reste l'environnement de publication de référence.

## Solution locale Windows

Le script accepte `pypandoc_binary` si `pandoc` n'est pas disponible dans `PATH`. WeasyPrint requiert un runtime GTK compatible ; son chemin peut être fourni avec `WEASYPRINT_DLL_DIRECTORIES`. Ghostscript est optionnel pour une validation locale, mais reste installé et utilisé dans la CI de publication.
