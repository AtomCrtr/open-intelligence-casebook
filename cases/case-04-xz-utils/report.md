# Case 04 - XZ Utils / CVE-2024-3094 : rapport public

> **Édition publique.** Ce rapport reprend le dossier OSINT d'origine. Seules modifications : retrait d'une section interne d'évaluation de l'espace de travail, retrait des URL d'avatar dans les extraits S-008/S-009, et libellé générique des outils de collecte. Aucun fait, jugement ou niveau de confiance n'est modifié.


> **Case ID :** `OSINT-XZ-UTILS-2026-001`
> **Nature :** investigation OSINT publique, passive et non intrusive.
> **Collecte :** consultation de pages publiques uniquement ; aucune connexion à une cible, aucun scan, aucun compte, aucun credential et aucune donnée personnelle inutile.
> **Date de collecte :** `2026-08-21T15:51:32+02:00` — UTC normalisé : `2026-08-21T13:51:32Z`.
> **Artifacts :** `source-extracts.md` et `citations-ledger.json` dans le même dossier.

---

## Révision du 2026-10-30

Réétude du dossier à partir de cinq sources complémentaires ([13] à [17]) et de trois citations ajoutées à [11]. Les faits F-001 à F-012 sont conservés ; aucun niveau de confiance n'est relevé sans source nouvelle. Principaux apports :

- **Chronologie longue (2021–2024)** : la compromission ne commence pas en février 2024 ; une compilation sourcée décrit plus de deux ans de contributions puis l'accès en écriture et la maintenance de releases (F-013, F-014).[13]
- **C-001 réconciliée** : le 28 mars correspond à la découverte et à la notification privée, le 29 mars à la divulgation publique (F-015).[13][2][17]
- **C-003 résolue au niveau documentaire** : le déclencheur M4 n'existe que dans les tarballs, la charge de second niveau est dans des fichiers de test du dépôt Git (F-016).[11][13][14]
- **Capacité technique requalifiée** : l'accès est conditionné à une signature Ed448 détenue par l'attaquant ; c'est une exécution de commande pré-authentification réservée au détenteur de la clé, pas un contournement d'authentification utilisable par n'importe qui (F-017).[15]
- **Matrice d'exposition par distribution** : Arch Linux, openSUSE / SUSE ajoutés à Debian et Red Hat ; distinction entre version présente, code malveillant effectivement compilé et sshd réellement lié à liblzma (F-018, F-019).[16][17]
- **Sévérité officielle** : CVSS 3.1 de 10.0 (CRITICAL), attribué par la NVD et par le CNA Red Hat (F-020).[14]

---

## 1. Objectif et périmètre

**Question analytique :** que permettent d’établir les sources publiques sur la chronologie de la compromission de XZ Utils, sa découverte, sa portée technique et la réponse de l’écosystème, sans dépasser les preuves disponibles concernant l’intention, l’identité ou l’attribution ?

**Périmètre inclus :**

- XZ Utils / liblzma et les versions 5.6.0 et 5.6.1 ;
- découverte publique, mécanisme décrit par les sources et réponse des distributions ;
- sources officielles, techniques et secondaires publiquement accessibles ;
- période historique 2024, avec vérification de l’état des pages consultées le 21 août 2026.

**Périmètre exclu :**

- attribution à un État, groupe ou personne réelle ;
- identification ou investigation de personnes privées derrière des pseudonymes ;
- exploitation, reproduction du backdoor, scan ou test d’une infrastructure ;
- recherche de compromission sur des systèmes réels ;
- collecte de données personnelles non nécessaires.

**Réponse satisfaisante :** produire une chronologie sourcée, distinguer les faits techniques des analyses, comparer la portée annoncée aux périmètres réellement documentés, expliciter les contradictions et qualifier séparément la fiabilité des sources et la confiance analytique.

---

## 2. Méthode de collecte

- Recherche web et extraction de pages publiques, en lecture seule.
- Sources enregistrées au moment de la collecte dans [`citations-ledger.json`](citations-ledger.json).
- Extraits verbatim conservés dans [`source-extracts.md`](source-extracts.md).
- Hash SHA-256 de `source-extracts.md` dans le dossier de travail d'origine : `c06370b5f0d48905a2504ccd44f429d02f59780d9beee491a2c386e04ead45fb`. La copie publique diffère uniquement par l'assainissement décrit en tête de ce rapport.
- Les sources ont été classées comme officielles, techniques primaires, secondaires ou synthèses d’organisations de sécurité.
- Les dépendances entre sources ont été conservées : notamment OpenSSF, Microsoft, Datadog et Ars Technica citent ou reprennent des éléments issus de l’alerte initiale et d’analyses techniques publiques.
- **Collecte complémentaire du 2026-10-30** : cinq pages publiques supplémentaires ([13] à [17]) et la page Red Hat [11] relue, par extraction de pages en lecture seule ; extraits ajoutés à [`source-extracts.md`](source-extracts.md) et au ledger. La page Ubuntu `ubuntu.com/security/CVE-2024-3094` a répondu HTTP 503 et n'est pas utilisée. Le dépôt xzbot [15] est lu comme documentation : aucun code n'est exécuté, aucune clé ni commande n'est reproduite.

---

## EXECUTIVE SUMMARY

Les sources publiques convergent fortement sur l’existence d’une compromission de la chaîne de publication de XZ Utils affectant les versions 5.6.0 et 5.6.1. CISA, Debian et le projet XZ identifient ces versions comme compromises ou à risque, tandis que Debian documente un périmètre principalement situé dans les branches testing, unstable et experimental, et indique qu’aucune version stable Debian n’était alors connue comme affectée.[1][3][5]

La découverte publique est associée à l’observation d’anomalies de performance et de validation sur Debian Sid, décrite dans le message technique d’Andres Freund publié le 29 mars 2024 à 08:51:26 UTC−07:00. Les sources secondaires parlent parfois d’une découverte le 28 mars ; cette différence doit être conservée comme une différence entre observation, analyse et divulgation, et non lissée en une date unique.[2][6][7]

