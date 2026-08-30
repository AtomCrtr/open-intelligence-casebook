# Carte publique affirmation-preuve - Case 02

Cette carte expose la chaîne **affirmation -> preuve -> confiance -> limite** à partir de métriques dérivées et de sources link-only. Elle ne republie ni corpus de posts, ni identifiants de comptes, ni données personnelles.

| Affirmation publique | Type de preuve | Sources / artefacts publics | Confiance | Limite déterminante |
|---|---|---|---|---|
| Le snapshot VIGINUM contient 371 observations de domaines, dont 232 datées et 139 non datées. | observation / décompte dérivé | [VIGINUM](sources.md), [métriques](data/key_metrics.csv) | élevée | `valid_from` n'est pas une preuve indépendante de première mise en ligne |
| Mars 2024 forme une vague paneuropéenne de 31 observations `pravda-*`. | observation + corroboration | VIGINUM export, VIGINUM partie 3, EDMO ; [chronologie](figures/timeline.svg) | moyenne à élevée | phases tardives 2024/2025 reposent davantage sur des publications ultérieures |
| Le paquet STIX analysé contient 609 nœuds et 1 013 relations ; la composante principale contient 604 nœuds. | observation source-modélisée | VIGINUM STIX, [métriques](data/key_metrics.csv) | élevée pour le décompte | le graphe représente aussi des choix de modélisation |
| La grande composante ne dépend pas du seul nœud campagne, mais elle est très sensible aux relations `amplifies`. | analyse de sensibilité | [figure de sensibilité](figures/graph_sensitivity.svg), rapport §6 | moyenne | sensibilité du modèle != chaîne de commandement réelle |
| La dissémination figée contient 1 932 observations Wikipedia et 2 018 observations X. | décompte dérivé + corroboration | CheckFirst, DFRLab, [métriques](data/key_metrics.csv) | élevée | présence d'un lien != audience, croyance ou effet |
| La France est ciblée mais ne domine pas la couche Wikipedia observée. | décompte dérivé | `fr=28` sur Wikipedia ; `fr=94` sur X ; 130 observations X vers domaines France-compatibles ; [figure France](figures/france_focus.svg) | élevée pour les comptes | aucune mesure d'audience française |
| H4 - modèle hybride - reste la meilleure hypothèse de travail. | ACH + triangulation | [figure ACH](figures/ach_hypotheses.svg), VIGINUM, EDMO, DFRLab, CheckFirst | faible à moyenne | ne démontre ni opérateur éditorial unique ni attribution étatique |
| Le corpus ne démontre ni impact humain, ni effet électoral, ni empoisonnement causal des LLM. | conclusion négative bornée par les données | absence de métriques d'audience/effet ; lectures concurrentes ASP/NewsGuard vs Harvard | élevée sur la lacune, faible sur les mécanismes non observés | absence de preuve != preuve d'absence |

## Règle de lecture

Le casebook interdit le glissement automatique **visibilité -> coordination -> attribution -> impact**. Chaque niveau exige une catégorie de preuve supplémentaire ; les niveaux non couverts restent explicitement non démontrés.
