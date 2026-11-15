# Recompter les domaines et le graphe Portal Kombat

Ce parcours permet de retrouver des résultats du rapport depuis **deux fichiers VIGINUM réels**, à un commit précis. Il ne recopie aucun corpus tiers dans ce dépôt et ne visite aucun domaine du réseau étudié.

Depuis la racine du dépôt public, avec Python 3.11 ou plus récent :

```bash
python tools/reproduce_results.py portal
```

Le programme consulte uniquement les deux URL GitHub du [manifest](data/reproduction_sources.json), vérifie la taille et l’empreinte SHA-256 de chaque réponse puis calcule les résultats en mémoire. Aucune donnée brute n’est enregistrée par cette commande. Si une source disparaît ou change, la vérification échoue au lieu de produire un nouveau résultat sous l’ancienne référence. Les droits des sources restent ceux de leurs auteurs ; l’accès public n’autorise pas leur redistribution.

Pour travailler hors réseau avec des fichiers déjà obtenus dans un cadre autorisé, placer les octets inchangés dans un répertoire extérieur au dépôt, sous les noms `S-008.bin` et `S-031.bin` :

```bash
python tools/reproduce_results.py portal --local-files /chemin/exterieur
```

## Du fichier au résultat

- **C2-PUB-001 :** le CSV contient 371 observations ; normaliser les noms en minuscules, retirer les espaces en bord et remplacer `[.]` par `.` donne 370 domaines distincts. La colonne source `create date`, au format jour/mois/année, fournit 232 dates et 139 absences. Elle ne prouve pas une première publication indépendante.
- **C2-PUB-002 :** convertir ces dates sans les imputer donne 31 observations datées de mars 2024. Ce recomptage utilise le même export que VIGINUM : il ne constitue pas une corroboration indépendante.
- **C2-PUB-003 :** les objets STIX hors `relationship` deviennent les 609 nœuds ; les 1 013 relations deviennent les liens. Pour calculer les composantes, les liens sont traités comme non orientés. Les nœuds isolés restent comptés. Le plus grand ensemble connecté contient 604 nœuds.
- **C2-PUB-004 :** retirer les liens attachés aux nœuds `campaign`, tout en gardant les 609 nœuds, laisse 703 liens et une composante de 602 nœuds. Retirer les relations `amplifies` donne une composante de 305 nœuds ; retirer `uses` en donne 560.

Le résultat est comparé à la [table des métriques](data/key_metrics.csv), également utilisée par les figures. `PASS` confirme l’accord du recomptage avec cette table pour ces mesures.

**Limite :** le graphe représente les choix de modélisation de la source. Sa connectivité ne démontre ni un commandement réel ni une audience. Les mesures Wikipedia, X et CheckFirst restent des agrégats historiques publiés : cette commande ne les recalcule pas. Le programme ne reproduit donc pas l’intégralité des résultats du dossier.

Les [sources](sources.md), la [carte des preuves](evidence-map.md) et la [provenance](provenance.csv) permettent de retrouver les publications et leurs dépendances. Les tests logiciels utilisent de petits exemples synthétiques étiquetés ; les résultats du rapport reposent sur les données réelles décrites ici.