Les éléments disponibles soutiennent avec une confiance élevée l’existence d’un code malveillant introduit dans le processus de publication/build et une capacité de compromission d’OpenSSH dans certaines conditions. Ils ne permettent pas d’établir avec le même niveau de confiance l’identité réelle de l’auteur, le nombre d’acteurs, la motivation exacte ou une attribution étatique. OpenSSF indique explicitement que la motivation reste inconnue, et Ars Technica rappelle que l’existence d’une personne réelle derrière le pseudonyme Jia Tan n’est pas établie.[4][12]

---

## KEY FINDINGS

1. **Versions concernées :** les versions XZ Utils 5.6.0 et 5.6.1 sont identifiées par CISA et le projet XZ comme contenant ou associées au backdoor ; Debian documente des paquets compromis dans ses branches non stables.[1][3][5] **Confiance : HIGH** — plusieurs sources officielles et techniques convergentes.
2. **Chaîne de publication :** les sources techniques décrivent un mécanisme où des éléments du code malveillant sont présents dans les tarballs de release et où le build de paquets DEB/RPM dans certaines conditions produit une bibliothèque liblzma compromise.[2][4][10] **Confiance : HIGH** pour le mécanisme général ; les détails d’exécution restent dépendants des analyses techniques.
3. **Découverte :** Andres Freund rapporte des symptômes inhabituels autour de liblzma sur Debian Sid et publie son analyse sur oss-security le 29 mars ; une compilation sourcée situe la découverte et la notification privée à Debian et à la liste distros le 28 mars.[2][13] **Confiance : HIGH** pour le contenu de son propre rapport ; **MEDIUM-HIGH** pour la séquence 28 mars (notification privée) → 29 mars (divulgation publique), qui repose sur une compilation secondaire, la liste distros n'étant pas publique.
4. **Portée réelle :** les sources ne justifient pas l’affirmation simplifiée selon laquelle toutes les distributions Linux ou toutes les installations de production étaient compromises. Debian indique que les versions stables n’étaient pas connues comme affectées, Red Hat que RHEL n’était pas affecté ; Arch Linux indique que le code n’a pas été injecté dans ses binaires et que sshd n’y est pas lié à liblzma ; openSUSE situe l’exposition dans Tumbleweed et MicroOS (7–28 mars) et l’exclut pour SUSE Linux Enterprise et Leap.[5][11][16][17] **Confiance : HIGH** pour chacun de ces périmètres ; l’exposition dépend de trois conditions cumulées — version présente, code effectivement compilé (paquets DEB/RPM x86-64), sshd lié à liblzma via libsystemd — et ne s’extrapole pas aux distributions non documentées.
5. **Capacité technique :** les analyses décrivent une interférence avec le processus d’authentification SSH permettant une exécution de commande pré-authentification ; l’analyse du binaire montre que la charge doit être chiffrée et signée avec une clé Ed448 de l’attaquant, ce qui réserve la capacité au détenteur de cette clé.[2][7][10][12][15] **Confiance : HIGH** pour la capacité réservée au détenteur de la clé (mécanisme décrit et reproduit en laboratoire avec une clé substituée) ; **LOW** pour toute exploitation réelle, qui n’est pas démontrée. Une exploitation réussie ne produisant pas d’entrée de journal de niveau INFO ou supérieur, l’absence de traces n’établit pas l’absence d’exploitation.[15]
6. **Attribution :** les sources soutiennent une insertion malveillante et une préparation structurée, mais ne permettent pas d’identifier un acteur réel ou un État avec une confiance suffisante.[4][12] **Confiance : LOW** pour toute attribution spécifique.
7. **Préparation longue :** l’opération s’inscrit dans plus de deux ans de contributions publiques (premier correctif en octobre 2021, accès en écriture établi fin 2022, première release produite par le même compte en mars 2023), accompagnées de messages de pression envoyés par des comptes qui n’apparaissent nulle part ailleurs selon les observations rapportées.[13] **Confiance : MEDIUM-HIGH** — chronologie secondaire dont chaque date renvoie à une archive publique (liste xz-devel, dépôt git), sans revérification ligne à ligne dans ce dossier.

---

## MITRE ATT&CK

Aucun mapping MITRE ATT&CK n’est retenu dans ce dossier. Les sources publiques décrivent un incident de chaîne d’approvisionnement et un mécanisme technique, mais ce cas ne dispose pas de télémétrie adversaire ou de séquence d’actions observées permettant de justifier un mapping précis sans surinterprétation.

---

## FACTS

