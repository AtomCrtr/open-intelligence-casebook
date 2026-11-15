# Construire l'édition publique

## Sources de vérité

- Chaque `cases/case-*/report.md` porte le texte de son rapport ; `READING_GUIDE.md` porte le guide de découverte.
- Les introductions expliquent les sujets ; les corps analytiques, sources et niveaux de confiance restent distincts de cette clarification éditoriale.
- `tools/report.html` et `tools/report.css` définissent le sommaire, les signets, la pagination et la présentation commune des six PDF.
- `data/key_metrics.csv` porte les métriques publiées.
- `provenance.csv` porte les liens publics affirmation-source et les lignées informationnelles.
- `tools/build_publication.py` génère les figures, les PDF, les checksums, le manifeste et la checklist de publication (dérivée des contrôles exécutés).

Le texte analytique ne doit pas être recopié dans le générateur PDF.

## Environnement Linux de référence

Python **3.12.12** (épinglé dans la CI par `actions/setup-python`), sur `ubuntu-24.04`.

```bash
sudo apt-get update
sudo apt-get install -y pandoc poppler-utils fonts-noto-core fonts-noto-extra
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

Le générateur produit les quatre rapports, `READING_GUIDE.pdf` et `BEGINNER_READING_TEST.pdf`. Il valide notamment le format A4, le texte sélectionnable sans caractères de contrôle invalides, les liens publics, les métadonnées PDF, le schéma de provenance et les checksums.

Pour contrôler la reproductibilité binaire, exécuter deux constructions successives et comparer les empreintes des quatre rapports PDF, du guide et du questionnaire. La CI Linux reste l'environnement de publication de référence.

## Solution locale Windows

Le script accepte `pypandoc_binary` si `pandoc` n'est pas disponible dans `PATH`. WeasyPrint requiert un runtime GTK compatible ; son chemin peut être fourni avec `WEASYPRINT_DLL_DIRECTORIES`. Ghostscript n’est plus utilisé : son passage `pdfwrite` corrompait le texte extrait des titres et du gras de certains rapports. Les PDF sont compressés sans perte par WeasyPrint et PyMuPDF. Le balisage de structure est conservé ; il ne vaut pas certification PDF/UA ni test avec un lecteur d’écran.

## Ordre de lecture

Chaque rapport contient une synthèse délimitée par `<!-- READER_SUMMARY_START -->` et `<!-- READER_SUMMARY_END -->`. Le générateur place cette synthèse après la couverture et avant le sommaire. Les titres et leurs liens restent dans le document. Les tests reconstruisent les rapports Titane et Portal Kombat pour contrôler les titres et le texte extrait.

Le [test de lecture](BEGINNER_READING_TEST.md) sert à recueillir une validation humaine ; sa préparation ne signifie pas que des débutants ont déjà testé les rapports.

Les identifiants des en-têtes de tableaux balisés et leurs références sont normalisés ensemble : WeasyPrint 68.0 les dérive sinon de la mémoire du processus. Cette normalisation conserve les relations cellule/en-tête et permet la comparaison binaire entre deux constructions.

## Recalculer des résultats avant de construire les PDF

```bash
python tools/reproduce_results.py titanium
python tools/reproduce_results.py portal
```

Le premier parcours est hors réseau et recalcule les douze comparaisons Titane à partir d’un sous-ensemble normalisé Eurostat publié avec attribution. Le second réacquiert en mémoire deux fichiers VIGINUM à un commit et une empreinte fixes, puis recalcule les domaines, le graphe et ses sensibilités. Voir les parcours [Titane](cases/case-01-titanium/REPRODUCE.md) et [Portal Kombat](cases/case-02-portal-kombat/REPRODUCE.md) pour le périmètre exact et les limites. La CI ne télécharge pas les corpus VIGINUM : les tests hors réseau utilisent des exemples synthétiques clairement identifiés.

La construction des figures vérifie le recalcul Titane et lit les mesures numériques Portal Kombat depuis `data/key_metrics.csv`. Une construction PDF seule ne recalcule pas les données VIGINUM ni les métriques Wikipedia/X.
