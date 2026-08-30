# Contrôle de publication — édition publique v1

**Statut : PASS après génération reproductible sur la branche `main`.**

## Périmètre et confidentialité

- [x] Historique Git du dépôt canonique privé non copié.
- [x] Aucun secret, jeton, fichier `.env`, chemin local ou nom de machine dans le package publié.
- [x] Aucune donnée brute tierce aux droits incertains n’est redistribuée.
- [x] Case 03 reste un teaser : aucune trajectoire, aucun identifiant avion et aucune conclusion GNSS historique.

## Intégrité analytique

- [x] Case 01 conserve la séparation commerce ≠ aéronautique ≠ qualification ≠ substitution.
- [x] Case 02 conserve la séparation visibilité ≠ coordination ≠ attribution ≠ impact.
- [x] Les chiffres publiés proviennent des résultats validés et des dérivations documentées.
- [x] Les niveaux de confiance et les limites restent visibles.

## Droits et transparence

- [x] Code original : Apache-2.0 ; contenu analytique original : CC BY 4.0.
- [x] Matériaux tiers non relicenciés ; sources amont incertaines traitées en `link-only` / `derived-only`.
- [x] `NOTICE.md`, `DISCLAIMER.md` et `AI_TRANSPARENCY.md` accessibles depuis le README.

## Qualité technique

- [x] Figures SVG valides.
- [x] PDF A4, texte sélectionnable, métadonnées assainies et liens web publics.
- [x] Aucun lien `file://` dans les PDF.
- [x] Checksums SHA-256 générés pour les PDF, figures et tables dérivées.
- [x] Construction automatisée et reproductible depuis `tools/build_publication.py`.

```text
RELEASE READINESS: PASS
```