| ID | Fait | Provenance | Confiance |
|----|------|------------|-----------|
| F-001 | CISA rapporte du code malveillant intégré dans XZ Utils 5.6.0 et 5.6.1 et associe l’activité à CVE-2024-3094. | S-001 / [1] | HIGH — alerte gouvernementale directement consultée. |
| F-002 | Le projet XZ indique que les tarballs de release 5.6.0 et 5.6.1 contiennent un backdoor. | S-003 / [3] | HIGH — déclaration officielle du projet, avec biais possible sur la gestion de crise. |
| F-003 | Le message d’Andres Freund décrit des symptômes inhabituels autour de liblzma sur Debian Sid, dont une consommation CPU élevée lors de connexions SSH et des erreurs Valgrind. | S-002 / [2] | HIGH — rapport technique primaire pour les observations de l’auteur. |
| F-004 | La page GitHub de release affiche un tag v5.6.0 par JiaT75 le `24 Feb 08:22` et un tag v5.6.1 par JiaT75 le `09 Mar 08:16`; le fuseau horaire n’est pas fourni par l’extrait. | S-008, S-009 / [8][9] | HIGH pour les métadonnées affichées ; MEDIUM pour toute conversion temporelle ou interprétation de rôle. |
| F-005 | Debian indique que les paquets compromis concernaient testing, unstable et experimental, tandis qu’aucune version stable Debian n’était alors connue comme affectée. | S-005 / [5] | HIGH — advisory Debian signé et spécifique à son périmètre. |
| F-006 | Red Hat indique que RHEL n’est pas affecté dans son advisory et distingue le statut de Fedora 40 beta et Fedora Rawhide. | S-011 / [11] | HIGH pour la position Red Hat ; périmètre limité aux produits Red Hat décrits. |
| F-007 | OpenSSF indique que la motivation reste inconnue, tout en décrivant une intention de compromettre certaines distributions et certaines conditions de build. | S-004 / [4] | MEDIUM-HIGH — synthèse experte, dépendante en partie de sources techniques antérieures. |
| F-008 | Microsoft situe l’identification du backdoor au 28 mars 2024 ; Datadog situe également la découverte au 28 mars, tandis que le rapport public d’Andres Freund est horodaté le 29 mars. | S-006, S-007, S-002 / [6][7][2] | HIGH pour l’existence de ces formulations ; MEDIUM pour leur réconciliation chronologique. |
| F-009 | CERT-EU décrit une capacité pré-authentification dans certaines conditions et identifie plusieurs distributions de test ou de développement comme concernées, tout en signalant que sa liste n’est pas exhaustive. | S-010 / [10] | MEDIUM-HIGH — advisory officiel mais rédigé pendant une phase d’analyse évolutive. |
| F-010 | Ars Technica rapporte que le code permettrait, sous certaines conditions, de faire passer une commande via un mécanisme SSH, mais précise qu’aucun code n’a été observé comme effectivement téléversé et que l’identité réelle derrière Jia Tan reste inconnue. | S-012 / [12] | MEDIUM — source secondaire crédible, mais dépendante d’analyses externes et de déclarations de chercheurs. |
| F-011 | Les sources consultées sont historiques et leur fraîcheur ne signifie pas que les pages ou les conclusions ont la même date de mise à jour : OpenSSF, Microsoft, Datadog et CERT-EU présentent des mises à jour distinctes. | S-004, S-006, S-007, S-010 / [4][6][7][10] | HIGH — observable dans les métadonnées des pages. |
| F-012 | La collecte de ce dossier est passive et limitée à des sources publiques ; aucun système cible, compte ou donnée personnelle privée n’a été investigué. | Journal de collecte local | HIGH — action effectivement réalisée. |
| F-013 | Une chronologie sourcée décrit un contributeur sous le nom « Jia Tan » actif pendant plus de deux ans, du premier correctif (2021-10-29) à l’obtention d’un accès en écriture et de la maintenance. | S-013 / [13] | MEDIUM-HIGH — compilation secondaire renvoyant à des archives publiques ; pas de revérification ligne à ligne. |
| F-014 | La même chronologie date l’insertion de fichiers de test binaires contenant le code caché au 2024-02-23, la première release produite par ce compte (v5.4.2) au 2023-03-18, et indique que l’accès en écriture est établi au 2022-12-30. | S-013 / [13] | MEDIUM-HIGH — dates au jour, sans heure ni fuseau. |
| F-015 | La découverte et la notification privée à Debian et à la liste distros@openwall sont datées du 2024-03-28 ; Red Hat attribue la CVE le même jour ; la divulgation publique suit le 29 mars. openSUSE confirme que le signalement a d’abord été adressé à Debian. | S-013, S-002, S-017 / [13][2][17] | MEDIUM-HIGH — la liste distros n’est pas publique ; séquence cohérente entre trois sources de lignées différentes. |
| F-016 | Red Hat indique que l’injection n’est complète que dans le paquet téléchargé : la distribution Git ne contient pas la macro M4 déclencheuse, mais contient les artefacts de second niveau ; la NVD décrit l’extraction d’un objet précompilé depuis un fichier de test déguisé. | S-011, S-014, S-013 / [11][14][13] | HIGH — deux sources officielles convergentes et une compilation indépendante. |
| F-017 | L’analyse publique du binaire indique que la porte dérobée valide une signature avec une clé publique Ed448 codée en dur et exige une charge chiffrée et signée avec la clé de l’attaquant ; une exploitation réussie ne génère aucune entrée de journal de niveau INFO ou supérieur. | S-015 / [15] | MEDIUM-HIGH — analyse d’un chercheur, reproductible et largement reprise, mais non institutionnelle. |
| F-018 | Arch Linux indique que le code distribué dans le tarball n’a pas été injecté dans ses binaires (le script ne visait que les environnements de build Debian/Fedora) et que sshd n’y est pas lié à liblzma. | S-016 / [16] | HIGH pour le périmètre Arch Linux. |
| F-019 | openSUSE indique que Tumbleweed et MicroOS ont inclus la version compromise du 7 au 28 mars 2024, et que le fichier malveillant n’est pas présent dans SUSE Linux Enterprise ni openSUSE Leap. | S-017 / [17] | HIGH pour le périmètre openSUSE / SUSE. |
| F-020 | La NVD affiche un score CVSS 3.1 de 10.0 (CRITICAL), attribué à la fois par la NVD et par le CNA Red Hat. | S-014 / [14] | HIGH — notice officielle ; le score mesure la gravité potentielle, pas une exploitation observée. |

---

## HYPOTHESES

### H1 — Compromission délibérée de la chaîne de publication/build

