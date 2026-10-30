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

---

## Collecte complémentaire du 2026-10-30

> Extraits verbatim collectés le 2026-10-30 par extraction de pages publiques (service d'extraction tiers, lecture seule). La mise en forme Markdown (gras, liens) des pages est retirée ; le texte est conservé mot pour mot. Aucune clé, commande ou charge utile n'est reproduite.

## S-011 / Red Hat — citations ajoutées

URL consultée : https://www.redhat.com/en/blog/urgent-security-alert-fedora-41-and-rawhide-users (redirige le 2026-10-30 vers `…/urgent-security-alert-fedora-40-and-rawhide-users`, titre « Urgent security alert for Fedora Linux 40 and Fedora Rawhide users »).

> The malicious injection present in the xz versions 5.6.0 and 5.6.1 libraries is obfuscated and only included in full in the download package - the Git distribution lacks the M4 macro that triggers the build of the malicious code.

> The second-stage artifacts are present in the Git repository for the injection during the build time, in case the malicious M4 macro is present.

> We have determined that Fedora Linux 40 beta does contain two affected versions of xz libraries

> At this time the Fedora Linux 40 builds have not been shown to be compromised.

> We have reports and evidence of the injections successfully building in xz 5.6.x versions built for Debian unstable (Sid).

> Fedora Rawhide users may have received version 5.6.0 or 5.6.1.

## S-013 / Russ Cox — chronologie

URL: https://research.swtch.com/xz-timeline

> Over a period of over two years, an attacker using the name “Jia Tan” worked as a diligent, effective contributor to the xz compression library, eventually being granted commit access and maintainership.

> 2021-10-29: Jia Tan sends first, innocuous patch to the xz-devel mailing list, adding “.editorconfig” file.

> Brian Krebs observes that many of these email addresses never appeared elsewhere on the internet, even in data breaches (nor again in xz-devel). It seems likely that they were fakes created to push Lasse to give Jia more control.

> At this point we know they have commit access.

> 2023-03-18: Jia Tan tags and builds their first release, v5.4.2.

> 2024-02-23: Jia Tan merges hidden backdoor binary code well hidden inside some binary test input files.

> This m4 file is not present in the source repository, but many other legitimate ones are added during package as well, so it’s not suspicious by itself.

> 2024-03-28: Andres Freund discovers bug, privately notifies Debian and distros@openwall. RedHat assigns CVE-2024-3094.

> (Note that this does not include systems like Arch Linux, Gentoo, and NixOS, which do not patch sshd.)

> a part of xz that also happens to be a dependency of OpenSSH sshd on Debian, Ubuntu, and Fedora, and other systemd-based Linux systems that patched sshd to link libsystemd.

## S-014 / NIST NVD

URL: https://nvd.nist.gov/vuln/detail/CVE-2024-3094

> Malicious code was discovered in the upstream tarballs of xz, starting with version 5.6.0.

> Through a series of complex obfuscations, the liblzma build process extracts a prebuilt object file from a disguised test file existing in the source code, which is then used to modify specific functions in the liblzma code.

> Base Score: 10 CRITICAL

> CNA: Red Hat, Inc.

## S-015 / xzbot (Anthony Weems)

URL: https://github.com/amlweems/xzbot

> The backdoor uses a hardcoded ED448 public key for signature validation and decrypting the payload.

> This payload must be encrypted and signed with the attacker's ED448 key.

> Note: successful exploitation does not generate any INFO or higher log entries.

## S-016 / Arch Linux

URL: https://archlinux.org/news/the-xz-package-has-been-backdoored/

> To our knowledge the malicious code which was distributed via the release tarball never made it into the Arch Linux provided binaries, as the build script was configured to only inject the bad code in Debian/Fedora based package build environments.

> Arch does not directly link openssh to liblzma, and thus this attack vector is not possible.

> The `xz` packages prior to version `5.6.1-2` (specifically `5.6.0-1` and `5.6.1-1`) contain this backdoor.

## S-017 / openSUSE

URL: https://news.opensuse.org/2024/03/29/xz-backdoor/

> Our rolling release distribution openSUSE Tumbleweed and openSUSE MicroOS included this version between March 7 and March 28.

> It has been established that the malicious file introduced into Tumbleweed is not present in SUSE Linux Enterprise and/or openSUSE Leap.

> Current research indicates that the backdoor is active in the SSH Daemon, allowing malicious actors to access systems where SSH is exposed to the internet.

> As of March 29, reverse engineering of the backdoor is still ongoing.
