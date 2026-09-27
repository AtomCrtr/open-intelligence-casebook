# Sources - Case 04

Toutes les sources sont publiques et **link-only** : ce dépôt ne republie que de courts extraits (voir [`source-extracts.md`](source-extracts.md)), vérifiables contre [`citations-ledger.json`](citations-ledger.json). Pages consultées le **2026-08-21**, en lecture seule. L'évaluation détaillée figure dans la section *Source assessment* du [rapport](report.md).

| Réf. | ID | Source | Type | Fiabilité | Lien |
|---|---|---|---|---|---|
| [1] | S-001 | CISA | advisory gouvernemental | HIGH | [lien](https://www.cisa.gov/news-events/alerts/2024/03/29/reported-supply-chain-compromise-affecting-xz-utils-data-compression-library-cve-2024-3094) |
| [2] | S-002 | Openwall oss-security — Andres Freund | rapport technique primaire | HIGH | [lien](https://www.openwall.com/lists/oss-security/2024/03/29/4) |
| [3] | S-003 | XZ Utils maintainer page | déclaration officielle du projet | MEDIUM-HIGH | [lien](https://tukaani.org/xz-backdoor) |
| [4] | S-004 | OpenSSF | synthèse d'experts | MEDIUM-HIGH | [lien](https://openssf.org/blog/2024/03/30/xz-backdoor-cve-2024-3094) |
| [5] | S-005 | Debian DSA-5649-1 | advisory de distribution | HIGH | [lien](https://www.debian.org/security/dsa-5649-1) |
| [6] | S-006 | Microsoft | guidance fournisseur | HIGH (recommandations) / MEDIUM (impact global) | [lien](https://techcommunity.microsoft.com/blog/vulnerability-management/microsoft-faq-and-guidance-for-xz-utils-backdoor/4101961) |
| [7] | S-007 | Datadog Security Labs | analyse fournisseur de sécurité | MEDIUM-HIGH | [lien](https://securitylabs.datadoghq.com/articles/xz-backdoor-cve-2024-3094) |
| [8] | S-008 | GitHub release v5.6.0 | métadonnées de dépôt | HIGH (tags affichés) | [lien](https://github.com/tukaani-project/xz/releases/tag/v5.6.0) |
| [9] | S-009 | GitHub release v5.6.1 | métadonnées de dépôt | HIGH (tags affichés) | [lien](https://github.com/tukaani-project/xz/releases/tag/v5.6.1) |
| [10] | S-010 | CERT-EU Advisory 2024-032 | advisory institutionnel européen | HIGH (publication) / MEDIUM-HIGH (détails) | [lien](https://cert.europa.eu/publications/security-advisories/2024-032/pdf) |
| [11] | S-011 | Red Hat advisory | advisory fournisseur / distribution | HIGH | [lien](https://www.redhat.com/en/blog/urgent-security-alert-fedora-41-and-rawhide-users) |
| [12] | S-012 | Ars Technica | journalisme technique | MEDIUM | [lien](https://arstechnica.com/security/2024/04/what-we-know-about-the-xz-utils-backdoor-that-almost-infected-the-world) |

## Dépendances à garder en tête

- **S-002** (rapport d'Andres Freund sur oss-security) est la source technique primaire de la découverte ; plusieurs synthèses la reprennent.
- **S-004, S-006, S-007, S-012** sont secondaires ou de synthèse : leur convergence ne vaut pas quatre corroborations indépendantes.
- **S-001, S-005, S-010, S-011** sont institutionnelles et distinctes, mais publiées dans la même fenêtre de réponse.
- **S-008 / S-009** établissent la séquence des releases, pas l'intention de l'auteur des tags.

Les contenus tiers restent soumis à leurs conditions d'origine (voir [NOTICE](../../NOTICE.md)).
