# Registre des preuves - Case 04 (OSINT-XZ-UTILS-2026-001)

> **Case :** [rapport public](report.md)
> **Collection batch :** `2026-08-21T15:51:32+02:00` — UTC normalisé : `2026-08-21T13:51:32Z`.
> **Méthode :** consultation passive de pages publiques par recherche web et extraction de pages. Aucun scan, aucune interaction avec une cible et aucune collecte de données personnelles inutiles.
> **Références méthodologiques :** [méthodologie commune du casebook](../../methodology/).

---

## 1. Règles d’interprétation appliquées

- **Reliability** = fiabilité de la source et de son acquisition pour le type d’information concerné.
- **Confidence** = confiance dans l’affirmation ou l’analyse associée après prise en compte du contexte, de la corroboration et des limites.
- `Direct observation` signifie que le contenu de la page a été directement consulté par l’analyste via l’outil de collecte.
- `Reported` serait utilisé pour une déclaration rapportée par une source ; ici, le contenu de la page est directement observé mais plusieurs sources rapportent elles-mêmes des faits antérieurs.
- `Derived` est utilisé pour les éléments calculés ou reconstruits à partir de plusieurs preuves.
- Les timestamps originaux sont conservés. Une conversion UTC n’est renseignée que lorsque l’offset est disponible.

---

## 2. Registre principal

