# Revue des droits - édition publique v1

**Date :** 30 août 2026  
**Périmètre :** `open-intelligence-casebook` - première édition publique  
**Principe :** une ressource accessible publiquement n'est pas considérée comme librement redistribuable par défaut.

## Décision générale

L'édition publique publie uniquement :

- du texte analytique original ;
- des figures et schémas originaux générés pour cette édition ;
- des métriques dérivées minimales nécessaires à la compréhension des résultats ;
- des liens vers les sources tierces ;
- des documents de méthodologie et de gouvernance originaux.

Aucun corpus tiers brut dont les droits sont absents, ambigus ou dépendants d'une plateforme amont n'est copié.

## Case 01 - Titane

| Élément public | Origine | Traitement | Décision |
|---|---|---|---|
| `report.md`, `report.pdf` | rédaction analytique originale dérivée de résultats déjà audités | CC BY 4.0 pour le contenu original | **autorisé** |
| figures SVG | visualisations originales à partir de métriques déjà validées | CC BY 4.0 pour les figures originales | **autorisé** |
| `data/key_metrics.csv` | métriques dérivées de la lecture Eurostat/Comext déjà validée | Eurostat autorise la réutilisation avec attribution | **autorisé** |
| documents Eurostat, USGS, UE, BEI, SEC et acteurs industriels | sources tierces | liens et références uniquement ; aucun document complet recopié | **link-only** |
| UN Comtrade | source complémentaire du casebook canonique | aucune donnée brute publiée ici | **exclu de la redistribution** |

Le périmètre public du Case 01 reste borné aux résultats du snapshot assaini ayant déjà obtenu `RELEASE READINESS: PASS` dans le dépôt canonique.

## Case 02 - Portal Kombat / Pravda

| Élément public | Origine | Traitement | Décision |
|---|---|---|---|
| `report.md`, `report.pdf` | rédaction analytique originale à partir de résultats Lot 3 validés | CC BY 4.0 pour le contenu original | **autorisé** |
| figures SVG | visualisations originales de métriques dérivées | CC BY 4.0 pour les figures originales | **autorisé** |
| `data/key_metrics.csv` | décomptes dérivés du snapshot canonique | aucune ligne brute de corpus amont | **derived-only** |
| rapports VIGINUM/SGDSN, EDMO, EEAS, DFRLab, ASP, NewsGuard, publication académique | publications tierces | liens uniquement ; aucune copie intégrale | **link-only** |
| fichiers techniques VIGINUM / CheckFirst | dépôts publics aux conditions variables | aucun corpus brut copié ; seuls liens et métriques dérivées | **review-required -> non redistribué** |
| Wikipedia / X | données soumises aux termes des plateformes et des projets amont | aucun texte de post, handle ou identifiant personnel ; métriques agrégées seulement | **derived-only** |

La présence d'une licence MPL-2.0 sur le dépôt de dissémination CheckFirst n'est pas interprétée comme une dérogation aux droits ou conditions des contenus Wikipedia/X représentés dans ces données.

## Case 03 - GNSS

**Revue du 1er novembre 2026.** Conditions des éditeurs consultées à cette date ; lecture prudente, pas un avis juridique.

| Élément public | Origine | Traitement | Décision |
|---|---|---|---|
| `report.md`, `report.pdf`, `key-judgments.md` | rédaction analytique originale | CC BY 4.0 pour le contenu original | **autorisé** |
| `figures/case03_confidence.svg` | figure originale, sans donnée tierce | CC BY 4.0 | **autorisé** |
| `sources.md`, `evidence-map.md`, `provenance.csv` | références : liens, emplacements, empreintes, lignées | aucun texte d'extrait | **link-only** |
| EASA (bulletin SIB 2022-02R4, page GNSS) | « Reproduction is authorised, provided the source is acknowledged » | courtes citations attribuées ; aucune copie de document | **link-only + citation courte** |
| OACI (A42-WP/34, A42-WP/553) | usage personnel non commercial ; reproduction soumise à accord écrit | paraphrase attribuée | **link-only** |
| IATA (évaluation de risque v5, communiqué EASA–IATA) | usage personnel non commercial ; aucune reproduction sur un autre site sans accord écrit | paraphrase attribuée ; chiffres reformulés | **link-only** |
| Atelier EASA–EUROCONTROL de juillet 2026 | présentations propriété de chaque intervenant ; pas de licence globale | aucune diapositive ni graphique reproduit ; paraphrase attribuée | **link-only** |
| UIT (procès-verbal CR/518) | usage personnel, éducatif ou non commercial ; reproduction et distribution soumises à permission | paraphrase attribuée | **link-only** |
| GPSJAM, ADS-B, trajectoires | couche d'observation non exécutée | rien publié | **exclu** |

Les registres de travail et les extraits verbatim restent dans le dépôt canonique privé.

**Décision : autorisé pour le rapport, les jugements, la figure et les références ; aucun document tiers redistribué.**

## Case 04 - XZ Utils

**Revue du 1er novembre 2026**, lecture prudente des pratiques du cas, pas un avis juridique.

| Élément public | Origine | Traitement | Décision |
|---|---|---|---|
| `report.md`, `README.md`, `evidence-map.md`, `evidence-register.md`, `provenance.csv`, `sources.md` | rédaction analytique originale | CC BY 4.0 pour le contenu original | **autorisé** |
| `source-extracts.md`, `citations-ledger.json` | courts extraits verbatim de 21 sources publiques (advisories, annonces de distribution, registres de paquets et de dépôt, archive de liste, analyses) | citations courtes et attribuées, à des fins d'analyse et de vérification ; aucune copie intégrale de document | **link-only + citation courte** |
| pages de release GitHub (S-008, S-009) | métadonnées de dépôt | image d'avatar et lien de profil retirés ; seul le pseudonyme affiché est conservé | **assaini** |
| métadonnées Git (S-020) et archive xz-devel (S-021) | registres publics | identifiants de commit, dates et sujets ; aucune adresse électronique reproduite ; dépôt lu sans contenu de fichier | **link-only + citation courte** |
| registre Launchpad (S-019) | réponse d'API publique | champs de version et de date ; aucun nom d'utilisateur reproduit ; réponse non redistribuée | **link-only + citation courte** |

Aucune tentative d'identification des personnes derrière les pseudonymes ; aucun fichier du projet XZ, piégé ou non, n'est redistribué.

**Décision : autorisé pour le texte original et les courts extraits attribués ; aucun document tiers redistribué.**

## Licences de l'édition

- code original : Apache License 2.0 ;
- texte analytique, diagrammes et figures originaux : Creative Commons Attribution 4.0 International ;
- contenu tiers : conditions d'origine conservées, aucune relicence implicite.

## Conclusion

**RIGHTS REVIEW: PASS**

Aucun artefact tiers copié dans l'édition publique ne conserve un statut de redistribution non résolu. Les sources dont les droits sont incertains restent sous forme de liens et de références.
