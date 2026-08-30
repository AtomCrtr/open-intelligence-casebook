# Open Intelligence Casebook — Conception de l'édition publique

## Objectif

Créer une édition publique, propre et lisible du portfolio privé `osint-intelligence-casebook`, sans exposer l'historique du dépôt privé, les audits internes, les branches de travail, les données non redistribuables, les données personnelles ni les artefacts intermédiaires de recherche.

L'édition publique s'adresse aux recruteurs, analystes, décideurs, étudiants et lecteurs non spécialistes. Elle doit conserver une rigueur analytique élevée tout en restant compréhensible sans connaissance préalable de l'OSINT, des chaînes d'approvisionnement, de la FIMI, de DISARM ou du GEOINT.

## Modèle de publication

Le dépôt privé reste le dépôt canonique de travail. Le dépôt public `AtomCrtr/open-intelligence-casebook` constitue une surface de publication assainie avec un historique Git neuf.

Aucun historique Git du dépôt privé n'est copié. Chaque fichier public doit appartenir à l'une des catégories suivantes :

- contenu explicatif original rédigé pour l'édition publique ;
- copie assainie d'un artefact déjà audité et prêt à être publié ;
- tableau ou figure dérivé dont la redistribution est explicitement autorisée ;
- rapport généré à partir de résultats analytiques déjà validés ;
- fichier de méthodologie, attribution, licence, transparence ou avertissement nécessaire à une publication responsable.

Le dépôt public ne doit contenir aucun jeu de données brut tiers sauf si sa redistribution est explicitement autorisée.

## Périmètre de la première édition publique

### Case 01 — Résilience de la chaîne d'approvisionnement du titane

Statut : terminé et publiable à partir du snapshot public précédemment audité.

Contenu de l'édition publique :

- page de présentation concise du cas ;
- rapport public détaillé en Markdown ;
- rapport PDF public soigné ;
- figures sélectionnées et tableaux dérivés nécessaires à la compréhension des conclusions ;
- notes méthodologiques expliquant le HHI, les limites des sources, les portes de qualification, l'analyse de scénarios et les niveaux de confiance ;
- registre des sources et des attributions limité aux éléments compatibles avec une publication publique.

Le rapport public doit préserver la distinction centrale :

`disponibilité commerciale != qualification aéronautique != approbation client != substituabilité opérationnelle`.

Il doit également préserver la distinction entre les données commerciales couvrant toutes les industries et la question décisionnelle spécifique à l'aéronautique.

### Case 02 — Portal Kombat / Pravda et intégrité de l'information

Statut : rapport analytique terminé ; le package de publication doit faire l'objet de sa propre vérification assainissement/droits avant diffusion finale.

Contenu de l'édition publique :

- page de présentation concise du cas ;
- rapport public détaillé en Markdown ;
- rapport PDF public soigné ;
- figures compatibles avec une diffusion publique expliquant la chronologie, la structure du réseau, la dissémination, le focus France/UE, l'ACH et les niveaux de confiance ;
- décomptes et tableaux dérivés compatibles avec une diffusion publique ;
- méthodologie expliquant l'OSINT passif, l'analyse de sensibilité du graphe, l'usage de DISARM, la triangulation et les hypothèses concurrentes ;
- liens vers les sources et attribution, sans redistribuer les corpus bruts tiers dont la licence amont est incertaine ou marquée comme nécessitant une revue.

Le rapport ne doit pas affirmer une attribution étatique, un commandement éditorial, un impact humain mesuré ou un empoisonnement démontré des modèles de langage lorsque les preuves ne permettent pas ces conclusions.

### Case 03 — Interférences GNSS et aviation civile européenne

Statut : étude en cours.

La première édition publique ne contient qu'une courte présentation décrivant la question de recherche, les méthodes en cours de développement et l'état d'avancement. Elle doit préciser explicitement que le design analytique a été gelé avant l'inspection de trajectoires réelles et qu'aucune conclusion historique sur les interférences GNSS n'est encore publiée.

Aucune donnée de travail du Case 03, aucun historique de branche, aucune donnée GPSJAM en volume, aucun identifiant d'aéronef, aucune sortie événementielle et aucune fixture synthétique ne sont publiés dans la première édition publique.

## Architecture de l'information du dépôt public

```text
README.md
LICENSE
NOTICE.md
DISCLAIMER.md
AI_TRANSPARENCY.md
CONTRIBUTING.md

cases/
  case-01-titanium/
    README.md
    report.md
    report.pdf
    figures/
    data/
    methodology.md
    sources.md

  case-02-portal-kombat/
    README.md
    report.md
    report.pdf
    figures/
    data/
    methodology.md
    sources.md

  case-03-gnss-interference/
    README.md

methodology/
  analytical-cycle.md
  source-evaluation.md
  confidence-and-hypotheses.md
  reproducibility.md

publication/
  public-manifest.csv
  rights-review.md
  release-checklist.md
  checksums.sha256

docs/superpowers/
  specs/
  plans/
```

