# Carte publique affirmation-preuve - Case 04

Cette carte expose la chaîne **affirmation → preuve → confiance → limite** du rapport. Chaque ligne correspond à un `claim_id` de la [table de provenance](provenance.csv), qui précise la lignée informationnelle de chaque source. Les références [n] renvoient à [`sources.md`](sources.md) et au [ledger de citations](citations-ledger.json).

| ID | Affirmation publique | Type de preuve | Sources | Confiance | Limite déterminante |
|---|---|---|---|---|---|
| C4-PUB-001 | Les versions XZ Utils 5.6.0 et 5.6.1 sont les versions compromises centrales du cas. | advisories convergents + déclaration du projet | [1] [3] [5] | HIGH | la déclaration du projet a un intérêt direct dans la communication de crise |
| C4-PUB-002 | Le mécanisme passe par la chaîne de publication / build et produit, dans certaines conditions, une liblzma compromise. | analyse technique primaire + synthèses | [2] [4] [10] | HIGH pour le mécanisme général | les détails d'exécution dépendent d'analyses techniques évolutives |
| C4-PUB-003 | La découverte publique repose sur des symptômes observés autour de liblzma sur Debian Sid (CPU, Valgrind). | rapport technique primaire | [2] | HIGH pour le contenu du rapport | source unique pour l'expérience directe du découvreur |
| C4-PUB-004 | L'incident n'équivaut pas à une compromission universelle de Linux : Debian stable et RHEL n'étaient pas connus comme affectés. | advisories de distribution | [5] [11] | HIGH pour Debian / Red Hat | non extrapolable à toutes les distributions |
| C4-PUB-005 | La capacité est une exécution de commande pré-authentification via SSH, réservée au détenteur d'une clé Ed448 de l'attaquant ; aucune exploitation réelle n'est démontrée. | analyses techniques + analyse du binaire + advisory + média | [2] [7] [10] [12] [15] | HIGH pour la condition de clé ; LOW pour toute exploitation | capacité ≠ exploitation observée ; l'exploitation ne laisse pas de journal INFO |
| C4-PUB-006 | Aucune attribution à une personne réelle, un groupe ou un État n'est établie ; la motivation reste inconnue. | synthèse experte + média | [4] [12] | LOW pour toute attribution spécifique | absence de données non publiques ; pas d'identification recherchée |
| C4-PUB-007 | Le 28 mars correspond à la découverte et à la notification privée, le 29 mars à la divulgation publique. | comparaison de sources + compilation chronologique | [6] [7] [2] [13] [17] | MEDIUM-HIGH pour la réconciliation | la liste distros n'est pas publique ; première observation des symptômes non datée |
| C4-PUB-008 | Les tags v5.6.0 (24 févr. 2024, 08:22:06 UTC) et v5.6.1 (9 mars 2024, 08:16:00 UTC) sont créés par le compte co-mainteneur ; l'affichage GitHub donne l'heure UTC. | métadonnées de dépôt + compilation | [8] [9] [20] [13] | HIGH pour les métadonnées | date déclarée par l'auteur du tag ; même dépôt que les pages GitHub ; ne prouve pas l'intention |
| C4-PUB-009 | La compromission s'inscrit dans plus de deux ans de contributions publiques : premier correctif le 2021-10-29, accès en écriture le 2022-12-30, première release (v5.4.2) le 2023-03-18, fichiers de test piégés le 2024-02-23. | compilation chronologique + archive de liste + métadonnées Git | [13] [21] [20] | HIGH pour les jalons datés | dates de commit et de tag déclarées par leur auteur ; messages de pression de 2022 non revérifiés |
| C4-PUB-013 | Ubuntu n'a eu la version 5.6.0 que dans `noble-proposed` (26 févr. – 29 mars 2024) ; aucune version publiée d'Ubuntu n'est affectée ; `5.6.1+really5.4.5` contient du code 5.4.5. | déclaration de la distribution + registre d'archive | [18] [19] | HIGH pour les versions publiées | même lignée Ubuntu ; exposition des machines ayant activé `noble-proposed` non documentée |
| C4-PUB-010 | Le déclencheur M4 n'existe que dans les tarballs ; la charge de second niveau est dans des fichiers de test du dépôt Git. | advisory + notice officielle + compilation | [11] [14] [13] | HIGH (résolution documentaire de C-003) | pas de comparaison octet par octet des artefacts |
| C4-PUB-011 | Arch Linux n'a pas compilé le code malveillant et ne lie pas sshd à liblzma ; openSUSE Tumbleweed et MicroOS ont été exposés du 7 au 28 mars, pas SUSE Linux Enterprise ni Leap. | annonces de distribution | [16] [17] | HIGH pour chaque périmètre | Ubuntu non vérifié ; non extrapolable aux autres distributions |
| C4-PUB-012 | La notice officielle attribue un score CVSS 3.1 de 10.0 (CRITICAL). | notice de vulnérabilité | [14] | HIGH | gravité potentielle, pas exploitation observée |

## Règle de lecture

Le cas interdit le glissement **version compromise → exploitation → attribution**. Chaque niveau exige une catégorie de preuve supplémentaire ; les niveaux non couverts restent explicitement non démontrés.

Aucune tentative n'a été faite pour identifier la ou les personnes derrière les pseudonymes cités par les sources.
