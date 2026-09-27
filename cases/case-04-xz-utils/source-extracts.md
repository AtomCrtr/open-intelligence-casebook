# XZ Utils — Extraits de sources collectées

> Extraits verbatim collectés le 2026-08-21 (lecture seule, aucune interaction avec les systèmes décrits). Les citations doivent être vérifiées contre les pages originales.
>
> **Assainissement de l'édition publique :** dans S-008 et S-009, l'image d'avatar et le lien relatif du compte ont été retirés ; seul le pseudonyme affiché et l'horodatage sont conservés. Aucun autre extrait n'est modifié.

## S-001 / CISA

URL: https://www.cisa.gov/news-events/alerts/2024/03/29/reported-supply-chain-compromise-affecting-xz-utils-data-compression-library-cve-2024-3094

> CISA and the open source community are responding to reports of malicious code being embedded in XZ Utils versions 5.6.0 and 5.6.1. This activity was assigned CVE-2024-3094.

## S-002 / Openwall oss-security — Andres Freund

URL: https://www.openwall.com/lists/oss-security/2024/03/29/4

> After observing a few odd symptoms around liblzma (part of the xz package) on Debian sid installations over the last weeks (logins with ssh taking a lot of CPU, valgrind errors) I figured out the answer:

> The upstream xz repository and the xz tarballs have been backdoored.

## S-003 / XZ Utils maintainer page

URL: https://tukaani.org/xz-backdoor/

> XZ Utils 5.6.0 and 5.6.1 release tarballs contain a backdoor.

## S-004 / OpenSSF

URL: https://openssf.org/blog/2024/03/30/xz-backdoor-cve-2024-3094/

> While the motivation behind this backdoor remains unknown, the intent was to compromise specific distributions, as the backdoors were only applied to DEB or RPM packages for the x86-64 architecture built with gcc and the gnu linker.

## S-005 / Debian DSA-5649-1

URL: https://www.debian.org/security/dsa-5649-1

> Right now no Debian stable versions are known to be affected.

## S-006 / Microsoft

URL: https://techcommunity.microsoft.com/blog/vulnerability-management/microsoft-faq-and-guidance-for-xz-utils-backdoor/4101961

> On March 28, 2024 a backdoor was identified in XZ Utils.

## S-007 / Datadog Security Labs

URL: https://securitylabs.datadoghq.com/articles/xz-backdoor-cve-2024-3094/

> When a malicious version of the `xz-utils` library is installed, a malicious shared object (SO) file is stored on disk.

## S-008 / GitHub release v5.6.0

URL: https://github.com/tukaani-project/xz/releases/tag/v5.6.0

> JiaT75 tagged this 24 Feb 08:22

## S-009 / GitHub release v5.6.1

URL: https://github.com/tukaani-project/xz/releases/tag/v5.6.1

> JiaT75 tagged this 09 Mar 08:16

## S-010 / CERT-EU Advisory 2024-032

URL: https://cert.europa.eu/publications/security-advisories/2024-032/pdf

> On March 29, several companies issued a warning regarding a backdoor found in the XZ Utils software.

## S-011 / Red Hat advisory

URL: https://www.redhat.com/en/blog/urgent-security-alert-fedora-41-and-rawhide-users

> No versions of Red Hat Enterprise Linux (RHEL) are affected by this CVE.

## S-012 / Ars Technica

URL: https://arstechnica.com/security/2024/04/what-we-know-about-the-xz-utils-backdoor-that-almost-infected-the-world/

> At the moment, it’s unknown if there was ever a real-world person behind this username or if Jia Tan is a completely fabricated individual.