| Evidence ID | Type | Description | Source | Source type | Primary / Secondary | Direct observation / Reported / Derived | Collection timestamp | Timezone | Normalized UTC (si disponible) | Hash si pertinent | Corroboration | Reliability | Confidence | Notes | Chain of custody / provenance |
|-------------|------|-------------|--------|-------------|---------------------|------------------------------------------|-----------------------|----------|-------------------------------|--------------------|---------------|-------------|------------|-------|--------------------------------|
| E-001 | advisory | CISA rapporte du code malveillant dans XZ Utils 5.6.0 et 5.6.1 et associe l’activité à CVE-2024-3094. | S-001 — [1] — CISA | advisory gouvernemental | Primary pour l’alerte CISA ; Secondary pour l’incident sous-jacent | Direct observation | 2026-08-21T15:51:32+02:00 | Europe/Paris / UTC+02:00 | 2026-08-21T13:51:32Z | N/A — page web | E-002, E-003, E-005, E-010 | HIGH — organisme officiel et page accessible | HIGH — formulation corroborée par plusieurs sources | Alerte datée du 2024-03-29 ; utile pour versions et recommandation, pas pour l’état actuel de toutes les distributions. | URL enregistrée dans `citations-ledger.json`; extrait verbatim dans `source-extracts.md`. |
| E-002 | rapport technique | Andres Freund décrit des symptômes CPU/Valgrind autour de liblzma sur Debian Sid et conclut que le dépôt et les tarballs ont été backdoorés. | S-002 — [2] — Openwall oss-security | rapport technique primaire | Primary | Direct observation | 2026-08-21T15:51:32+02:00 | Europe/Paris / UTC+02:00 | 2026-08-21T13:51:32Z | N/A — page web | E-001, E-003, E-005, E-010 | HIGH — rapport technique horodaté et détaillé | HIGH pour les observations de l’auteur ; MEDIUM pour les parties que l’auteur dit ne pas avoir complètement analysées | Message source : 2024-03-29T08:51:26-07:00, soit 2024-03-29T15:51:26Z. | URL et quote enregistrées ; aucune copie binaire de pièce jointe acquise. |
| E-003 | déclaration de mainteneur | Le projet XZ affirme que les tarballs 5.6.0 et 5.6.1 contiennent un backdoor et décrit les mesures de remise en état. | S-003 — [3] — tukaani.org/xz-backdoor | page officielle du projet | Primary pour le statut du projet ; Secondary pour l’analyse externe | Direct observation | 2026-08-21T15:51:32+02:00 | Europe/Paris / UTC+02:00 | 2026-08-21T13:51:32Z | N/A — page web | E-001, E-002, E-005 | MEDIUM-HIGH — source officielle mais intéressée par la communication de crise | HIGH pour l’énoncé sur les tarballs ; MEDIUM pour les éléments historiques non accompagnés d’artefacts dans la page | Page évolutive ; elle contient aussi des mises à jour jusqu’à 2025-01-17. | URL et quote enregistrées dans le ledger ; extrait conservé localement. |
| E-004 | analyse de synthèse | OpenSSF décrit l’intention de compromettre certaines distributions et indique que la motivation reste inconnue. | S-004 — [4] — OpenSSF | publication d’experts / synthèse | Secondary | Direct observation | 2026-08-21T15:51:32+02:00 | Europe/Paris / UTC+02:00 | 2026-08-21T13:51:32Z | N/A — page web | E-001, E-002, E-005, E-010 | MEDIUM-HIGH — organisation experte, dépendances explicites | HIGH pour la réserve « motivation inconnue » ; MEDIUM-HIGH pour les détails de build repris d’autres sources | Publication 2024-03-30, mise à jour affichée au 2024-04-01. | URL et quote enregistrées ; provenance secondaire explicitement notée. |
| E-005 | advisory | Debian indique que les paquets compromis concernaient testing/unstable/experimental et qu’aucune version stable n’était alors connue comme affectée. | S-005 — [5] — Debian DSA-5649-1 | advisory de distribution | Primary pour Debian | Direct observation | 2026-08-21T15:51:32+02:00 | Europe/Paris / UTC+02:00 | 2026-08-21T13:51:32Z | N/A — page web | E-001, E-004, E-006, E-011 | HIGH — advisory signé et spécifique au périmètre Debian | HIGH pour les versions et canaux Debian décrits | Message source : 2024-03-29T16:09:37Z. | URL, identifiant DSA et quote enregistrés ; signature visible dans la page extraite. |
| E-006 | guidance fournisseur | Microsoft décrit la situation, les versions 5.6.0/5.6.1 et des moyens d’évaluer l’exposition dans ses produits. | S-006 — [6] — Microsoft | guidance technique fournisseur | Secondary / technical | Direct observation | 2026-08-21T15:51:32+02:00 | Europe/Paris / UTC+02:00 | 2026-08-21T13:51:32Z | N/A — page web | E-001, E-005, E-011 | HIGH pour la guidance Microsoft ; MEDIUM pour l’impact global | HIGH pour le contenu de la guidance ; MEDIUM pour la date de découverte et les généralisations | Publiée 2024-04-01, mise à jour affichée au 2024-04-07. | URL et quote enregistrées ; les requêtes Microsoft ne sont pas exécutées dans ce cas OSINT. |
| E-007 | analyse technique | Datadog résume le chargement d’un objet partagé malveillant et l’interception d’une fonction OpenSSL sous certaines conditions. | S-007 — [7] — Datadog Security Labs | analyse de sécurité fournisseur | Secondary / technical | Direct observation | 2026-08-21T15:51:32+02:00 | Europe/Paris / UTC+02:00 | 2026-08-21T13:51:32Z | N/A — page web | E-002, E-004, E-010, E-012 | MEDIUM-HIGH — expertise technique mais curation de sources externes | MEDIUM-HIGH — mécanisme cohérent, mais pas preuve d’exploitation réelle | Publiée 2024-04-03, dernière mise à jour affichée au 2024-04-08. | URL et quote enregistrées ; aucune reproduction du mécanisme. |
| E-008 | métadonnée de release | La page GitHub affiche le tag v5.6.0 sous JiaT75 avec `24 Feb 08:22`. | S-008 — [8] — GitHub release v5.6.0 | métadonnée de dépôt | Primary pour la page de release | Direct observation | 2026-08-21T15:51:32+02:00 | Europe/Paris / UTC+02:00 | 2026-08-21T13:51:32Z | N/A — page web | E-002, E-003, E-009 | HIGH — métadonnée de plateforme | HIGH pour le texte affiché ; MEDIUM pour année/fuseau non fournis | L’année est contextualisée par le tag et le dossier 2024 mais non répétée dans l’extrait ; aucune conversion UTC. | URL et quote enregistrées ; timestamp original conservé tel qu’affiché. |
| E-009 | métadonnée de release | La page GitHub affiche le tag v5.6.1 sous JiaT75 avec `09 Mar 08:16`. | S-009 — [9] — GitHub release v5.6.1 | métadonnée de dépôt | Primary pour la page de release | Direct observation | 2026-08-21T15:51:32+02:00 | Europe/Paris / UTC+02:00 | 2026-08-21T13:51:32Z | N/A — page web | E-002, E-003, E-008 | HIGH — métadonnée de plateforme | HIGH pour le texte affiché ; MEDIUM pour année/fuseau non fournis | Aucune conversion UTC ; ne pas présenter l’heure comme locale ou UTC. | URL et quote enregistrées ; timestamp original conservé tel qu’affiché. |
| E-010 | advisory | CERT-EU décrit la capacité pré-authentification sous conditions et liste des distributions touchées ou non touchées, en indiquant que la liste n’est pas exhaustive. | S-010 — [10] — CERT-EU Advisory 2024-032 | advisory institutionnel européen | Primary pour l’advisory ; Secondary pour les détails repris | Direct observation | 2026-08-21T15:51:32+02:00 | Europe/Paris / UTC+02:00 | 2026-08-21T13:51:32Z | N/A — PDF distant, hash non acquis | E-001, E-002, E-005, E-011, E-012 | HIGH pour la publication ; MEDIUM-HIGH pour les détails en évolution | MEDIUM-HIGH — la version 1.1 met à jour l’analyse et rappelle que la liste est incomplète | v1.0 datée du 2024-03-30 ; v1.1 datée du 2024-04-02. Encodage du PDF imparfait dans l’extraction. | URL PDF et historique de version conservés ; pas de téléchargement local du PDF. |
| E-011 | advisory | Red Hat indique que RHEL n’est pas affecté et distingue Fedora 40 beta de Fedora Rawhide. | S-011 — [11] — Red Hat | advisory fournisseur/distribution | Primary pour le périmètre Red Hat | Direct observation | 2026-08-21T15:51:32+02:00 | Europe/Paris / UTC+02:00 | 2026-08-21T13:51:32Z | N/A — page web | E-001, E-005, E-010 | HIGH — source mainteneur/distribution | HIGH pour les déclarations propres à Red Hat ; non extrapolable aux autres distributions | Publié 2024-03-29, mise à jour affichée au 2024-03-30. | URL et quote enregistrées ; périmètre explicitement limité à Red Hat/Fedora. |
| E-012 | article journalistique | Ars Technica synthétise la chronologie, le mécanisme et l’incertitude sur l’identité réelle derrière Jia Tan. | S-012 — [12] — Ars Technica | journalisme technique | Secondary | Direct observation | 2026-08-21T15:51:32+02:00 | Europe/Paris / UTC+02:00 | 2026-08-21T13:51:32Z | N/A — page web | E-002, E-005, E-007, E-011 | MEDIUM — média spécialisé citant des sources techniques | MEDIUM pour le contexte ; LOW pour toute attribution ou identité | Source contemporaine utile mais narrative et dépendante de chercheurs/advisories externes. | URL et quote enregistrées ; ne soutient pas seule un finding technique critique. |
| E-013 | artefact dérivé | Extraits verbatim des pages consultées, utilisés pour les quotes du ledger. | [`source-extracts.md`](source-extracts.md) | artefact de collecte dérivé | Derived | Derived | 2026-08-21T15:51:32+02:00 | Europe/Paris / UTC+02:00 | 2026-08-21T13:51:32Z | SHA-256:c06370b5f0d48905a2504ccd44f429d02f59780d9beee491a2c386e04ead45fb | E-001 à E-012 | HIGH pour l’intégrité du fichier ; dépend des pages sources | HIGH pour la traçabilité des quotes ; ne constitue pas une source indépendante | Le fichier conserve uniquement des extraits, pas l’intégralité des pages. | Créé dans le dossier du cas ; hash calculé après écriture ; citations vérifiées automatiquement contre le ledger ; la copie publique n'est modifiée que par l'assainissement déclaré dans les extraits. |

