# Contrôle de publication — édition publique

**Statut : PASS.** Fichier généré par `tools/build_publication.py` à la fin d'une construction réussie. La première section ne rapporte que des contrôles exécutés par le générateur ; la seconde liste des engagements vérifiés par revue humaine, que le générateur ne contrôle pas.

## Contrôles automatiques

- [x] Traçabilité de chaque cas (`tools/check_case.py`) : `case-01-titanium`, `case-02-portal-kombat`, `case-03-gnss-interference`, `case-04-xz-utils` — aucun problème.
- [x] Provenance publique : Case 01 : 8 affirmations ; Case 02 : 8 ; Case 03 : 12 ; Case 04 : 13 (minimum 8 par cas, lignée informationnelle renseignée).
- [x] Case 02 : étude commune DFRLab / CheckFirst déclarée comme une seule lignée ; source S-029 bornée à C2-PUB-008.
- [x] Case 04 : aucune URL d'avatar ni section interne d'évaluation dans les fichiers publiés.
- [x] Figures SVG : 12 fichiers analysés sans erreur.
- [x] PDF : Case 01 (23 pages, 12 liens web), Case 02 (22 pages, 19 liens web), Case 03 (12 pages, 19 liens web), Case 04 (27 pages, 32 liens web), guide de lecture (6 pages, 9 liens web) ; format A4, texte sélectionnable, titre conforme, aucun lien `file://` ni lien vers un fichier local.
- [x] Recherche de motifs interdits (`/mnt/data/`, `C:\Users\`, `file://`, `private-user-images.githubusercontent.com`) dans 40 fichiers publics : aucune occurrence.
- [x] Empreintes SHA-256 : 24 fichiers générés vérifiés (`checksums.sha256`).

## Engagements vérifiés par revue humaine (non contrôlés par le générateur)

- Historique Git du dépôt canonique privé non copié.
- Aucune donnée brute tierce aux droits incertains n'est redistribuée ; voir la [revue des droits](rights-review.md).
- Case 01 : séparation commerce ≠ aéronautique ≠ qualification ≠ substitution.
- Case 02 : séparation visibilité ≠ coordination ≠ attribution ≠ impact.
- Case 03 : évaluation documentaire ; aucune trajectoire, aucun identifiant avion, aucune donnée GPSJAM ; citations OACI, IATA, UIT et intervenants de l'atelier paraphrasées.
- Case 04 : instruit dans un espace de travail distinct, publié sous forme assainie (écarts documentés en tête du rapport) ; aucune tentative d'identification des personnes derrière les pseudonymes.
- Licences : code original Apache-2.0 ; contenu analytique original CC BY 4.0 ; matériaux tiers non relicenciés.
- `NOTICE.md`, `DISCLAIMER.md` et `AI_TRANSPARENCY.md` accessibles depuis le README.

```text
RELEASE READINESS: PASS
```