- **Soutien :** tarballs de release compromis, versions successives, code obfusqué, conditions de build ciblées et intervention dans le processus de publication.[2][3][4][10] Révision du 2026-10-30 : plus de deux ans de contributions préalables, accès en écriture puis maintenance des releases, et charge réservée au détenteur d’une clé Ed448 : la préparation est longue et délibérée.[13][15]
- **Affaiblissement :** les sources publiques ne démontrent pas à elles seules le nombre d’acteurs ni toute la chaîne opérationnelle.
- **Test ou information invalidante :** preuve indépendante d’une compromission accidentelle du compte ou d’un artefact de build sans intention malveillante ; les sources retenues ne fournissent pas cette preuve.
- **Confiance : HIGH** pour l’insertion volontaire de code malveillant ; MEDIUM pour la reconstruction complète de la campagne.

### H2 — Compromission d’un compte ou d’un environnement de mainteneur sans connaissance complète de l’auteur

- **Soutien :** l’identité réelle derrière le pseudonyme n’est pas établie et les sources ne donnent pas de preuve publique complète sur l’identité opérationnelle.[4][12]
- **Affaiblissement :** la répétition des modifications, la signature de tarballs et les ajustements entre versions sont plus compatibles avec une action structurée qu’avec un incident ponctuel, sans toutefois prouver le modèle exact.
- **Test ou information invalidante :** journaux d’accès, preuves cryptographiques, correspondances d’identité ou éléments d’infrastructure non publics.
- **Révision du 2026-10-30 :** la chronologie sourcée montre que le même compte contribue publiquement depuis 2021, obtient l’accès en écriture puis produit les releases ; l’hypothèse d’un compte légitime compromis à la dernière minute devient peu compatible avec ces observations.[13]
- **Confiance : LOW** — abaissée depuis LOW-MEDIUM ; hypothèse conservée pour mémoire, sans être exclue formellement en l’absence de données non publiques.

### H3 — Opération organisée ou soutenue par un acteur étatique

- **Soutien :** durée apparente de préparation, ciblage technique et effort de construction d’une position de confiance ; certaines analyses secondaires évoquent un profil compatible avec une opération très organisée.[7][12]
- **Affaiblissement :** aucune source primaire retenue n’identifie un État, un groupe ou une personne réelle ; OpenSSF indique que la motivation reste inconnue.[4]
- **Test ou information invalidante :** renseignement indépendant et vérifiable reliant l’opération à un acteur identifié.
- **Confiance : LOW** — hypothèse plausible mais insuffisamment étayée ; aucune attribution n’est retenue.

---

## Timeline

> Les timestamps sont conservés avec le fuseau fourni. Lorsqu’une page n’affiche pas de timezone ou d’heure complète, la normalisation UTC est indiquée comme non disponible.

| Timestamp source | Timezone / source timezone | Normalized UTC | Événement | Source | Statut |
|------------------|----------------------------|----------------|-----------|--------|--------|
| 2021-10-29 — heure non fournie | unknown | not available | Premier correctif du compte « Jia Tan » sur la liste xz-devel. | S-013 / [13] | rapporté (compilation sourcée) |
| 2022-12-30 — heure non fournie | unknown | not available | Lot de commits fusionné directement dans le dépôt : accès en écriture établi. | S-013 / [13] | rapporté (compilation sourcée) |
| 2023-03-18 — heure non fournie | unknown | not available | Première release (v5.4.2) produite par ce compte. | S-013 / [13] | rapporté (compilation sourcée) |
| 2024-02-23 — heure non fournie | unknown | not available | Ajout de fichiers de test binaires contenant le code caché. | S-013 / [13] | rapporté (compilation sourcée) |
| `24 Feb 08:22` — année contextuelle 2024 | unknown | not available | Tag GitHub v5.6.0 affiché sous JiaT75 ; date du 2024-02-24 corroborée au jour par [13]. | S-008 / [8] ; S-013 / [13] | confirmé comme affichage de page ; heure/fuseau incomplets |
| `09 Mar 08:16` — année contextuelle 2024 | unknown | not available | Tag GitHub v5.6.1 affiché sous JiaT75 ; date du 2024-03-09 corroborée au jour par [13]. | S-009 / [9] ; S-013 / [13] | confirmé comme affichage de page ; heure/fuseau incomplets |
| 2024-03-07 → 2024-03-28 | unknown | not available | Version compromise incluse dans openSUSE Tumbleweed et MicroOS. | S-017 / [17] | confirmé pour openSUSE |
| 2024-03-28 — heure non fournie | unknown | not available | Découverte et notification privée à Debian et distros@openwall ; CVE-2024-3094 attribuée par Red Hat. Date d’identification également rapportée par Microsoft et Datadog. | S-013, S-006, S-007 / [13][6][7] | rapporté ; cohérent entre lignées distinctes |
| 2024-03-29T08:51:26-07:00 | UTC−07:00 | 2024-03-29T15:51:26Z | Publication du rapport technique d’Andres Freund sur oss-security. | S-002 / [2] | confirmé |
| 2024-03-29T16:09:37+00:00 | UTC | 2024-03-29T16:09:37Z | Publication de l’advisory Debian DSA-5649-1. | S-005 / [5] | confirmé |
| 2024-03-29 — heure non fournie | unknown | not available | Publication de l’alerte CISA. | S-001 / [1] | confirmé comme date de publication |
| 2024-03-30 — heure non fournie | unknown | not available | Publication initiale de l’article OpenSSF ; mise à jour affichée au 1er avril. | S-004 / [4] | confirmé comme métadonnée de page |
| 2024-04-01 — heure non fournie | unknown | not available | Publication de la guidance Microsoft ; mise à jour affichée au 7 avril. | S-006 / [6] | confirmé comme métadonnée de page |
| 2024-04-02 — heure non fournie | unknown | not available | Advisory CERT-EU v1.1 ; historique indiquant une v1.0 au 30 mars. | S-010 / [10] | confirmé |
| 2024-04-03 — heure non fournie | unknown | not available | Publication de l’analyse Datadog ; dernière mise à jour affichée au 8 avril. | S-007 / [7] | confirmé |
| 2024-05-29 — heure non fournie | unknown | not available | La page du mainteneur indique la publication de nouvelles releases propres. | S-003 / [3] | rapporté par le mainteneur |
| 2026-08-21T15:51:32+02:00 | Europe/Paris / UTC+02:00 | 2026-08-21T13:51:32Z | Collecte des pages publiques pour ce dossier. | Journal local et ledger | confirmé |

