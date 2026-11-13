# Case 03 — Interférences GNSS et aviation civile européenne

## Avant de commencer

**La question en langage courant.** Que peut-on savoir sur les perturbations de navigation par satellite qui touchent l'aviation civile, à partir des documents accessibles ?

**L'idée à retenir.** Les sources documentent des perturbations réelles et des conséquences opérationnelles. Elles ne fournissent pas une mesure homogène de tous les événements européens ni de leurs conséquences.

**Ce qui a été fait.** Le dossier compare des publications institutionnelles et sectorielles, examine leurs dépendances et confronte plusieurs explications. Le projet n'a pas exécuté la couche d'observation ADS-B/GPSJAM prévue au départ.

**Statut.** Étude documentaire finalisée et publiée. Une étude fondée sur de nouvelles observations constituerait une phase distincte.

### Les mots utiles

- **GNSS** : ensemble des systèmes de navigation par satellite, dont le GPS fait partie.
- **Brouillage** : perturbation du signal qui gêne sa réception.
- **Leurrage** : émission de signaux trompeurs susceptibles d'induire une position ou une heure erronée.
- **FIR** : zone géographique d'information de vol ; elle sert ici à situer certaines observations rapportées.
- **ADS-B** : messages émis par les avions, contenant notamment des informations de position ; ils ne sont pas des mesures radiofréquence du brouillage.
- **Taux normalisé** : nombre d'événements rapporté à une base comparable, par exemple un volume de trafic défini.

**Pour lire les chiffres.** Davantage de signalements peut refléter davantage d'événements, une meilleure détection ou les deux. Les périodes et zones ne sont comparables que si l'on comprend comment les données ont été produites.

**Parcours.** Lire « En cinq minutes », puis les limites et les recommandations. La [carte des preuves](evidence-map.md) et les [sources](sources.md) permettent d'approfondir. La présentation a été clarifiée le 13 novembre 2026 ; les jugements et leurs niveaux de confiance restent ceux de l'édition approuvée.

## Rapport final — édition documentaire

> **Analyse OSINT — non destinée à la navigation.**
>
> **Statut :** version 1.0 du 1er novembre 2026, jugements clés approuvés le 1er novembre 2026 ; errata du 6 novembre 2026 issus d'une contre-relecture.
>
> *Les mentions « vérifié » et « contre-analyse » de cette édition renvoient à des contrôles effectués par l'auteur. Elles ne valent ni revue indépendante ni validation scientifique.*

| Champ | Valeur |
|---|---|
| Version | 1.0 — 2026-11-01 (rédaction 2026-10-30 ; jugements approuvés le 2026-11-01) |
| Mode | évaluation documentaire multi-sources (périmètre fixé le 30 octobre 2026) |
| Question | Comment les données ouvertes peuvent-elles aider à suivre et caractériser les dégradations de navigation touchant l'aviation civile européenne depuis 2022, sans confondre corrélation, couverture des capteurs et causalité ? |
| Période | 14 février 2022 → 31 juillet 2026 ; sources lues jusqu'au 30 octobre 2026 |
| Audience | Organisation civile qui doit surveiller et expliquer le phénomène (sécurité des vols, gestion des risques, veille) |
| Corpus | 8 sources, 10 lignées, 67 extraits vérifiés (détail §4) |
| Jugements | [5 jugements clés](key-judgments.md) |
| Contre-analyse | conduite par l'auteur avant l'approbation des jugements (non publiée) |

---

## 1. En cinq minutes

**Réponse courte.** Les sources ouvertes suffisent à établir **que** les dégradations GNSS ont fortement augmenté entre 2022 et la mi-2025, **où** elles se concentrent en Europe, et **de quelle nature** elles relèvent : des brouillages et des leurrages réels. Elles ne suffisent pas à **mesurer** l'ampleur européenne, la fréquence des conséquences ni l'évolution récente avec un dénominateur homogène. Les comptages bruts d'incidents sont trompeurs ; seuls des taux normalisés sont utilisables pour la veille.

