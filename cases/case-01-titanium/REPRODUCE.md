# Recalculer les résultats Titane

**Question :** comment les masses importées deviennent-elles un indicateur de concentration ? Le programme ci-dessous recalcule les douze comparaisons du rapport : six produits, en 2017 et en 2025. Il fonctionne sans accès au dépôt privé, sans dépendance Python et sans connexion réseau.

Depuis la racine du dépôt public, avec Python 3.11 ou plus récent :

```bash
python tools/reproduce_results.py titanium
```

`PASS` signifie que les calculs retrouvent les valeurs publiées : HHI, part du premier partenaire, couverture et bornes. Une incohérence arrête le programme. Cela vérifie le calcul sur ce snapshot ; cela ne valide pas les jugements industriels.

## Données et provenance

- [reproduction_masses.csv](data/reproduction_masses.csv) : 431 lignes issues du snapshot normalisé Eurostat/Comext DS-045409. UE27, importations extra-UE, six CN8, années complètes 2017 et 2025, masse nette en unités de 100 kg. Les valeurs en euros et les autres années ne sont pas exportées dans ce parcours.
- [Manifest](data/reproduction_manifest.json) : périmètre, attribution et empreinte du fichier d’entrée.
- [uncertainty.csv](data/uncertainty.csv) : résultats attendus de couverture et de bornes pour les douze comparaisons.
- [key_metrics.csv](data/key_metrics.csv) : résultats du rapport, comparés au recalcul.

**Attribution :** Source Eurostat, DS-045409, accès le 26 juillet 2026 ; filtrage et classification réalisés par ce projet. [Conditions de réutilisation Eurostat](https://ec.europa.eu/eurostat/help/copyright-notice). Les classifications et calculs du projet ne sont pas une validation par Eurostat.

Il s’agit d’un **snapshot historique**, pas d’une extraction actualisée. Une nouvelle requête Eurostat peut renvoyer des valeurs révisées. La reproduction commence à la table normalisée publiée ; elle ne reconstitue pas l’intégralité de l’acquisition initiale ni les analyses industrielles.

## Dictionnaire

| Champ | Sens |
|---|---|
| `year` | année complète, 2017 ou 2025 |
| `cn8` | code douanier du produit, conservé comme texte |
| `partner` | code d’origine ou code technique Eurostat |
| `role` | `identified` : origine individuelle retenue ; `unidentified` : code sans pays attribuable ; `total` : total extra-UE publié |
| `net_mass_100kg` | masse déclarée, en centaines de kilogrammes ; cellule vide = absente, pas zéro |

La sélection des pays et codes techniques est figée dans `role`. Les agrégats géographiques sont exclus pour éviter de compter deux fois les mêmes flux. Une origine douanière n’identifie pas nécessairement le producteur ou un fournisseur qualifié.

## Exemple : barres, 2017 — C1-PUB-001

1. Additionner les masses des origines identifiées : leur couverture représente **97,77 %** de la masse publiée. La part sans pays attribuable est **2,23 %**.
2. Diviser chaque masse identifiée par la somme des masses identifiées, puis multiplier par 100. La somme des carrés de ces parts donne **2 991,9** : le HHI renormalisé sur les origines identifiées.
3. Pour exprimer des limites sur **le total**, prendre `u = 2,23` points et multiplier chaque part renormalisée par `1 − u/100`. La somme de leurs carrés donne **2 860,0**.
4. La borne supérieure affecte toute la part inconnue à la plus grande origine connue : `borne basse + 2 × u × plus grande part sur le total + u²`, soit **3 060,3**. La borne basse décrit une dispersion limite de l’inconnu, pas une répartition observée.

La méthode historique arrondit `u` à 0,001 point de pourcentage avant le calcul des bornes ; les HHI sont affichés à une décimale. La couverture et les bornes ne sont pas un intervalle de confiance statistique. Le HHI renormalisé et l’enveloppe n’ont pas le même dénominateur.

**Conclusion limitée :** l’indicateur décrit la concentration commerciale. Il ne donne ni la probabilité d’une rupture ni la qualification d’une matière pour l’aéronautique. Retrouver les [affirmations et leurs preuves](evidence-map.md) `C1-PUB-001` à `C1-PUB-004`, puis leurs limites industrielles `C1-PUB-005` à `C1-PUB-008`.