---

## SOURCE ASSESSMENT

| Source | Type | Primary / Secondary | Reliability | Corroboration / dépendance | Fraîcheur et limites |
|--------|------|---------------------|-------------|----------------------------|---------------------|
| S-001 CISA | advisory gouvernemental | Primary pour la position CISA ; secondary pour l’incident initial | HIGH | Cohérent avec Debian, XZ, Openwall et CERT-EU ; alerte historique | 2024-03-29 ; utile pour l’alerte et la recommandation, pas pour l’état courant de toutes les distributions. |
| S-002 Openwall / Freund | rapport technique primaire | Primary | HIGH pour les observations et l’analyse de l’auteur | Source initiale majeure ; plusieurs sources secondaires la citent | 2024-03-29 ; l’auteur précise lui-même que certaines parties du mécanisme n’étaient pas encore complètement analysées. |
| S-003 XZ maintainer | déclaration officielle du projet | Primary pour le statut du projet | MEDIUM-HIGH | Corrobore versions et remédiation ; intérêt direct dans la communication de crise | Page évolutive ; elle mélange faits historiques et mises à jour ultérieures. |
| S-004 OpenSSF | synthèse d’experts | Secondary | MEDIUM-HIGH | Reprend Openwall, Red Hat et Debian ; dépendance explicite à ces sources | Publiée 2024-03-30, mise à jour 2024-04-01 ; utile pour la synthèse, moins forte qu’une preuve technique originale. |
| S-005 Debian DSA | advisory distribution | Primary pour Debian | HIGH | Corrobore versions et périmètre Debian ; source indépendante de la communication Microsoft | 2024-03-29 ; périmètre limité à Debian. |
| S-006 Microsoft | guidance fournisseur | Secondary / technical | HIGH pour les recommandations Microsoft ; MEDIUM pour l’impact global | Reprend CISA et advisories des distributions | Publiée 2024-04-01, mise à jour 2024-04-07 ; document de réponse, pas une autopsie complète. |
| S-007 Datadog | analyse fournisseur de sécurité | Secondary / technical | MEDIUM-HIGH | Curation explicite de sources externes ; dépend d’Openwall et d’autres analyses | Publiée 2024-04-03, mise à jour 2024-04-08 ; utile pour mécanisme, risque de propagation narrative. |
| S-008/S-009 GitHub releases | métadonnées de dépôt | Primary | HIGH pour les tags affichés ; MEDIUM pour le contexte temporel incomplet | Corrobore la séquence des releases ; ne prouve pas à elle seule l’intention | Heure et fuseau non affichés dans l’extrait ; année contextualisée mais non répétée par la page. |
| S-010 CERT-EU | advisory institutionnel européen | Primary pour l’advisory ; Secondary pour les détails repris | HIGH pour la publication ; MEDIUM-HIGH pour les détails techniques en évolution | Références Openwall, Red Hat, Debian et autres advisories | v1.0 du 30 mars, v1.1 du 2 avril ; signale que la liste des distributions n’est pas exhaustive. |
| S-011 Red Hat | advisory fournisseur/distribution | Primary pour le périmètre Red Hat | HIGH | Corrobore avec Debian la distinction entre branches de développement et systèmes stables ; périmètre spécifique | 2024-03-29, mise à jour 2024-03-30 ; conclusions propres à Red Hat/Fedora. L’URL citée redirige depuis vers `…fedora-40-and-rawhide-users` : le titre parle désormais de Fedora Linux 40, ce qui concorde avec F-006. |
| S-012 Ars Technica | journalisme technique | Secondary | MEDIUM | S’appuie sur Freund, Openwall, analyses de chercheurs et advisories | Source contemporaine utile pour le contexte ; ne doit pas soutenir seule une attribution. |
| S-013 Russ Cox, chronologie | compilation chronologique sourcée | Secondary (renvoie à des archives primaires) | MEDIUM-HIGH | Lignée propre ; chaque entrée pointe vers une archive xz-devel, un commit git ou un rapport de bug ; reprend aussi S-002 | Publiée 2024-04-01, mise à jour 2024-04-03 ; dates au jour sans fuseau ; les liens primaires ne sont pas revérifiés un à un ici. |
| S-014 NIST NVD | notice de vulnérabilité officielle | Primary pour la notice et le score | HIGH | Description fournie par le CNA Red Hat ; corrobore S-011 | Publiée 2024-03-29, dernière modification 2026-06-17 ; le score est une gravité potentielle. |
| S-015 xzbot | analyse technique de chercheur (rétro-ingénierie) | Primary pour l’analyse du binaire | MEDIUM-HIGH | Lignée distincte de S-002 pour le format de la charge ; cite d’autres analyses publiques | 2024-04-01 → 2024-04-03 ; démonstration en laboratoire avec une clé substituée, pas une observation d’exploitation réelle. |
| S-016 Arch Linux | annonce de distribution | Primary pour Arch Linux | HIGH | Indépendante de Debian et Red Hat ; reprend S-002 pour le contexte | 2024-03-29, mise à jour ultérieure ; périmètre Arch uniquement. |
| S-017 openSUSE | annonce de distribution | Primary pour openSUSE / SUSE | HIGH pour le périmètre ; MEDIUM pour la description de l’impact | Indépendante de Debian et Red Hat | 2024-03-29 ; précise que la rétro-ingénierie était alors en cours. |

---

## CONTRADICTIONS

### C-001 — 28 mars contre 29 mars

Microsoft et Datadog indiquent le 28 mars comme date d’identification, alors que le message public d’Andres Freund est horodaté le 29 mars à 08:51:26 UTC−07:00.[6][7][2]

