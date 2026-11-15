---
title: "Comprendre le renseignement et lire les quatre études"
subtitle: "Guide de découverte — aucune connaissance technique nécessaire"
author: "Emeline Cartier — Open Intelligence Casebook"
date: "14 novembre 2026"
lang: fr-FR
reading-guide: true
---

<!-- READER_SUMMARY_START -->

# Commencer en deux minutes

**Le renseignement**, ici, est une analyse qui aide à comprendre une situation et à décider. On part d’une question, on vérifie les informations, puis on explique ce qui est établi et ce qui reste incertain.

**Les quatre cas utilisent des sources réelles.** Titane étudie des échanges commerciaux ; Portal Kombat des liens entre sites ; GNSS des documents sur la navigation aérienne ; XZ Utils une compromission logicielle. Ils montrent des compétences utiles à l’analyse, sans constituer quatre enquêtes criminelles.

**Pour commencer**, choisissez un rapport et lisez sa synthèse juste après la couverture. Essayez ensuite d’expliquer sa question, son résultat et sa principale limite avec vos mots. Les sources et les détails permettent de vérifier votre compréhension.

**Le prochain cas envisagé** porte sur JuicyFields et les escroqueries à l’investissement. Il reste à cadrer à partir de documents publics réels. Une allégation, une arrestation et une condamnation devront être distinguées.

**Pour tester la lecture**, utilisez le [questionnaire débutant](BEGINNER_READING_TEST.md). Aucun résultat de test auprès de débutants n’est encore disponible.

<!-- READER_SUMMARY_END -->


# Commencer ici

Un **casebook** est un dossier d'étude : il pose une question, rassemble des informations, compare des explications et présente une réponse avec ses limites. Ce portfolio contient quatre études finalisées dans leur périmètre. Elles servent à apprendre et à montrer une méthode d'analyse.

**Parcours conseillé :** lire ce guide, choisir un sujet dans le tableau, puis lire l'introduction du rapport. Les sources et les tableaux détaillés permettent ensuite de vérifier le raisonnement. Chaque étude existe en Markdown, lisible sur GitHub, et en PDF, téléchargeable et imprimable.

## Les cas sont-ils finis ?

| Étude | Statut de l'édition | Ce qui reste inconnu ou hors périmètre |
|---|---|---|
| Titane | Terminée et publiée | Les données douanières ne décrivent pas directement les achats et qualifications d'un constructeur. |
| Portal Kombat | Terminée et publiée | Le contrôle du réseau et son effet sur les opinions ne sont pas démontrés par l'étude. |
| GNSS | Terminée et publiée comme étude documentaire | La couche de mesures propres à partir de trajectoires et de données GPSJAM n'a pas été réalisée. |
| XZ Utils | Terminée et publiée | L'identité réelle des auteurs et une exploitation réelle restent non établies. |

**Terminé signifie : une réponse livrée pour une question et un périmètre définis.** Cela ne signifie pas que toutes les inconnues ont disparu, que le sujet est clos pour toujours ou que les résultats sont actualisés en continu. Les dates des données et des sources restent celles indiquées dans chaque rapport. L'harmonisation éditoriale du 14 novembre 2026 n'est pas une nouvelle collecte.

## Choisir une première lecture

| Pour comprendre… | Lire | PDF |
|---|---|---|
| Comment des chiffres deviennent une analyse utile | [Titane](cases/case-01-titanium/README.md) | [Rapport Titane](cases/case-01-titanium/report.pdf) |
| Comment étudier un réseau et vérifier ses liens | [Portal Kombat](cases/case-02-portal-kombat/README.md) | [Rapport Portal Kombat](cases/case-02-portal-kombat/report.pdf) |
| Comment raisonner quand les mesures sont incomplètes | [GNSS](cases/case-03-gnss-interference/README.md) | [Rapport GNSS](cases/case-03-gnss-interference/report.pdf) |
| Comment reconstituer une séquence à partir de sources publiques | [XZ Utils](cases/case-04-xz-utils/README.md) | [Rapport XZ Utils](cases/case-04-xz-utils/report.pdf) |

# Qu'est-ce que le renseignement ?

Dans ce guide, le **renseignement** désigne le résultat d'un travail d'analyse qui aide une personne à comprendre une situation et à décider. On part d'une question ; on évalue les informations disponibles ; on explique ce qu'elles permettent de conclure et ce qu'il faudrait encore vérifier.

Une donnée isolée peut être exacte sans répondre à la question. L'analyse lui donne un contexte, teste des explications et indique ses limites.

## Un exemple tiré de Portal Kombat

L’export étudié contient 371 observations correspondant à 370 domaines distincts. Cela décrit le fichier examiné. Ce comptage ne donne ni le nombre de lecteurs, ni leur opinion, ni l’identité du responsable du réseau. L’analyse consiste précisément à séparer ces questions et à rechercher les preuves adaptées à chacune.

| Étape | Question simple |
|---|---|
| Besoin | Quelle décision faut-il éclairer ? |
| Collecte | Quelles informations peut-on obtenir dans le périmètre autorisé ? |
| Vérification | D'où viennent-elles et sont-elles fiables pour cette question ? |
| Analyse | Quelles explications résistent aux éléments disponibles ? |
| Restitution | Que sait-on, avec quelle confiance, et que vérifier ensuite ? |
| Réévaluation | Quelle information ferait changer la conclusion ? |