| # | Jugement clé | Confiance |
|---|---|---|
| KJ-01 | Hausse nette des dégradations GNSS de 2022 à la mi-2025 ; évolution postérieure incertaine (persistance déclarée, baisses locales). | **Élevée** (sens : monde, foyer balte) · Modérée (Europe entière) · Faible (ampleur, après mi-2025) |
| KJ-02 | Deux foyers européens (CEAC, Turquie comprise) persistants de 2024 à octobre 2026 : Baltique et Nord-Est (EPWW, EYVL, EVRR, EETT, EFIN, ESAA) ; mer Noire et Méditerranée orientale (LTAA, LTBB, LRBB, LBSR, LCCC). Pas d'émergence démontrée. | **Élevée** (foyers) · Faible (classement fin) |
| KJ-03 | Le signal relève surtout d'interférences réelles, en partie intentionnelles, amplifiées par une meilleure détection : modèle mixte H4 à dominante H1 ; l'hypothèse « artefacts » (H3) est écartée comme explication principale. | **Élevée** (rejet de H3) · Modérée (part H1 / H2) |
| KJ-04 | Conséquences opérationnelles réelles et documentées (déroutements, fausses alertes TAWS, positions erronées après la sortie de zone) ; fréquence et gravité non mesurables. | **Élevée** (nature) · Faible (fréquence) |
| KJ-05 | Les comptages bruts ne sont pas des indicateurs de tendance (à Budapest, 2,6 à 8,1 % des événements déclarés par les pilotes) ; les taux normalisés et l'indicateur EASA par FIR le sont, avec garde-fous. | **Élevée** · Modérée (liste d'indicateurs) |

**Ce que le rapport n'établit pas :** une série européenne 2022–2026 ; un atlas FIR/H3 ; une comparaison avec des zones témoins ; une fréquence de conséquences ; une attribution propre au projet. Les attributions citées (UIT, Conseil de l'OACI, PANSA, IATA) sont **rapportées**, jamais requalifiées.

**Recommandations (détail §8) :**
- **REC-01** — suivre des taux normalisés, jamais des comptages bruts ;
- **REC-02** — traiter les effets comme pouvant persister après la sortie de zone ;
- **REC-03** — rendre le dénominateur obligatoire dans tout chiffre transmis ;
- **REC-04** — ne lancer une phase observationnelle que sur une question que ce rapport laisse ouverte.

---

## 2. Ce qui a changé par rapport au cadrage initial

Le protocole prévoyait une couche d'observation propre : exposition GPSJAM, trajectoires ADS-B bornées, FIR témoins. Cette couche est restée bloquée par la permission GPSJAM et par les autorisations D4. Le 2026-10-30, la propriétaire a décidé de finaliser le cas comme **évaluation documentaire multi-sources** (choix de périmètre du 30 octobre 2026).

Conséquences assumées :
- les PIR-2, PIR-4 et PIR-5 sont partiellement **inconclusives** ;
- aucune donnée de trajectoire, aucun identifiant d'aéronef ni aucune donnée GPSJAM n'est utilisé ;
- les gels D1–D4 sont conservés, non exécutés ;
- la question, les hypothèses H1–H4, les variables canoniques et les garde-fous sont inchangés.

Un fait atténue cette perte : l'EASA publie elle-même, par FIR, l'indicateur que la couche propre devait calculer. Il s'agit de la part d'aéronefs dont la catégorie d'intégrité NIC est inférieure à 7, moyennée sur 7 et 30 jours (EV-059, EV-061). Le rapport s'appuie sur cette publication institutionnelle, avec ses biais déclarés, au lieu de la reproduire.

## 3. Méthode

1. **Vérification des preuves existantes.** Les 42 extraits du registre ATOM ont été revérifiés fragment par fragment (voir la [carte des preuves](evidence-map.md)) :
   - S-001 sur l'**original, identique à l'octet près** au snapshot gelé (SHA-256 `7e3be273…1218`), récupéré sur le miroir officiel EASA ;
   - S-004 et S-005 d'abord sur le texte de copies datées de la Wayback Machine (2026-10-30), puis sur les **originaux identiques à l'octet près** (SHA-256 `b55b46b6…3984` et `8f0d23fc…0660`), téléchargés par la propriétaire depuis ces copies le 2026-11-01.

   Résultat : **42 extraits complets sur 42**, tous vérifiés sur des octets identiques aux snapshots gelés. Les deux champs de cartouche d'EV-028, non extraits le 2026-10-30, figurent bien dans l'original.