**Évaluation :** il s’agit probablement de jalons différents — observation initiale, analyse privée, notification ou publication — mais les sources retenues ne permettent pas de déterminer exactement quelle étape correspond à chaque date. La contradiction est conservée comme une incertitude chronologique.

**Révision du 2026-10-30 — réconciliée (MEDIUM-HIGH) :** la chronologie sourcée situe au 28 mars la découverte et la notification privée à Debian et à la liste distros@openwall, et au 29 mars la divulgation publique ; openSUSE confirme que le signalement est d’abord allé à Debian.[13][17] Les deux dates désignent donc deux jalons distincts. L’heure et le jour de la première observation des symptômes restent inconnus : Andres Freund parle lui-même des « dernières semaines ».

### C-002 — « Linux largement affecté » contre impact principalement pré-release

Les formulations générales de CISA et de certaines analyses secondaires peuvent donner une impression de compromission généralisée, tandis que Debian précise que stable n’était pas connu comme affecté et Red Hat indique que RHEL n’était pas affecté.[1][5][11]

**Évaluation :** pas de contradiction directe après segmentation par distribution et canal de publication. La formulation correcte est : **versions compromises publiées ; exposition dépendante de la distribution, du canal, du build et de l’intégration OpenSSH**.

### C-003 — Contenu du dépôt contre contenu des tarballs

Openwall décrit une portion du backdoor uniquement présente dans les tarballs et d’autres éléments obfusqués présents dans le dépôt ; Ars Technica résume le mécanisme comme absent du dépôt GitHub et présent dans les tarballs.[2][12]

**Évaluation :** les formulations semblent viser des étapes différentes de la chaîne : artefacts préparatoires dans le dépôt versus déclencheur/build malveillant dans les tarballs. Il ne faut pas réduire cette nuance à « tout était dans Git » ou « rien n’était dans Git » sans examiner chaque artefact.

**Révision du 2026-10-30 — résolue au niveau documentaire (HIGH) :** Red Hat précise que la macro M4 déclenchant la construction du code malveillant n’existe que dans le paquet téléchargé, tandis que les artefacts de second niveau sont présents dans le dépôt Git ; la NVD et la chronologie sourcée décrivent un objet précompilé caché dans des fichiers de test binaires du dépôt.[11][14][13] Les deux formulations sont donc exactes pour des étapes différentes. Une comparaison octet par octet des artefacts n’a pas été faite.

### C-004 — Capacité technique et exploitation observée

Openwall indique que le mécanisme semblait permettre une forme d’accès ou de RCE pré-authentification, tandis que CERT-EU décrit une capacité de RCE sous conditions ; Ars Technica indique qu’aucun code téléversé n’a été observé.[2][10][12]

**Évaluation :** il s’agit principalement d’une évolution du niveau d’analyse : capacité théorique ou démontrée par reverse engineering ne signifie pas exploitation réussie dans la nature. Aucune exploitation à grande échelle n’est retenue comme fait.

**Révision du 2026-10-30 :** l’analyse du binaire précise la nature de la capacité : exécution de commande pré-authentification conditionnée à une charge signée avec la clé Ed448 de l’attaquant.[15] « RCE » et « contournement d’authentification » décrivent donc la même capacité, réservée au détenteur de la clé ; aucune source ne rapporte d’exploitation réelle.

### C-005 — Motivation et identité

OpenSSF indique que la motivation reste inconnue ; Ars Technica indique que l’existence d’une personne réelle derrière Jia Tan n’est pas établie, tandis que certaines analyses secondaires évoquent un acteur étatique ou organisé.[4][12]

**Évaluation :** ce n’est pas une contradiction tranchée mais un conflit de niveaux de preuve. Le dossier conserve l’attribution comme hypothèse LOW et ne la présente pas comme conclusion.

### C-006 — « Accès pour des acteurs malveillants » contre accès réservé au détenteur d’une clé

openSUSE écrit, le 29 mars, que la porte dérobée permet à des acteurs malveillants d’accéder aux systèmes exposant SSH, tout en précisant que la rétro-ingénierie est en cours ; l’analyse ultérieure du binaire montre que la charge doit être signée avec la clé Ed448 de l’attaquant.[17][15]

**Évaluation :** pas de contradiction de fond, mais une différence de date et de précision. Le risque pour les systèmes exposés était réel ; il n’ouvrait pas l’accès à n’importe quel tiers. La recommandation openSUSE de réinstaller reste cohérente avec F-017 : l’exploitation ne laisse pas de trace dans les journaux usuels.

---

## MATRICE D’EXPOSITION PAR DISTRIBUTION

> Trois conditions sont nécessaires à l’exposition : **(1)** une version 5.6.0 ou 5.6.1 présente ; **(2)** le code malveillant effectivement compilé, ce qui exigeait un build de paquet DEB ou RPM x86-64 ; **(3)** un sshd lié à liblzma, en pratique via le patch libsystemd. Une distribution peut remplir (1) sans remplir (2) ou (3).[4][13][16]

| Distribution / canal | (1) Version présente | (2) Code compilé | (3) sshd lié à liblzma | Source | Lecture |
|---|---|---|---|---|---|
| Debian testing, unstable, experimental | oui | oui (injection observée sur unstable) | oui (sshd patché pour libsystemd) | [5][11][13] | exposé |
| Debian stable | non connu | — | — | [5] | non connu comme affecté |
| Fedora Rawhide | oui (5.6.0 ou 5.6.1) | non précisé | — | [11] | arrêt d’usage demandé par Red Hat |
| Fedora Linux 40 beta | oui (paquets 5.6.0) | « pas montré compromis » | — | [11] | rétrogradation recommandée |
| RHEL | non | — | — | [11] | non affecté |
| openSUSE Tumbleweed, MicroOS | oui (7–28 mars 2024) | non précisé | décrit comme actif dans sshd | [17] | réinstallation recommandée si SSH exposé |
| SUSE Linux Enterprise, openSUSE Leap | non | — | — | [17] | non affecté |
| Arch Linux | oui (paquets 5.6.0-1, 5.6.1-1) | non selon Arch | non | [16][13] | vecteur SSH non applicable selon Arch |
| Ubuntu | non vérifié | — | — | page en erreur 503 le 2026-10-30 | lacune de collecte |