## OSINT, Data et renseignement criminel

**OSINT** signifie « renseignement en sources ouvertes » : il utilise des informations publiquement accessibles. La qualité vient de leur vérification et de leur analyse. Une donnée inventée pour un exercice reste une donnée synthétique, même si elle ressemble à une page web publique.

**La Data** apporte des moyens de structurer, nettoyer et rapprocher les données. Python et SQL peuvent aider à reconstruire une chronologie ou à tester des liens. Un graphique ou un score ne suffit pas à expliquer une situation.

**Le renseignement criminel** applique l'analyse à des phénomènes et activités criminels : modes opératoires, réseaux, évolutions et priorités de vérification. Il peut éclairer des choix à long terme, l'organisation d'une réponse ou un dossier précis. Le niveau stratégique et l'appui à une enquête sont donc des usages possibles ; ils ne se résument pas à une opposition entre deux métiers.

**L'analyse criminelle judiciaire**, dont les fonctions ANACRIM évoquées dans le projet professionnel, s'exerce dans un cadre et avec des formations propres. Ce portfolio est un travail personnel d'apprentissage. Il ne confère ni qualification ANACRIM ni statut de preuve judiciaire à ses résultats.

# Lire une conclusion avec ses limites

## Les mots employés dans les rapports

| Mot | Sens dans ce portfolio |
|---|---|
| Source | Document, organisme ou jeu de données d'où vient l'information. |
| Fait observé | Élément directement présent dans les données examinées. |
| Fait rapporté | Élément décrit par une source ; le projet ne l'a pas observé directement. |
| Hypothèse | Explication possible à confronter aux éléments disponibles. |
| Jugement analytique | Conclusion argumentée, accompagnée de son périmètre et de sa confiance. |
| Confiance | Solidité de l'appui disponible pour un jugement ; ce n'est pas un pourcentage de probabilité. |
| Attribution | Identification d'un responsable ; elle exige des éléments adaptés à cette question. |
| Provenance | Chemin permettant de retrouver l'origine d'une information et ses transformations. |
| Lignée informationnelle | Origine commune de plusieurs publications : dix reprises d'un même rapport restent dépendantes de ce rapport. |
| Graphe | Représentation d'objets et de relations ; chaque lien doit avoir une justification. |

Les termes « élevée », « modérée » et « faible » expriment la confiance. Certains tableaux historiques conservent des libellés anglais (HIGH, MEDIUM, LOW) ou des appréciations intermédiaires : leur formulation d'origine est conservée. Une confiance élevée ne supprime pas les limites de périmètre.

## Trois précautions de lecture

- Une relation technique commune peut venir d'un prestataire partagé ; elle n'établit pas automatiquement un contrôle commun.
- Une information absente peut être simplement indisponible ; elle ne prouve pas que l'événement n'a pas eu lieu.
- Une étude finalisée peut conserver des hypothèses non départagées et des questions ouvertes.

## Retrouver les preuves

Dans chaque dossier, le **rapport** explique le raisonnement. La **carte des preuves** (`evidence-map.md`) relie les affirmations aux éléments utilisés. Les **sources** (`sources.md`) permettent de retrouver les publications. La **table de provenance** (`provenance.csv`) décrit leur origine et leurs dépendances. Pour XZ Utils, le registre et les extraits de citations complètent ce parcours.

Les sources tierces conservent leurs droits. Certaines sont seulement liées et ne sont pas reproduites dans le portfolio. L'[usage de l'IA](AI_TRANSPARENCY.md) est déclaré ; une réponse d'IA ne constitue pas une source.

# Prochain sujet proposé : JuicyFields

**Statut : candidat à cadrer, étude non commencée.** Ce projet porterait sur une affaire réelle d’escroquerie présumée à l’investissement dans le cannabis. Il répondrait à la question : **que permettent d’établir les documents publics sur le dispositif décrit par les autorités, sa chronologie et la coopération judiciaire ?**

Les points de départ sont les publications d’[Eurojust](https://www.eurojust.europa.eu/news/eurojust-helps-tackle-massive-fraud-eur-645-million-medicinal-cannabis-plants-across-europe), de la [National Crime Agency](https://www.nationalcrimeagency.gov.uk/news/uk-arrest-in-645-million-international-investment-scam) et de la [police de Berlin](https://www.berlin.de/polizei/polizeimeldungen/2024/pressemitteilung.1436559.php). Ces communiqués décrivent les positions des autorités à leurs dates de publication ; ils ne remplacent pas les décisions judiciaires.

La première étape sera de vérifier l’accès aux décisions et aux documents publics nécessaires. Les liens du réseau devront chacun renvoyer à une pièce. Aucun paiement, acteur ou lien manquant ne sera inventé. Si les sources ne permettent pas de reconstituer des transactions, le dossier le dira et restera documentaire.

Les livrables envisagés sont une chronologie sourcée, un graphe de relations documentées, une comparaison des explications possibles et une note courte distinguant faits, allégations et inconnues. Ce cadrage ne constitue ni une enquête en cours ni une conclusion sur la culpabilité de personnes.
