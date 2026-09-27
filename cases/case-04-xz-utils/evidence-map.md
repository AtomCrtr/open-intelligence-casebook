# Carte publique affirmation-preuve - Case 04

Cette carte expose la chaîne **affirmation → preuve → confiance → limite** du rapport. Chaque ligne correspond à un `claim_id` de la [table de provenance](provenance.csv), qui précise la lignée informationnelle de chaque source. Les références [n] renvoient à [`sources.md`](sources.md) et au [ledger de citations](citations-ledger.json).

| ID | Affirmation publique | Type de preuve | Sources | Confiance | Limite déterminante |
|---|---|---|---|---|---|
| C4-PUB-001 | Les versions XZ Utils 5.6.0 et 5.6.1 sont les versions compromises centrales du cas. | advisories convergents + déclaration du projet | [1] [3] [5] | HIGH | la déclaration du projet a un intérêt direct dans la communication de crise |
| C4-PUB-002 | Le mécanisme passe par la chaîne de publication / build et produit, dans certaines conditions, une liblzma compromise. | analyse technique primaire + synthèses | [2] [4] [10] | HIGH pour le mécanisme général | les détails d'exécution dépendent d'analyses techniques évolutives |
| C4-PUB-003 | La découverte publique repose sur des symptômes observés autour de liblzma sur Debian Sid (CPU, Valgrind). | rapport technique primaire | [2] | HIGH pour le contenu du rapport | source unique pour l'expérience directe du découvreur |
| C4-PUB-004 | L'incident n'équivaut pas à une compromission universelle de Linux : Debian stable et RHEL n'étaient pas connus comme affectés. | advisories de distribution | [5] [11] | HIGH pour Debian / Red Hat | non extrapolable à toutes les distributions |
| C4-PUB-005 | Une capacité d'interférence pré-authentification avec SSH est décrite sous conditions ; une exploitation à grande échelle n'est pas démontrée. | analyses techniques + advisory + média | [2] [7] [10] [12] | MEDIUM-HIGH | capacité ≠ exploitation observée |
| C4-PUB-006 | Aucune attribution à une personne réelle, un groupe ou un État n'est établie ; la motivation reste inconnue. | synthèse experte + média | [4] [12] | LOW pour toute attribution spécifique | absence de données non publiques ; pas d'identification recherchée |
| C4-PUB-007 | La date de « découverte » varie entre le 28 mars (Microsoft, Datadog) et le 29 mars (rapport public horodaté). | comparaison de sources | [6] [7] [2] | HIGH pour l'existence des formulations ; MEDIUM pour leur réconciliation | jalons différents (observation, analyse, publication) non départagés |
| C4-PUB-008 | Les pages de release affichent les tags v5.6.0 (24 févr.) et v5.6.1 (9 mars) sous le compte co-mainteneur. | métadonnées de dépôt | [8] [9] | HIGH pour l'affichage ; MEDIUM pour toute conversion temporelle | fuseau horaire absent ; ne prouve pas l'intention |

## Règle de lecture

Le cas interdit le glissement **version compromise → exploitation → attribution**. Chaque niveau exige une catégorie de preuve supplémentaire ; les niveaux non couverts restent explicitement non démontrés.

Aucune tentative n'a été faite pour identifier la ou les personnes derrière les pseudonymes cités par les sources.