## Conception du README

Le README racine sert de page d'accueil du portfolio et doit être compréhensible en moins de deux minutes.

Il contient :

1. une phrase présentant l'objectif du portfolio ;
2. une courte explication de ce qu'est un casebook d'intelligence ;
3. des cartes ou sections compactes pour le Case 01, le Case 02 et le Case 03 ;
4. des liens directs vers les deux PDF publics terminés ;
5. un statut transparent pour chaque cas ;
6. les compétences démontrées : OSINT, GEOINT, data engineering, traçabilité des preuves, ACH, gestion de l'incertitude et reproductibilité ;
7. un schéma court de la méthode commune ;
8. les principes de publication et d'éthique ;
9. des liens vers la méthodologie, la transparence IA, la licence, la notice et le disclaimer.

Le README ne doit ni exagérer le niveau d'expertise ni présenter des hypothèses analytiques comme des faits établis.

## Conception éditoriale des PDF

Deux rapports publics sont produits pour la première édition, un pour chaque cas terminé.

Longueur cible : environ 20 à 30 pages A4 par rapport, avec possibilité de varier si la clarté l'exige.

Les deux rapports utilisent la même identité visuelle afin que le portfolio soit perçu comme une série éditoriale cohérente.

### Structure commune des rapports

1. page de couverture ;
2. statut du document, date, périmètre et niveau de diffusion ;
3. résumé exécutif « En deux minutes » ;
4. cinq à huit chiffres ou constats clés ;
5. question centrale et raisons de son importance ;
6. méthodologie expliquée en français clair ;
7. preuves et résultats principaux ;
8. chronologie visuelle et/ou chaîne analytique ;
9. hypothèses concurrentes et niveaux de confiance ;
10. ce que les preuves ne permettent pas d'établir ;
11. implications et recommandations conditionnelles ;
12. reproductibilité et traçabilité des sources ;
13. glossaire ;
14. sélection de sources et navigation vers l'ensemble des sources.

### Principes visuels

- esthétique moderne de type rapport institutionnel / renseignement ;
- espace blanc généreux ;
- hiérarchie visuelle forte et navigation claire entre les pages ;
- corps de texte lisible à un niveau de zoom normal ;
- absence de fonds décoratifs denses ;
- graphiques utilisés uniquement lorsqu'ils clarifient une conclusion ;
- chaque graphique comporte un titre, une période, une unité, une source et une note de limite ;
- encadrés « À retenir », « Limite », « Niveau de confiance » et « Ce que cela ne prouve pas » ;
- la couleur ne doit jamais être le seul moyen de transmettre une information ;
- les tableaux doivent être simplifiés pour les non-spécialistes et les preuves détaillées déplacées en annexe si nécessaire ;
- références de sources cliquables lorsque cela est techniquement fiable.

### Contenu visuel du Case 01

Le rapport doit inclure, lorsque les données publiables le permettent :

- comparaison du HHI 2017 vs 2025 pour les six catégories de produits ;
- comparaison des origines dominantes ;
- vue de composition des échanges avec avertissement explicite sur le double comptage ;
- schéma maturité industrielle vs qualification aéronautique ;
- schéma des portes de qualification et de substitution ;
- matrice scénarios/options ;
- principales limites des données douanières.

### Contenu visuel du Case 02

Le rapport doit inclure, lorsque les données dérivées sont compatibles avec une diffusion publique :

- chronologie de 2013 aux phases d'expansion 2024/2025 ;
- explication visuelle de la structure du réseau plutôt qu'un graphe complet illisible ;
- tableau ou visualisation de sensibilité du graphe ;
- encadré France/UE ;
- panneau de dissémination pour les observations Wikipedia et X ;
- vue des hypothèses concurrentes / ACH ;
- distinction entre visibilité, coordination, attribution et impact ;
- question explicitement non résolue entre « LLM grooming » et « vides informationnels ».

## Accessibilité et règles pour un large public

Le récit principal est rédigé en français. Les termes anglais sont conservés uniquement lorsqu'ils sont utiles et sont définis lors de leur première apparition.

Tout terme technique qu'un lecteur généraliste peut ne pas connaître doit être expliqué dans le texte ou dans le glossaire.

Les graphiques doivent comporter des légendes textuelles résumant leur enseignement. Les tableaux doivent rester lisibles sur une page A4 sans nécessiter un zoom supérieur à des conditions normales de lecture.

