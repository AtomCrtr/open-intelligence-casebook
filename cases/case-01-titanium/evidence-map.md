# Carte publique affirmation-preuve - Case 01

Cette carte rend visible la chaîne **affirmation -> preuve -> confiance -> limite** sans republier les registres internes ni les corpus tiers du dépôt canonique. Elle complète le [rapport public](report.md), la [liste des sources](sources.md) et la [table de provenance publique](provenance.csv), qui distingue éditeur et lignée informationnelle.

| ID | Affirmation publique | Type de preuve | Sources / artefacts publics | Confiance | Limite déterminante |
|---|---|---|---|---|---|
| C1-PUB-001 | La concentration commerciale évolue différemment selon les six formes de titane. | mesure dérivée reproductible | [Eurostat / Comext](sources.md), [métriques CN8](data/key_metrics.csv), [figure HHI](figures/hhi_2017_2025.svg) | élevée pour la mesure commerciale | flux toutes industries, pas exposition aéronautique directe |
| C1-PUB-002 | Les tubes se concentrent fortement entre 2017 et 2025 : HHI 2 130,6 -> 4 137,9 ; Chine 60,23 % du premier partenaire en 2025. | mesure dérivée reproductible | [métriques CN8](data/key_metrics.csv), Eurostat | élevée | origine douanière != producteur réel != fournisseur qualifié |
| C1-PUB-003 | Les déchets et chutes montrent au contraire une baisse de concentration : HHI 2 568,5 -> 1 449,4. | mesure dérivée reproductible | [métriques CN8](data/key_metrics.csv), Eurostat | élevée | ne prouve pas une boucle fermée aéronautique ni une substitution |
| C1-PUB-004 | Un changement de premier partenaire ne signifie pas automatiquement une diversification structurelle. | inférence bornée par la mesure | formes brutes/poudres : États-Unis -> Kazakhstan avec HHI quasi stable ; [figure partenaires](figures/dominant_partner.svg) | modérée | les catégories CN8 agrègent plusieurs produits et usages |
| C1-PUB-005 | Une capacité industrielle nouvelle ne devient pas automatiquement une source aéronautique substituable. | triangulation industrielle + règle analytique | BEI/ECOTITANIUM, Osaka Titanium, SEC/IperionX ; [portes de qualification](figures/qualification_gates.svg) | modérée | qualification, approbation client, contrat et livraison restent moins observables |
| C1-PUB-006 | H1, H3 et H4 sont partiellement soutenues ; H2 reste non concluante. | ACH / hypothèses concurrentes | [rapport §7](report.md), [figure hypothèses](figures/hypotheses.svg) | faible à modérée selon l'hypothèse | le corpus ne reconstruit pas toute la chaîne mondiale qualifiée maillon par maillon |
| C1-PUB-007 | Trois scénarios 2030 servent à tester la robustesse des options, sans probabilité implicite. | scénarios exploratoires | [rapport §9](report.md), [figure scénarios](figures/scenarios_2030.svg) | modérée sur la logique, aucune probabilité attribuée | scénarios sensibles aux capacités, qualifications, demande et données internes futures |
| C1-PUB-008 | Les recommandations doivent rester conditionnelles et ne peuvent pas dimensionner seules une décision réelle de stock, sourcing ou investissement. | synthèse décisionnelle | [rapport §12-13](report.md), cadre de veille et données internes requises | modérée | consommation, criticité, délais, contrats, approbations et coûts réels ne sont pas publics |

## Règle de lecture

Une affirmation n'est renforcée que par une preuve portant sur le **même objet et le même périmètre**. Une capacité physique ne transfère pas sa preuve à la qualification ; une qualification ne transfère pas sa preuve à l'approbation client ; une baisse de HHI ne transfère pas sa preuve à la résilience aéronautique.

## Vérifier un résultat

Le [parcours de reproduction](REPRODUCE.md) explique les entrées, le calcul et sa limite. Les identifiants ci-dessus correspondent exactement à ceux de `provenance.csv` ; ils ne dépendent pas de la position des lignes.
