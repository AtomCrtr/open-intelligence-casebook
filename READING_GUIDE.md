---
title: "Comprendre le renseignement et lire les quatre études"
subtitle: "Guide de découverte — aucune connaissance technique nécessaire"
author: "Emeline Cartier — Open Intelligence Casebook"
date: "13 novembre 2026"
lang: fr-FR
reading-guide: true
---

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

**Terminé signifie : une réponse livrée pour une question et un périmètre définis.** Cela ne signifie pas que toutes les inconnues ont disparu, que le sujet est clos pour toujours ou que les résultats sont actualisés en continu. Les dates des données et des sources restent celles indiquées dans chaque rapport. L'harmonisation éditoriale du 13 novembre 2026 n'est pas une nouvelle collecte.

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

## Un exemple entièrement fictif

Trois sites de placement partagent la même adresse de contact technique. C'est une **information de départ**, à vérifier sur les pièces de l'exercice. Elle peut indiquer un prestataire commun. Elle peut aussi soutenir une hypothèse d'organisation commune. À elle seule, elle ne permet pas de qualifier une infraction ni d'identifier un responsable.

L'analyste cherche alors des éléments qui départagent les explications : mêmes bénéficiaires déclarés ? chronologie compatible ? données de paiement simulées cohérentes ? informations contradictoires ? Une note utile précise les liens établis, les liens incertains et la prochaine vérification prioritaire.

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

# Prochain sujet proposé : comprendre un réseau de fraude

**Case 05 — Escroqueries aux faux investissements : analyser un réseau fictif et prioriser les vérifications.**

**Statut : proposition, non commencée.** L'objectif serait d'apprendre comment un analyste transforme des indices dispersés en questions et en priorités utiles. Aucune conclusion sur une affaire réelle n'est annoncée.

La question centrale serait : **quels liens entre sites, sociétés fictives, contacts et paiements simulés soutiennent l'hypothèse d'une organisation commune, et quelles vérifications permettraient de départager les autres explications ?**

Le cas séparerait deux types de matériaux : des publications officielles ouvertes pour comprendre le phénomène, et un dossier entièrement synthétique pour s'exercer. Les comptes, sociétés, personnes, déclarations et transactions de l'exercice seraient inventés et clairement étiquetés.

Les livrables proposés sont une chronologie, un graphe justifié lien par lien, une comparaison d'hypothèses, des traitements Python/SQL reproductibles et une note de deux pages. Cette note expliquerait ce qui est établi dans l'exercice, ce qui reste incertain et quelles vérifications seraient prioritaires dans le cadre décrit.

**Le résultat attendu est un raisonnement vérifiable et utile à une décision.** La taille du réseau ou le nombre de graphiques ne suffisent pas à démontrer la qualité de l'analyse.
