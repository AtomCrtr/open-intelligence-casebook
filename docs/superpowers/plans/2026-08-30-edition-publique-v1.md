# Édition publique v1 - Plan d'implémentation

> **Pour les agents d'exécution :** utiliser `superpowers:subagent-driven-development` si des sous-agents sont disponibles, sinon `superpowers:executing-plans`. Les étapes utilisent des cases à cocher pour le suivi.

**Objectif :** construire la première édition publique assainie d'Open Intelligence Casebook avec un README portfolio, les Cases 01 et 02 en rapports Markdown/PDF détaillés, un teaser Case 03, la méthodologie commune et un gate final de publication.

**Architecture :** le dépôt public possède un historique neuf et ne reçoit que des artefacts explicitement sélectionnés. Les deux rapports sont régénérés à partir de résultats déjà validés dans le dépôt privé, avec une identité visuelle commune, puis vérifiés par rendu page par page avant publication. Les données tierces brutes aux droits incertains restent hors du dépôt ; seules des dérivations publiques, des explications et des liens sont publiés.

**Stack technique :** Markdown, Python 3.11+, `python-docx`, Matplotlib, LibreOffice headless, outils PDF internes de rendu/inspection, GitHub.

**Spécification :** `docs/superpowers/specs/2026-08-30-public-edition-design.md`

## Contraintes globales

- Langue principale : français clair ; résumé anglais facultatif et court.
- Aucun historique Git du dépôt privé n'est copié.
- Aucun dataset brut tiers n'est publié sans droit explicite de redistribution.
- Case 01 : résultats limités au périmètre du snapshot public ayant déjà passé le gate S11.5.
- Case 02 : les corpus amont aux droits incertains sont uniquement référencés par lien ; seuls les résultats dérivés publics sont copiés.
- Case 03 : teaser uniquement ; aucune donnée, fixture, trajectoire, identifiant avion ou résultat historique.
- Chaque affirmation chiffrée doit provenir d'un résultat validé ou d'une dérivation publique documentée.
- Les PDF doivent être lisibles sur A4, accessibles aux non-spécialistes et contrôlés visuellement page par page.
- Les métadonnées finales doivent être assainies et les checksums SHA-256 publiés.

---

### Tâche 1 : Structure éditoriale et fichiers de gouvernance

**Fichiers :**
- Créer : `README.md`
- Créer : `LICENSE`
- Créer : `NOTICE.md`
- Créer : `DISCLAIMER.md`
- Créer : `AI_TRANSPARENCY.md`
- Créer : `CONTRIBUTING.md`
- Créer : `methodology/analytical-cycle.md`
- Créer : `methodology/source-evaluation.md`
- Créer : `methodology/confidence-and-hypotheses.md`
- Créer : `methodology/reproducibility.md`

**Produit :** une page d'accueil lisible en moins de deux minutes et les règles de gouvernance visibles dès la première navigation.

- [ ] Rédiger le README avec les trois cas, leurs statuts, les compétences démontrées et la méthode commune.
- [ ] Rédiger licence, notice, disclaimer et transparence IA sans importer de texte privé inutile.
- [ ] Rédiger quatre pages méthodologiques courtes et pédagogiques.
- [ ] Vérifier qu'aucune formulation ne présente une hypothèse comme un fait établi.
- [ ] Vérifier tous les liens internes créés à cette étape.

### Tâche 2 : Édition publique du Case 01 - Titane

**Fichiers :**
- Créer : `cases/case-01-titanium/README.md`
- Créer : `cases/case-01-titanium/report.md`
- Créer : `cases/case-01-titanium/methodology.md`
- Créer : `cases/case-01-titanium/sources.md`
- Créer : `cases/case-01-titanium/data/key_metrics.csv`
- Créer : `cases/case-01-titanium/figures/*.png`
- Générer : `cases/case-01-titanium/report.pdf`

**Source analytique :** Case 01 canonique, limité aux résultats déjà présents dans le snapshot S11.5 ayant obtenu `RELEASE READINESS: PASS`.

**Produit :** rapport public d'environ 20-30 pages expliquant la résilience de la chaîne d'approvisionnement du titane aéronautique européen.

- [ ] Extraire uniquement les chiffres, conclusions, limites, hypothèses et sources nécessaires au récit public.
- [ ] Construire `key_metrics.csv` avec les six catégories CN8, HHI 2017/2025, partenaires dominants et conclusions limitées.
- [ ] Générer des figures lisibles : HHI, origines dominantes, chaîne qualification/substitution, maturité industrielle et matrice scénarios/options.
- [ ] Rédiger le rapport Markdown en distinguant commerce toutes industries et question aéronautique.
- [ ] Inclure systématiquement « ce que cela ne prouve pas » pour les données douanières et les capacités industrielles.
- [ ] Générer un DOCX de travail puis un PDF final à partir de la même source éditoriale.
- [ ] Rendre le PDF en PNG et inspecter chaque page ; corriger tout rognage, chevauchement, table illisible ou glyphes défectueux.
- [ ] Contrôler les métadonnées et calculer le SHA-256 du PDF final.