---

## 3. Dépendances et indépendance

- E-002 est la source technique primaire centrale pour la découverte et certains détails de mécanisme.
- E-001, E-005, E-010 et E-011 sont des sources institutionnelles distinctes, mais leurs advisories ont été produits dans la même fenêtre de réponse et peuvent reprendre des informations communes.
- E-004, E-006, E-007 et E-012 sont secondaires ou de synthèse ; leur convergence ne doit pas être comptée comme quatre corroborations indépendantes si elles reprennent E-002 ou les mêmes advisories.
- E-008 et E-009 sont des métadonnées de dépôt distinctes et utiles pour la séquence des releases, mais elles ne suffisent pas à établir l’intention de l’auteur du tag.

---

## 4. Contradictions enregistrées

| Contradiction ID | Evidence concernée | Description | Traitement |
|------------------|---------------------|-------------|------------|
| C-001 | E-002, E-006, E-007 | Date d’identification formulée comme 28 mars par Microsoft/Datadog, rapport public d’Andres Freund daté du 29 mars. | Conserver les deux jalons ; ne pas choisir une date unique sans source sur la première observation. |
| C-002 | E-001, E-005, E-011 | Formulation générale de risque contre périmètres Debian/Red Hat principalement non stables ou spécifiques. | Segmenter par distribution, canal, version et build ; ne pas extrapoler. |
| C-003 | E-002, E-007, E-010, E-012 | Nuance entre artefacts présents dans le dépôt et déclencheur/artefacts dans les tarballs. | Décrire les étapes séparément ; une analyse artefact par artefact serait nécessaire pour trancher. |
| C-004 | E-002, E-007, E-010, E-012 | Capacité pré-authentification décrite avec des degrés différents, sans preuve d’exploitation à grande échelle. | Distinguer capacité technique, démonstration et exploitation observée. |
| C-005 | E-004, E-012 | Motivation et identité inconnues, malgré des hypothèses secondaires d’acteur organisé ou étatique. | Conserver l’attribution en hypothèse LOW ; ne pas conclure. |

---

## 5. Contrôles de qualité

- [x] Au moins trois sources publiques utilisées.
- [x] Source primaire technique incluse : E-002.
- [x] Sources officielles incluses : E-001, E-005, E-010, E-011.
- [x] Sources secondaires crédibles incluses : E-006, E-007, E-012.
- [x] Chaque source possède un Evidence ID et un lien.
- [x] Primary / Secondary distingué de Source type.
- [x] Direct observation / Reported / Derived renseigné.
- [x] Timestamp de collecte, timezone et UTC normalisé enregistrés.
- [x] Corroborations et dépendances documentées.
- [x] Reliability et confidence séparées.
- [x] Contradictions conservées.
- [x] Les extraits verbatim sont vérifiés par le ledger de citations.
- [x] Aucune recherche intrusive ou action externe réalisée.
