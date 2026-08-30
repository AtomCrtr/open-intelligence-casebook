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

Le Case 03 ne publie qu'une page de présentation originale. Aucune donnée GPSJAM, aucune fixture, aucune trajectoire, aucun identifiant d'aéronef et aucune sortie événementielle ne sont redistribués.

**Décision : autorisé pour le teaser original ; données de travail exclues.**

## Licences de l'édition

- code original : Apache License 2.0 ;
- texte analytique, diagrammes et figures originaux : Creative Commons Attribution 4.0 International ;
- contenu tiers : conditions d'origine conservées, aucune relicence implicite.

## Conclusion

**RIGHTS REVIEW: PASS**

Aucun artefact tiers copié dans l'édition publique ne conserve un statut de redistribution non résolu. Les sources dont les droits sont incertains restent sous forme de liens et de références.