Les rapports ne doivent pas dépendre de la couleur seule et doivent conserver un contraste exploitable lors d'une impression en niveaux de gris.

## Règles d'intégrité des preuves

Chaque affirmation chiffrée d'un rapport public doit être reliée à un résultat analytique existant et validé, ou à une dérivation compatible avec une diffusion publique et explicitement documentée.

Aucune nouvelle conclusion causale ne doit être ajoutée pour des raisons éditoriales.

Les rapports publics conservent des catégories distinctes :

- observé ;
- rapporté ;
- corroboré ;
- inféré ;
- hypothèse ;
- non démontré.

Le vocabulaire de confiance doit rester conforme au casebook d'origine.

## Règles de confidentialité et de sécurité opérationnelle

L'édition publique exclut :

- secrets, jetons, identifiants, chemins locaux, noms de machines ou adresses e-mail privées ;
- données personnelles inutiles ;
- identifiants bruts de comptes lorsque l'anonymisation faisait partie de la politique canonique de publication ;
- identifiants d'aéronefs privés, callsigns, hashes ICAO24 stables ou enregistrements sensibles de trajectoires ;
- journaux d'audit privés et notes de travail ;
- tout contenu pouvant être interprété à tort comme une alerte opérationnelle en direct ou un produit de navigation.

## Règles de droits et d'attribution

La publication du Case 01 suit le modèle de droits du snapshot assaini ayant déjà passé l'audit.

Le Case 02 fait l'objet d'une revue explicite des droits du package public avant publication. Les éléments amont marqués comme nécessitant une revue sont liés et décrits, mais ne sont pas copiés dans le dépôt public tant que leur permission de redistribution n'est pas établie indépendamment.

Le code original et le texte analytique original reçoivent une licence explicite. Les contenus tiers conservent leurs conditions d'origine et sont documentés dans `NOTICE.md` ainsi que dans les pages de sources propres à chaque cas.

## Transparence sur l'IA

`AI_TRANSPARENCY.md` doit préciser que l'IA générative peut contribuer à la rédaction, à la génération de code, au formatage ou à la transformation éditoriale, tandis que la sélection des sources, l'évaluation des preuves, les jugements analytiques, la validation et les décisions de publication restent soumis à une revue humaine.

Les rapports PDF publics doivent inclure une courte note de transparence et renvoyer vers ce fichier du dépôt pour davantage de détails.

## Reproductibilité

L'édition publique doit fournir suffisamment de méthodologie et d'artefacts dérivés pour permettre aux lecteurs de comprendre et, lorsque les droits le permettent, de reproduire les résultats publiés sans avoir accès au dépôt canonique privé.

Lorsque les données brutes ne peuvent pas être redistribuées, le dépôt public documente :

- la source amont ;
- la date de collecte ou de snapshot lorsque cela est pertinent ;
- la logique de transformation ;
- le schéma ou les champs attendus ;
- les sommes de contrôle des artefacts publics redistribuables ;
- la limite exacte empêchant la publication des données brutes.

## Gate de publication

Le dépôt n'est pas considéré comme prêt à être publié tant que tous les contrôles suivants ne sont pas validés :

- aucun historique privé copié ;
- manifeste public correspondant exactement aux fichiers prévus ;
- scan secrets et vie privée sans finding ;
- aucun chemin local ni identifiant de machine ;
- métadonnées PDF contrôlées ;
- liens internes valides ;
- affirmations des rapports revues par rapport aux preuves des casebooks ;
- droits du Case 01 hérités uniquement du périmètre du snapshot public validé ;
- revue des droits du Case 02 sans blocage de redistribution non résolu pour les artefacts copiés ;
- contenus tiers aux droits incertains publiés uniquement sous forme de liens ;
- revue du rendu PDF confirmant l'absence de texte rogné, chevauchement, glyphes cassés ou tableaux illisibles ;
- sommes de contrôle générées pour les PDF finaux ;
- transparence IA, notice, disclaimer et licence visibles depuis la navigation de première lecture ;
- checklist indépendante finale enregistrant un statut `PASS`.

## Critères de réussite

Un lecteur non spécialiste doit pouvoir comprendre la question centrale, les résultats principaux, les limites et le sens du niveau de confiance de chacun des cas en moins de dix minutes.

Un lecteur technique doit pouvoir relier les affirmations importantes à des références publiques et comprendre leur dérivation sans avoir besoin du dépôt privé.

Un recruteur doit pouvoir identifier les compétences démontrées en OSINT, GEOINT, data engineering, analyse structurée, reproductibilité, gestion de l'incertitude et communication orientée décision depuis le README racine et les cinq premières pages de chaque PDF.