2. **Sources complémentaires.** Cinq sources ont été ajoutées pour répondre aux PIR sans observation propre : la page EASA actualisée (S-002), IATA (S-020, S-021), les actes de l'atelier EASA–EUROCONTROL de juillet 2026 (S-022) et le procès-verbal UIT (S-023). Elles ont été téléchargées octet par octet et hachées. 25 extraits ont été vérifiés dans leur couche texte ([sources](sources.md), [carte des preuves](evidence-map.md)).
3. **Analyse.** Réponse PIR par PIR, matrice ACH, test de robustesse par retrait de la lignée dominante, puis rédaction des jugements et de la couche décisionnelle **en dernier**.
4. **Contre-analyse** sur les octets finaux, conduite par l'auteur.

## 4. Corpus et lignées

| Source | Nature | Lignée | Fiabilité | Rôle |
|---|---|---|---|---|
| [S-001](https://ad.easa.europa.eu/blob/EASA_SIB_2022_02R4_C1.pdf/SIB_2022-02R4_1) EASA SIB 2022-02R4 (07/2026) | bulletin de sécurité | ODG-EASA-SIB | A | tendance, zones, effets, statut réglementaire |
| [S-002](https://www.easa.europa.eu/en/domains/air-operations/global-navigation-satellite-system-outages-and-alterations) EASA, page GNSS (snapshot 30/10/2026) | tableau de bord institutionnel | ODG-EASA-NIC | A | méthode NIC, classement des FIR |
| [S-004](https://www.icao.int/sites/default/files/Meetings/a42/Documents/WP/wp_034_en.pdf) OACI A42-WP/34 | papier du Secrétariat | ODG-ICAO-SECRETARIAT | A | effets, NOTAM, cadre |
| [S-005](https://www.icao.int/sites/default/files/Meetings/a42/Documents/WP/wp_553_en.pdf) OACI A42-WP/553 | papier du Conseil + annexe des États | ODG-ICAO-COUNCIL / ODG-STATES-CWP15745 | A / B | FIR baltes, vols affectés, mesures RF |
| [S-020](https://ic.iata.org/sites/default/files/iata_sih_document_attachment/IATA%20Safety%20Risk%20Assessment%20-%20GNSS%20Interference%20V5.pdf) IATA, évaluation de risque v5 | évaluation sectorielle | ODG-IATA-FDX | B | taux par 1 000 vols |
| [S-021](https://www.iata.org/en/pressroom/2025-releases/2025-06-18-01/) Communiqué EASA–IATA | communiqué | ODG-IATA-FDX | B | +220 % (même lignée que S-020) |
| [S-022](https://www.eurocontrol.int/system/files/2026-07/gnss-rfi-workshop_slides_final.pdf) Atelier EASA–EUROCONTROL (07/2026) | diapositives de plusieurs intervenants | ODG-BOEING-GEM, ODG-PANSA, ODG-HUNGAROCONTROL | B | enregistreurs de bord, séries polonaises, biais de déclaration |
| [S-023](https://www.itu.int/dms_pub/itu-r/md/00/cr/cir/R00-CR-CIR-0518!!PDF-E.pdf) UIT, procès-verbal de la 98e réunion du RRB | procès-verbal officiel | ODG-ITU-RRB | A | dates, conclusion du Comité, hausse des cas |

**Lecture des lignées.** IATA, États et EASA mesurent tous à partir de données ADS-B ou d'enregistreurs de bord : leurs pipelines sont distincts, mais ce n'est pas une indépendance de mesure. Les mesures RF des États (EV-037) et les rapports d'équipage sont les seules classes de capteurs différentes. S-005 et S-023 se recoupent : le Conseil de l'OACI cite la conclusion de l'UIT, qui repose elle-même sur des mesures d'administrations nationales.

## 5. Réponses par besoin de renseignement

### PIR-1 — Évolution temporelle (KJ-01)

Trois lignées à taux ou à déclarations concordent sur une hausse 2022 → mi-2025 ; une quatrième (UIT) ne compte que des signalements :
- **EASA :** hausse depuis février 2022 (EV-001, EV-002) ;
- **IATA :** taux mondial de perte GPS de 28,1 à 56,1 pour 1 000 vols entre 2021 et 2024, puis 60,1 au premier semestre 2025 (EV-043, EV-044) ;
- **États :** part des vols affectés dans six FIR passée d'environ 7,5 % à 27,4 % entre mai 2024 et avril 2025 (EV-042) ;
- **UIT :** selon un membre du Comité, cas multipliés par plus de cinq sur janvier–septembre 2024 (EV-064), un comptage compatible avec un simple effet de signalement (H2), donc non discriminant.

Après la mi-2025, les signaux divergent. Le Conseil de l'OACI parle d'une interférence se poursuivant sans interruption (EV-039) et l'EASA classe toujours les mêmes FIR en octobre 2026 (EV-060). Mais PANSA montre, dans la FIR de Varsovie, un pic du brouillage en juin 2025 (1 940) puis une baisse jusqu'à 317 en novembre, avec une remontée à 620 en décembre (EV-055). Les baisses localisées que Boeing relève dans certaines FIR portent sur des données de juin 2024 à mai 2025 (EV-051, EV-070) : elles ne renseignent pas l'après-mi-2025.

**Réponse :** sens établi au niveau mondial et balte (Élevée), pour l'Europe entière (Modérée) ; ampleur européenne et évolution récente inconclusives (Faible).

### PIR-2 — Distribution géographique (KJ-02)

Deux foyers européens sont persistants. Le foyer Baltique et Nord-Est est cité par les États et le Conseil de l'OACI en 2025, par l'EASA en juillet et en octobre 2026, et par Boeing (EFIN 52 %). Le foyer mer Noire et Méditerranée orientale apparaît chez l'EASA en octobre 2026 (LTAA 1er) et chez Boeing (LTAA 77 %). Les effets sont aussi importés plus à l'ouest, à Budapest, par des vols venant de ces foyers (EV-058).

**Réponse :** foyers établis (Élevée) ; classement fin et émergence inconclusifs (Faible) ; atlas non produit.

### PIR-3 — Nature du phénomène (KJ-03)

Évaluation qualitative de compatibilité (voir §6) :
- **H3 (artefacts) écartée** comme explication principale : mesures RF, signatures de leurrage, enregistreurs de bord ;
- **H2 (meilleure détection) présente** : biais de déclaration et institutionnalisation de la surveillance ;
- **conclusion :** modèle mixte H4, à dominante H1.

Aucune classification automatique, aucun score probabiliste.

### PIR-4 — Conséquences observables (KJ-04)

La nature des conséquences est établie : déroutements, diversions, écarts aux clairances (EV-007), fausses alertes TAWS avec montées non coordonnées (EV-008), positions erronées après la sortie de zone (EV-010, EV-038). HungaroControl signale aussi des pertes de liaison CPDLC (EV-067). L'EASA maintient que la situation ne justifie pas de directive (EV-012).

**Inconclusif :** la fréquence, la gravité et la comparaison avec des fenêtres témoins.

### PIR-5 — Biais et sensibilité (KJ-03, KJ-05)

Biais chiffrés ou documentés :
- dans la FIR de Budapest, début 2026, seuls **2,6 à 8,1 %** des événements détectés sont déclarés par les pilotes (EV-057) — seule mesure publique de ce biais trouvée ;
- 18 codes NOTAM coexistent (EV-022) ;
- la définition de « affected » n'est pas publiée (GAP-002) ;
- l'indicateur EASA exige un nombre « représentatif » de mouvements et un seuil NIC (EV-059, EV-061) ;
- PANSA signale des interférences internes, civiles et militaires (EV-054).

**Inconclusif :** la décomposition de la tendance entre couverture, trafic et jours incomplets.

### PIR-6 — Indicateurs de veille civile (KJ-05)

| Indicateur | Usage | Garde-fou |
|---|---|---|
| Classement EASA des FIR, 7 et 30 jours (S-002) | repérer les zones persistantes | un rang n'est pas une intensité ; dépend du trafic et de la couverture ADS-B |
| Taux par 1 000 vols (IATA FDX, S-020) | tendance d'ensemble | mondial ; population variable ; accès réservé aux membres |
| Part des vols affectés par FIR (publications d'États, S-005) | tendance régionale | définition de « affected » à exiger |
| Rapports d'équipage | qualifier les effets | ne jamais compter : 2,6 à 8,1 % de déclaration à Budapest |
| Bulletins EASA et OACI | statut réglementaire | « information only » (EV-016) |

Chaque tableau ou carte dérivé doit porter la mention « Analyse OSINT — non destinée à la navigation ».

## 6. Hypothèses concurrentes (ACH)

Légende : **C** compatible · **I** incompatible · **N** neutre ou non discriminant.

| Preuve | H1 interférences intentionnelles accrues | H2 phénomène stable, mieux détecté | H3 artefacts / couverture | H4 mixte |
|---|---|---|---|---|
| Taux normalisés en hausse (EV-043, EV-042) | C | I | I | C |
| Mesures RF et triangulation (EV-037, EV-063) | C | N | I | C |
| Leurrage circulaire autour de Rostov (EV-032) | C | N | I | C |
| Enregistreurs de bord, hors couverture au sol (EV-046, EV-050) | C | N | I | C |
| Déclaration pilote 2,6–8,1 %, Budapest (EV-057) | N | C | N | C |
| Surveillance institutionnalisée (EV-059) | N | C | N | C |
| Interférences internes civiles et militaires (EV-054) | N | N | C (pour une partie) | C |
| Baisse locale en Pologne fin 2025 (EV-055) | N | N | N | C |

**Lecture :** H3 accumule des incohérences sur des preuves diagnostiques ; H2 seule est incompatible avec la hausse des taux normalisés ; H4 est compatible avec toutes les preuves, H1 en est la composante dominante. Ce qui ferait basculer le jugement : une série européenne à dénominateur constant montrant des taux stables (renforcerait H2), ou des campagnes RF ne trouvant pas d'émetteur (renforcerait H3).

## 7. Contradictions et robustesse

| ID | Objet | Traitement |
|---|---|---|
| CONTR-01 | 98e réunion du RRB : 17–21 mars 2025 (S-005 §1.3) contre 17–25 mars (annexe A §2.1) | **Résolue :** le procès-verbal de l'UIT, source primaire, donne 17–21 mars 2025 (EV-062). L'annexe des États contient une erreur de date sans portée sur les mesures. |
| CONTR-02 (proposée) | Persistance sans interruption (EV-039, 09/2025) contre baisse PANSA fin 2025 (EV-055) | Pas de contradiction de fond : périmètres différents (six FIR contre EPWW seule) et périodes différentes. Elle limite la confiance sur l'évolution après mi-2025 (KJ-01). |

**Robustesse — retrait de la lignée dominante.**
- KJ-01 : sans IATA, seuls l'EASA (qualitatif) et les États (2024–2025, six FIR) portent la tendance ; le sens tient pour le foyer balte, **la confiance pour 2022–2023 tombe à Faible**.
- KJ-02 : sans l'EASA, les États, l'OACI et Boeing désignent les mêmes foyers ; KJ-02 tient.
- KJ-03 : sans les mesures RF des États, le rejet de H3 repose encore sur le leurrage de Rostov (même lignée d'États) et sur les enregistreurs de bord ; **la confiance passerait à Modérée**.
- Aucun jugement ne repose sur une source unique.

## 8. Recommandations

| ID | Action | Objectif | Porteur | Déclencheur / condition | Revue |
|---|---|---|---|---|---|
| REC-01 | Suivre le classement EASA 7/30 jours et des taux normalisés ; ne jamais suivre un compte brut d'incidents | éviter de confondre hausse du signalement et hausse du phénomène | responsable sécurité des vols ou veille | mise en place de toute veille GNSS | trimestrielle, à chaque révision du bulletin EASA |
| REC-02 | Traiter les effets GNSS comme pouvant persister après la sortie d'une zone affectée (positions, temps, TAWS) | couvrir les vols qui traversent les deux foyers | exploitants, formation des équipages | vols traversant les FIR de KJ-02 | à chaque nouvelle publication EASA ou OACI |
| REC-03 | Exiger, pour tout chiffre transmis, le dénominateur et la définition de « affecté » | rendre les séries comparables (GAP-002) | toute organisation qui publie ou relaie des chiffres | réception d'un chiffre non normalisé | à chaque échange de données |
| REC-04 | N'ouvrir une phase observationnelle (ADS-B bornée, témoins) que pour une question laissée ouverte ici : ampleur européenne, émergence, conséquences | ne pas collecter de trajectoires pour compenser une lacune documentaire | propriétaire du projet | nouvelle décision explicite et permissions | à la décision suivante sur D4 et GPSJAM |

## 9. Limites et lacunes

- **Octets de S-004 et S-005 :** confirmés identiques aux SHA-256 gelés le 2026-11-01 (fichiers fournis par la propriétaire). L'ancien snapshot gelé de S-002 et ceux de trois pages non utilisées (S-003, S-006, S-007) ne sont pas retrouvés : S-002 a été recollecté (nouveau snapshot daté) et aucun extrait ne dépend des trois autres.
- **Sources de type diapositives (S-022) :** méthodes non publiées ; unités des séries PANSA non précisées.
- **Portée mondiale d'IATA et de Boeing :** pas de ventilation européenne publique.
- **Accès :** aucune donnée non publique, aucune donnée GPSJAM, aucune observation propre.

| Lacune | État au 1er novembre 2026 | Motif |
|---|---|---|
| GAP-001 — snapshots de pages HTML | close | nouveau snapshot daté pour S-002 ; aucun extrait ne dépend des trois autres pages |
| GAP-002 — dénominateurs et définition de « affecté » | ouverte | définition de « affected » et dénominateurs non publiés (REC-03) |
| GAP-003 — lignées de mesure | ouverte | lignées enregistrées par jugement ; entrées des indicateurs EASA non identifiées |
| GAP-004 — mesures radiofréquence | ouverte | conclusion primaire de l'UIT obtenue (EV-063) ; mesures RF brutes non publiques |
| GAP-005 — conséquence par événement | sans objet pour cette édition ; ouverte pour une phase d'observation | hors périmètre de l'édition documentaire |
| GAP-006 — couverture des capteurs | sans objet pour cette édition ; ouverte pour une phase d'observation | hors périmètre de l'édition documentaire |
| GAP-007 — changements des pratiques de signalement | ouverte | codes NOTAM et biais de déclaration documentés ; pas de journal daté des changements |
| GAP-008 — dates de la réunion UIT | close | CONTR-01 résolue sur pièce primaire (EV-062) |
| GAP-009 — corrections du registre des sources | close | corrections du registre des sources faites et revues |
| GAP-010 — accès aux données ADS-B et GPSJAM | sans objet pour cette édition ; ouverte pour une phase d'observation | hors périmètre de l'édition documentaire |
| GAP-011 — zones témoins | sans objet pour cette édition ; ouverte pour une phase d'observation | hors périmètre de l'édition documentaire |

## 10. Traçabilité

- Jugements : [jugements clés](key-judgments.md)
- Sources : [liste des sources](sources.md), avec leurs liens publics
- Preuves : [carte des preuves](evidence-map.md) (identifiant, source, localisation, jugements) et [provenance](provenance.csv)
- Les registres de travail et les extraits verbatim ne sont pas publiés : les conditions de plusieurs éditeurs réservent la reproduction.

## Glossaire

| Terme | Sens dans ce rapport |
|---|---|
| ACH | analyse des hypothèses concurrentes : matrice confrontant chaque preuve aux hypothèses H1 à H4 |
| ADS-B | messages de position que les avions diffusent ; ils incluent un indicateur d'intégrité (NIC) |
| CEAC | Conférence européenne de l'aviation civile (ici : périmètre européen au sens large, Turquie comprise) |
| CONTR-01, CONTR-02 | contradictions entre sources, traitées au §7 ; CONTR-02 est signalée sans être une contradiction de fond |
| CPDLC | liaison de données contrôleur-pilote |
| EV-xxx | identifiant d'un extrait de source, localisé dans la [carte des preuves](evidence-map.md) |
| FDX | programme d'échange de données de vol d'IATA |
| FIR | région d'information de vol (par exemple EPWW : Varsovie ; LTAA : Ankara) |
| GAP-xxx | lacune de l'enquête, avec son état au §9 |
| GNSS | systèmes de navigation par satellite (GPS, Galileo…) |
| GPSJAM | site public de cartes d'interférences dérivées de l'ADS-B, non utilisé dans cette édition |
| KJ-01 à KJ-05 | jugements clés |
| Lignée | origine commune d'une mesure ; deux sources de même lignée ne se corroborent pas |
| NIC | catégorie d'intégrité de navigation déclarée dans l'ADS-B ; une valeur inférieure à 7 signale une position dégradée |
| PIR | besoins prioritaires de renseignement, c'est-à-dire les six questions de l'étude |
| RRB | Comité du Règlement des radiocommunications de l'UIT |
| Snapshot | copie datée et hachée d'une source, conservée hors du dépôt public |
| TAWS | système d'avertissement de proximité du relief |
