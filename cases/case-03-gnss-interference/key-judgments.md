# Case 03 — Jugements clés de l'édition documentaire

> **Statut :** approuvés le 1er novembre 2026. Voir le [rapport](report.md) pour le contexte.
>
> *Les mentions « vérifié » et « contre-analyse » de cette édition renvoient à des contrôles effectués par l'auteur. Elles ne valent ni revue indépendante ni validation scientifique.*
>
> Analyse OSINT — non destinée à la navigation.

## Règles appliquées

- Confiance humaine : **Élevée / Modérée / Faible** ; elle porte sur le jugement, pas sur la fiabilité d'une source.
- Chaque jugement cite des identifiants vérifiés : les identifiants cités, localisés dans la [carte des preuves](evidence-map.md).
- Lignées (`origin_dependency_group`) :
  - `ODG-EASA-SIB` (S-001), `ODG-EASA-NIC` (S-002), `ODG-ICAO-SECRETARIAT` (S-004), `ODG-STATES-CWP15745` (S-005 annexe A), `ODG-ICAO-COUNCIL` (S-005 corps) ;
  - `ODG-IATA-FDX` (S-020, S-021), `ODG-BOEING-GEM`, `ODG-PANSA`, `ODG-HUNGAROCONTROL` (S-022), `ODG-ITU-RRB` (S-023).
- **Indépendance de mesure ≠ indépendance de pipeline.** Les indicateurs des États, de l'EASA et d'IATA reposent tous sur des données ADS-B ou des enregistreurs de bord. Seules les campagnes RF des États (EV-037) et les rapports d'équipage relèvent d'autres classes de capteurs.
- Aucune attribution n'est jugée par le projet : elle reste de classe `reported`, conformément aux variables canoniques.

---

## KJ-01 — Une hausse nette jusqu'à mi-2025, une évolution ensuite incertaine

**Jugement.** Les dégradations GNSS touchant l'aviation civile ont nettement augmenté entre 2022 et la mi-2025. Plusieurs lignées distinctes concordent sur le sens de cette évolution. Depuis la mi-2025, l'évolution n'est plus établie : une baisse locale est documentée en Pologne, tandis que les institutions décrivent un phénomène persistant.