Les cellules « — » ne sont pas renseignées par les sources retenues. Une absence de mention ne vaut pas absence d’exposition.

---

## CONFIDENCE

**Confiance globale : MEDIUM-HIGH.**

**Justification :** les versions, l’existence du code malveillant, la publication du rapport initial, le périmètre Debian et les mesures de réponse sont corroborés par plusieurs sources primaires et techniques. La confiance globale est inférieure à HIGH pour les éléments qui dépendent d’analyses évolutives, de sources secondaires ou d’informations non publiques : première minute de découverte, exploitation réelle, identité et attribution.

| Jugement | Confidence | Justification |
|----------|------------|---------------|
| XZ Utils 5.6.0 et 5.6.1 sont les versions centrales du cas | HIGH | CISA, XZ, Debian et les métadonnées GitHub convergent. |
| Le mécanisme implique la chaîne de publication/build et liblzma | HIGH | Openwall, OpenSSF, CERT-EU et sources techniques convergent ; détails fins à rattacher aux artefacts correspondants. |
| L’impact a été limité à certains canaux/distributions et n’est pas équivalent à une compromission universelle | HIGH pour Debian/Red Hat ; MEDIUM pour l’écosystème global | Les sources sont précises pour leurs périmètres mais ne couvrent pas toutes les distributions. |
| Une exploitation réussie à grande échelle a eu lieu | LOW / non établi | Les sources décrivent une capacité et un risque ; aucune preuve retenue d’exploitation réussie à grande échelle. |
| La capacité est une exécution de commande pré-authentification réservée au détenteur de la clé Ed448 | HIGH | Mécanisme décrit par l’analyse du binaire et reproduit en laboratoire avec une clé substituée ; cohérent avec les advisories.[15] |
| La compromission résulte d’une préparation de plus de deux ans | MEDIUM-HIGH | Chronologie sourcée renvoyant à des archives publiques, non revérifiée ligne à ligne.[13] |
| Le 28 mars désigne la notification privée et le 29 mars la divulgation publique | MEDIUM-HIGH | Trois lignées concordantes ; la liste distros n’est pas publique.[13][2][17] |
| Jia Tan correspond à une personne réelle identifiable | LOW / non établi | Les sources publiques retenues signalent explicitement cette incertitude. |
| Attribution à un État ou à un groupe précis | LOW / non retenue | Aucun élément primaire suffisant ; hypothèse fondée surtout sur des inférences secondaires. |

---

## LIMITATIONS

- Les pages ont été consultées le 21 août 2026, mais une partie des documents est historique et certains sont évolutifs.
- Les timestamps de plusieurs pages sont seulement des dates sans heure ni timezone.
- Les dates affichées par GitHub pour les releases ne fournissent pas de timezone dans l’extrait collecté.
- Les sources secondaires dépendent parfois des mêmes sources primaires ; leur nombre ne constitue donc pas automatiquement un nombre équivalent de sources indépendantes.
- Aucun accès aux journaux de commit complets, aux artefacts binaires originaux, aux logs d’infrastructure ou aux données d’exploitation n’a été réalisé dans ce dossier.
- Les conclusions sur l’intention, l’identité et l’attribution restent limitées par l’absence de données non publiques.
- La collecte web dépend du contenu rendu par les pages au moment de l’accès ; les extraits conservés ne remplacent pas les archives originales.
- La collecte complémentaire du 2026-10-30 passe par un service d’extraction de pages tiers ; la page Ubuntu n’a pas pu être lue (HTTP 503) et la matrice d’exposition reste incomplète.
- La chronologie longue [13] est une compilation secondaire : ses liens vers les archives xz-devel et les commits n’ont pas été revérifiés un à un dans ce dossier.

---

## UNKNOWNS / INTELLIGENCE GAPS

- Quelle est la date et l’heure exactes de la première observation de l’anomalie ? La notification privée (28 mars) et la publication (29 mars) sont désormais distinguées ; la première observation des symptômes reste non datée.
- Quelle a été l’étendue exacte des paquets distribués et installés dans chaque distribution et canal ?
- Des systèmes de production ont-ils exécuté un build compromis ou exposé un SSH vulnérable ?
- Une exploitation réelle a-t-elle été observée, par qui, quand et avec quels artefacts ?
- Quelle est la chaîne complète d’identités, de comptes et d’infrastructures derrière les pseudonymes ?
- Quelle motivation opérationnelle précise était poursuivie ?
- Quels éléments du backdoor étaient dans le dépôt, les tarballs, les scripts de build et les binaires selon chaque version ?
- Les pages officielles ont-elles été modifiées ou révisées après les dates visibles dans les extraits ?

---

## RECOMMENDED NEXT STEPS

1. Pour une analyse historique plus fine, conserver des copies versionnées ou des archives datées des advisories et comparer les versions successives plutôt que de se fier uniquement à la page actuelle.
2. Construire une matrice par distribution, version, canal et méthode de build ; ne pas généraliser le périmètre Debian ou Red Hat à tout Linux.
3. Rattacher chaque affirmation technique à un artefact précis : commit, tarball, script de build, objet compilé ou advisory de distribution.
4. Traiter l’identité et l’attribution comme des intelligence gaps, sauf apparition d’éléments indépendants et vérifiables.
5. Pour un usage défensif, utiliser les recommandations des distributions et de CISA dans un environnement autorisé ; ce dossier ne réalise aucune vérification de systèmes réels.