### Tâche 3 : Édition publique du Case 02 - Portal Kombat / Pravda

**Fichiers :**
- Créer : `cases/case-02-portal-kombat/README.md`
- Créer : `cases/case-02-portal-kombat/report.md`
- Créer : `cases/case-02-portal-kombat/methodology.md`
- Créer : `cases/case-02-portal-kombat/sources.md`
- Créer : `cases/case-02-portal-kombat/data/key_metrics.csv`
- Créer : `cases/case-02-portal-kombat/figures/*.png`
- Générer : `cases/case-02-portal-kombat/report.pdf`

**Source analytique :** rapport final Lot 3, brief exécutif et résultats dérivés validés ; aucun corpus tiers brut marqué `review-required`.

**Produit :** rapport public d'environ 20-30 pages expliquant comment caractériser une campagne de manipulation de l'information à partir de sources ouvertes.

- [ ] Extraire les résultats publics : 371 domaines, graphe 609/1 013, chronologie, France/UE, observations Wikipedia/X, sensibilité du graphe et ACH.
- [ ] Construire `key_metrics.csv` uniquement avec des résultats dérivés et publiables.
- [ ] Générer des figures explicatives : chronologie, architecture du réseau, sensibilité, focus France, dissémination, matrice visibilité/coordination/attribution/impact et ACH H1-H4.
- [ ] Rédiger le rapport en français clair avec définition de FIMI, STIX, DISARM et ACH.
- [ ] Conserver explicitement les limites : pas d'attribution étatique démontrée, pas de commandement éditorial démontré, pas d'impact humain mesuré, pas d'empoisonnement LLM démontré.
- [ ] Rédiger la revue des droits propre au Case 02 et convertir tout contenu amont incertain en référence par lien uniquement.
- [ ] Générer un DOCX de travail puis le PDF final.
- [ ] Rendre le PDF en PNG et inspecter chaque page ; corriger toute anomalie de mise en page.
- [ ] Contrôler les métadonnées et calculer le SHA-256 du PDF final.

### Tâche 4 : Teaser public du Case 03

**Fichiers :**
- Créer : `cases/case-03-gnss-interference/README.md`

**Produit :** une page transparente présentant la question GNSS sans publier de résultat prématuré.

- [ ] Présenter la question, le périmètre européen, l'OSINT institutionnel, le GEOINT et l'analyse de trajectoires comme méthodes en développement.
- [ ] Écrire explicitement `design gelé avant données réelles` et `aucune conclusion historique publiée`.
- [ ] Ne publier aucune fixture, donnée GPSJAM, sortie événementielle ou identifiant d'aéronef.

### Tâche 5 : Package de publication et gate final

**Fichiers :**
- Créer : `publication/public-manifest.csv`
- Créer : `publication/rights-review.md`
- Créer : `publication/release-checklist.md`
- Créer : `publication/checksums.sha256`

**Produit :** preuve lisible que l'édition publique a été vérifiée avant fusion dans `main`.

- [ ] Construire le manifeste exact des fichiers destinés à la publication.
- [ ] Vérifier secrets, données personnelles, chemins locaux, noms de machines et identifiants opérationnels interdits.
- [ ] Vérifier les droits de chaque artefact copié ; tout élément tiers incertain reste link-only.
- [ ] Vérifier les liens internes et la présence de licence/notice/disclaimer/transparence IA depuis le README.
- [ ] Inspecter les deux PDF et leurs métadonnées.
- [ ] Générer les checksums SHA-256.
- [ ] Revoir les affirmations importantes contre les résultats canoniques.
- [ ] Enregistrer `RELEASE READINESS: PASS` uniquement si tous les contrôles sont effectivement validés ; sinon conserver un statut bloqué et documenter le finding.

### Tâche 6 : Intégration GitHub

**Produit :** branche de publication vérifiée, prête à être fusionnée dans `main`.

- [ ] Vérifier le diff complet et confirmer qu'aucun fichier privé ou intermédiaire n'est présent.
- [ ] Vérifier que les deux PDF sont bien présents et ouvrables depuis GitHub.
- [ ] Ouvrir une pull request de la branche de construction vers `main` avec résumé, contrôles effectués et statut du gate.
- [ ] Ne fusionner que si le gate final est `PASS`.