| Élément | Valeur | Preuve | Lignée |
|---|---|---|---|
| Hausse déclarée depuis février 2022 | « increase in jamming and/or spoofing » | EV-001, EV-002 | ODG-EASA-SIB |
| Taux de perte GPS pour 1 000 vols (monde) | 28,1 → 30,9 → 39,9 → 56,1 → 60,1 (2021 → S1 2025) | EV-043, EV-044 | ODG-IATA-FDX |
| Événements de perte GPS 2021 → 2024 | +220 % | EV-048 (même lignée qu'EV-043) | ODG-IATA-FDX |
| Part des vols affectés, 6 FIR baltes et nordiques | ~7,5 % (mai 2024) → ~27,4 % (avril 2025) | EV-042 | ODG-STATES-CWP15745 |
| Cas déposés à l'UIT, janv.–sept. 2024 (comptage de signalements, **non discriminant** : compatible avec H2) | plus de cinq fois l'année précédente ; un nombre croissant de cas | EV-064, EV-065 | ODG-ITU-RRB |
| Persistance, 2025 → 2026 | se poursuit sans interruption ; classement EASA au 14/10/2026 | EV-039, EV-060 | ODG-ICAO-COUNCIL, ODG-EASA-NIC |
| Baisse locale après la mi-2025 | EPWW : brouillage au plus haut en juin 2025 (1 940) puis 317 en novembre, remontée à 620 en décembre ; leurrage de 282 (janvier) à 52 (novembre), 95 en décembre | EV-055, EV-056 | ODG-PANSA |
| Baisses localisées antérieures à la mi-2025 (contexte) | Boeing : hausse mondiale des occurrences avec des baisses localisées dans certaines FIR, sur des données de juin 2024 à mai 2025 ; elles ne renseignent pas l'après-mi-2025 | EV-051, EV-070 | ODG-BOEING-GEM |

- **Confiance : Élevée** pour le sens de la tendance 2022 → mi-2025 au niveau mondial (taux IATA normalisés) et dans le foyer balte (part des vols, États, 2024–2025). **Modérée** pour l'Europe prise dans son ensemble : sur 2022–2023, seuls l'affirmation qualitative de l'EASA (EV-001) et le taux mondial IATA portent le jugement. Le comptage UIT n'est pas retenu comme preuve de tendance (KJ-05).
- **Confiance : Faible** pour l'ampleur européenne et pour la période postérieure à la mi-2025. Le taux IATA est mondial ; les dénominateurs diffèrent (GAP-002) ; aucune série européenne homogène 2022–2026 n'est publiée.
- **Limite principale :** aucune série couvrant toute la période du cas (14 février 2022 → 31 juillet 2026) avec un dénominateur constant.
- **Discriminant :** une série européenne publiée par FIR et par mois, normalisée par le trafic, couvrant 2022–2026.
- **Raccourci interdit :** additionner ou comparer directement les chiffres des lignées. Ils n'ont ni la même unité, ni la même population.

## KJ-02 — Deux foyers européens persistants, sans démonstration d'une émergence

**Jugement.** La dégradation se concentre de façon persistante, entre 2024 et octobre 2026, sur deux foyers qui touchent l'espace aérien européen au sens large (États de la CEAC, dont la Turquie) :
- **Baltique et Nord-Est** : EPWW, EYVL, EVRR, EETT, EFIN, ESAA ;
- **mer Noire et Méditerranée orientale** : LTAA, LTBB, LRBB, LBSR, LCCC.

Aucune émergence d'un nouveau foyer européen n'est démontrée par les sources.

- Preuves :
  - zones citées dans le bulletin EASA de juillet 2026 (EV-003) ;
  - les six FIR baltes et nordiques citées par le Conseil de l'OACI en 2025 (EV-029) ;
  - le classement EASA à 30 jours au 14/10/2026 : LTAA 1er, EPWW 2e, LRBB 3e, LBSR 5e, EETT 6e, EYVL 7e, LCCC 9e, LTBB 11e, EFIN 14e, EVRR 16e (EV-059, EV-060) ;
  - Boeing : EFIN est la seule FIR de l'Union dans son top 10 (52 %), derrière LTAA (77 %) (EV-052) ;
  - HungaroControl : les effets sont importés par des vols venant de la mer Noire et de la Baltique orientale (EV-058) ;
  - EASA et IATA : incidents signalés en hausse ces dernières années en Europe de l'Est et au Moyen-Orient (EV-049).
- **Confiance : Élevée** pour la désignation des deux foyers. Trois lignées, avec des méthodes différentes (indicateur NIC, enregistreurs Boeing, déclarations d'États), et trois dates (2025, juillet 2026, octobre 2026).
- **Confiance : Faible** pour le classement fin entre FIR. Le ratio EASA dépend du trafic et de la couverture ADS-B (EV-059) ; un rang ne mesure pas une intensité.
- **Inconclusif (PIR-2) :** l'atlas FIR/H3 et la mesure de persistance propre au projet n'ont pas été produits (choix de périmètre du 30 octobre 2026). L'« émergence » ne peut pas être évaluée sans série datée par FIR.
- **Raccourci interdit :** lire une FIR absente du classement comme épargnée. L'absence de données n'est pas une absence de perturbation.

## KJ-03 — Le signal relève surtout de brouillages et de leurrages réels, amplifiés par une meilleure détection

**Jugement.** Les observations sont incompatibles avec une explication dominée par des artefacts de couverture ou des défauts techniques (H3). Elles sont compatibles avec des interférences réelles, en partie intentionnelles (H1). Une part de la hausse des comptages vient d'une meilleure détection (H2), ce qui oriente vers le modèle mixte H4, avec une composante réelle dominante.

- Discriminants qui écartent H3 :
  - campagnes de mesure radiofréquence au sol et en vol, avec triangulation (EV-037), reprises dans le procès-verbal UIT (EV-063, EV-066) ;
  - signatures de leurrage impossibles à produire par un trou de couverture : 293 vols et plus de 21 000 positions fausses sur une trajectoire circulaire autour de Rostov (EV-032) ;
  - enregistreurs de bord indépendants de la couverture au sol (EV-046, EV-050).
- Éléments qui maintiennent H2 dans le jeu :
  - la population suivie par IATA FDX varie d'une année à l'autre : le graphique superpose des barres de vols enregistrés, dont les valeurs ne sont pas lisibles dans la couche texte ; seul le cumul est publié (24,6 millions de vols d'août 2021 à juin 2025, EV-045) ;
  - la surveillance s'est institutionnalisée (indicateur EASA, EV-059) ;
  - dans la FIR de Budapest, début 2026, les rapports de pilotes ne couvrent que 2,6 à 8,1 % des événements détectés (EV-057) ; tout progrès du signalement gonfle donc les comptes bruts.
- Pourquoi la composante réelle domine : les **taux normalisés** progressent aussi (EV-043, EV-042), ce qu'un simple effet de détection n'explique pas.
- **Confiance : Élevée** pour le rejet de H3 comme explication principale. **Modérée** pour la part relative de H1 et de H2 : elle n'est pas quantifiable avec les sources publiques.
- **Attribution (rapportée, non jugée) :**
  - le Comité du Règlement des radiocommunications de l'UIT, statuant notamment sur un document des administrations d'Estonie, de Lettonie et de Lituanie (EV-069), écrit que des mesures ont géolocalisé la source des brouillages sur le territoire de la Fédération de Russie (EV-063) ;
  - le Conseil de l'OACI qualifie la situation d'infraction à la Convention de Chicago (EV-034) ;
  - PANSA désigne la Fédération de Russie et le Bélarus comme principales sources et signale aussi des interférences internes, civiles et militaires (EV-068, EV-054) ;
  - IATA désigne les entités militaires comme principales sources des interférences délibérées et invalidantes (EV-047).

  Le projet ne dispose d'aucune mesure propre et ne requalifie pas ces attributions.
- **Raccourci interdit :** tirer une attribution de la géométrie des zones affectées, ou faire d'une observation ADS-B une mesure radiofréquence.

## KJ-04 — Des conséquences opérationnelles réelles, de nature documentée mais de fréquence non mesurée

**Jugement.** Les sources institutionnelles documentent des conséquences opérationnelles concrètes.

Effets rapportés comme observés :
- déroutements et diversions, écarts aux clairances ATC (EV-007) ;
- fausses alertes TAWS « PULL UP » ayant conduit à des montées non coordonnées (EV-008) ;
- effets importés par des vols venant des zones affectées, dont des positions erronées (EV-058).

Effets décrits comme possibles par les institutions :
- surveillance ADS-B corrompue (EV-009) ;
- positions erronées après la sortie de la zone affectée (EV-010, EV-038) ;
- charge accrue des contrôleurs (EV-021).

Leur fréquence et leur gravité ne sont pas mesurables à partir des sources publiques. L'EASA ne considère pas, à ce stade, qu'il s'agisse d'une condition dangereuse justifiant une directive (EV-012).

- **Confiance : Élevée** pour l'existence et la nature de ces conséquences : bulletin EASA et papiers de l'OACI concordants, avec des retours de prestataires de navigation aérienne (S-022).
- **Confiance : Faible** pour toute quantification. Les comptes de « vols affectés » (EV-031 : 23 438 à 41 282 vols par mois, janvier–avril 2025) reposent sur une définition non publiée de « affected » (GAP-002) et ne mesurent pas une conséquence.
- **Inconclusif (PIR-4) :** la comparaison événement / référence / témoin sur des fenêtres fixées indépendamment n'a pas été réalisée (choix de périmètre du 30 octobre 2026 ; GAP-005 et GAP-011 sont sans objet pour cette édition et restent ouvertes pour une phase d'observation).

## KJ-05 — Les comptages bruts ne sont pas des indicateurs de veille ; les taux normalisés et l'indicateur EASA le sont, avec garde-fous

**Jugement.** Pour une organisation civile, les comptages bruts d'incidents ne peuvent pas servir à mesurer une tendance :
- ils sous-estiment massivement les événements : 2,6 à 8,1 % de déclaration par les pilotes dans la FIR de Budapest début 2026 (EV-057), sans mesure équivalente publiée ailleurs ;
- ils dépendent de codes NOTAM non harmonisés, 18 codes différents (EV-022) ;
- leurs dénominateurs varient d'une source à l'autre.

Les indicateurs utilisables sont les taux normalisés (par 1 000 vols, part des vols ou des aéronefs) et l'indicateur EASA par FIR moyenné sur 7 et 30 jours, à condition d'en afficher les biais : couverture ADS-B, trafic, seuil NIC < 7 (EV-059, EV-061).

- **Confiance : Élevée** pour l'inadéquation des comptages bruts. **Modérée** pour la liste d'indicateurs, qui n'a pas été testée sur une série propre.
- **Inconclusif (PIR-5) :** la part de la tendance attribuable à la couverture, au trafic ou aux jours incomplets n'est pas quantifiée par le projet.

---

## Couverture des PIR

| PIR | Réponse | État |
|---|---|---|
| PIR-1 Évolution | KJ-01 | répondu (sens) ; ampleur européenne inconclusive |
| PIR-2 Géographie | KJ-02 | répondu (foyers persistants) ; émergence et atlas inconclusifs |
| PIR-3 Nature | KJ-03 | répondu (compatibilité qualitative, H4 à dominante H1) |
| PIR-4 Conséquences | KJ-04 | répondu (nature) ; fréquence et comparaison témoin inconclusives |
| PIR-5 Biais | KJ-03, KJ-05 | partiellement répondu (biais de déclaration chiffré) ; décomposition inconclusive |
| PIR-6 Veille | KJ-05 | répondu (indicateurs et garde-fous) |