---

## Revue critique indépendante

### Conclusions les moins solides

- L’attribution à un acteur étatique ou à une personne réelle est la partie la moins solide ; elle reste LOW et n’est pas retenue comme finding établi.
- La date exacte de la première découverte est ambiguë entre les formulations du 28 et du 29 mars.
- L’exploitation réelle à grande échelle n’est pas démontrée par les sources collectées.

### Affirmations dépendant d’une seule source

- Les heures affichées par GitHub pour les tags 5.6.0 et 5.6.1 reposent sur les pages GitHub correspondantes ; elles sont corroborées par la séquence générale, mais pas par un second registre indépendant.
- L’absence d’affectation de RHEL repose principalement sur l’advisory Red Hat ; elle est valide pour le périmètre Red Hat, pas pour tout l’écosystème.
- Les détails de la première observation reposent principalement sur le rapport d’Andres Freund, qui est la source primaire appropriée mais unique pour son expérience directe.

### Biais de sélection

- La collecte privilégie les sources institutionnelles et techniques anglophones, ce qui peut sous-représenter des analyses indépendantes ou des sources de distributions non incluses.
- Plusieurs sources secondaires citent les mêmes advisories ; leur convergence narrative ne doit pas être comptée comme corroboration totalement indépendante.
- Les sources postérieures à l’événement peuvent bénéficier d’informations découvertes après les premières alertes, ce qui explique certaines différences de précision.

### Contradictions insuffisamment explorées

- La contradiction apparente entre dépôt et tarballs est résolue au niveau documentaire (révision du 2026-10-30) ; une comparaison artefact par artefact, octet par octet, reste à faire.
- Les différences de formulation sur RCE, bypass et exploitation devraient être comparées avec la date et le niveau de reverse engineering de chaque source.
- La portée par distribution couvre désormais Debian, Fedora/RHEL, Arch Linux et openSUSE/SUSE ; Ubuntu et les distributions non documentées restent à couvrir.

### Informations qui pourraient invalider l’analyse

- Preuve que les versions ou tarballs citées ne contenaient pas le code décrit.
- Logs ou rapports montrant une exploitation réussie à grande échelle, ou au contraire démontrant l’absence vérifiable d’exploitation dans tous les environnements concernés.
- Éléments authentifiés établissant une autre cause que l’insertion malveillante dans la chaîne de publication.
- Nouvelle analyse primaire démontrant une attribution spécifique avec une chaîne de preuve indépendante.

---

## Sources

[1] https://www.cisa.gov/news-events/alerts/2024/03/29/reported-supply-chain-compromise-affecting-xz-utils-data-compression-library-cve-2024-3094
    > "CISA and the open source community are responding to reports of malicious code being embedded in XZ Utils versions 5.6.0 and 5.6.1. This activity was assigned CVE-2024-3094."
[2] https://www.openwall.com/lists/oss-security/2024/03/29/4
    > "The upstream xz repository and the xz tarballs have been backdoored."
[3] https://tukaani.org/xz-backdoor
    > "XZ Utils 5.6.0 and 5.6.1 release tarballs contain a backdoor."
[4] https://openssf.org/blog/2024/03/30/xz-backdoor-cve-2024-3094
    > "While the motivation behind this backdoor remains unknown, the intent was to compromise specific distributions, as the backdoors were only applied to DEB or RPM packages for the x86-64 architecture built with gcc and the gnu linker."
[5] https://www.debian.org/security/dsa-5649-1
    > "Right now no Debian stable versions are known to be affected."
[6] https://techcommunity.microsoft.com/blog/vulnerability-management/microsoft-faq-and-guidance-for-xz-utils-backdoor/4101961
    > "On March 28, 2024 a backdoor was identified in XZ Utils."
[7] https://securitylabs.datadoghq.com/articles/xz-backdoor-cve-2024-3094
    > "When a malicious version of the `xz-utils` library is installed, a malicious shared object (SO) file is stored on disk."
[8] https://github.com/tukaani-project/xz/releases/tag/v5.6.0
    > "> JiaT75 tagged this 24 Feb 08:22"
[9] https://github.com/tukaani-project/xz/releases/tag/v5.6.1
    > "> JiaT75 tagged this 09 Mar 08:16"
[10] https://cert.europa.eu/publications/security-advisories/2024-032/pdf
    > "On March 29, several companies issued a warning regarding a backdoor found in the XZ Utils software."
[11] https://www.redhat.com/en/blog/urgent-security-alert-fedora-41-and-rawhide-users
    > "No versions of Red Hat Enterprise Linux (RHEL) are affected by this CVE."
[12] https://arstechnica.com/security/2024/04/what-we-know-about-the-xz-utils-backdoor-that-almost-infected-the-world
    > "At the moment, it’s unknown if there was ever a real-world person behind this username or if Jia Tan is a completely fabricated individual."
[13] https://research.swtch.com/xz-timeline
    > "Over a period of over two years, an attacker using the name “Jia Tan” worked as a diligent, effective contributor to the xz compression library, eventually being granted commit access and maintainership."
[14] https://nvd.nist.gov/vuln/detail/CVE-2024-3094
    > "Malicious code was discovered in the upstream tarballs of xz, starting with version 5.6.0."
[15] https://github.com/amlweems/xzbot
    > "The backdoor uses a hardcoded ED448 public key for signature validation and decrypting the payload."
[16] https://archlinux.org/news/the-xz-package-has-been-backdoored/
    > "To our knowledge the malicious code which was distributed via the release tarball never made it into the Arch Linux provided binaries, as the build script was configured to only inject the bad code in Debian/Fedora based package build environments."
[17] https://news.opensuse.org/2024/03/29/xz-backdoor/
    > "Our rolling release distribution openSUSE Tumbleweed and openSUSE MicroOS included this version between March 7 and March 28."
