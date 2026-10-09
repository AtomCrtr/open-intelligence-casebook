# 🛩️ Case 03 - Interférences GNSS et aviation civile européenne

**Statut : en cours - design analytique gelé avant données réelles.**

[![Statut](https://img.shields.io/badge/statut-en%20d%C3%A9veloppement-c8643b)](#avancement)
[![Design](https://img.shields.io/badge/design-gel%C3%A9-1f6f78)](#pourquoi-geler-le-design-avant-les-données-)
[![Données réelles](https://img.shields.io/badge/donn%C3%A9es%20r%C3%A9elles-aucune%20publi%C3%A9e-7a93a0)](#ce-que-cette-page-ne-contient-pas)
[![Publication](https://img.shields.io/badge/publication-HOLD-7a93a0)](#comment-ce-cas-deviendra-publiable)

> **Question de recherche :** comment les données ouvertes peuvent-elles aider à suivre et caractériser les dégradations de navigation touchant l'aviation civile européenne depuis 2022, sans confondre corrélation, couverture des capteurs et causalité ?

Le travail combine OSINT institutionnel, GEOINT par FIR, data engineering et analyse bornée de trajectoires historiques. Le design actuel impose une séparation stricte entre **observation cinématique ou qualité de données** et toute classification de brouillage, spoofing, interférence GNSS ou attribution.

*État au 9 octobre 2026. Cette page présente une méthode et un état d'avancement, pas un résultat.*

<p align="center">
  <img src="figures/case03_gates.svg" alt="Avancement du Case 03 en six étapes : question, design et protocole gelés ; accès aux données sous gates ; jugements non rédigés ; publication en HOLD. Quatre garde-fous d'interprétation sont rappelés." width="100%">
</p>

📌 [Avancement](#avancement) · 🔬 [Axes d'étude](#six-axes-détude) · ⚖️ [Hypothèses concurrentes](#hypothèses-concurrentes) · 🛡️ [Garde-fous](#garde-fous-méthodologiques) · ✅ [Établi / non démontré](#établi--non-démontré) · 🔎 [Revue des droits](../../publication/rights-review.md)

---

## En deux minutes

- **Ce que le cas cherche à faire :** suivre, du 14 février 2022 au 31 juillet 2026, l'évolution et la distribution géographique des **dégradations de navigation déclarées** dans l'espace aérien européen, puis examiner ce qu'elles permettent - ou non - d'affirmer sur d'éventuelles interférences GNSS.
- **Où il en est :** la question, le périmètre, les règles de décision et le protocole d'accès borné aux données sont **gelés**. Ils l'ont été **avant** toute observation réelle, pour que ni les événements retenus, ni le choix d'éventuelles zones témoins, ni les seuils ne puissent être ajustés après coup.
- **Ce qui est publié :** uniquement cette page de méthode. **Aucune conclusion, aucun niveau de confiance, aucune carte, aucune statistique** issus de données réelles : il n'en existe pas encore de publiables.
- **Ce qui est interdit d'avance :** transformer un signal de précision déclarée en preuve de brouillage, une observation ADS-B en mesure radiofréquence, une coïncidence temporelle en cause, ou une géométrie en attribution.

## Pourquoi geler le design avant les données ?

Définir les fenêtres, les critères et les tests **avant** d'inspecter les observations réelles limite deux biais classiques : choisir les événements qui confirment l'intuition, et ajuster les seuils après coup. Chaque étape d'accès à des données réelles passe par un gate documenté et une approbation humaine explicite.

Concrètement, le protocole gelé fixe à l'avance :

- les règles de sélection des fenêtres d'événements, indépendantes des résultats que l'on cherchera ensuite à expliquer ;
- les critères d'éventuelles zones témoins, définis avant tout accès aux trajectoires et sans lien avec le niveau de perturbation ou la gravité rapportée : aucune zone témoin n'est encore choisie, et aucune ne pourra l'être à partir des observations ;
- le traitement des jours incomplets et des données manquantes, qui restent **manquantes** et ne sont jamais converties en « absence de perturbation » ;
- les limites de volume de toute première collecte, afin qu'un essai ne puisse pas déborder de son cadre.

## Avancement

| Étape | État |
|---|---|
| Question, périmètre, besoins de renseignement | ✅ gelés |
| Design analytique | ✅ gelé |
| Pré-enregistrement de l'accès borné aux données | ✅ gelé |
| Accès aux données réelles | ⏳ sous gates d'autorisation humaine explicite |
| Jugements analytiques | ⏳ non rédigés |
| Publication du cas complet | ⛔ HOLD |

## Six axes d'étude

| Axe | Question posée | Statut |
|---|---|---|
| 1. Évolution temporelle | comment la dégradation déclarée évolue-t-elle sur la période ? | non traité |
| 2. Distribution géographique | quelles FIR montrent une dégradation persistante ou émergente ? | non traité |
| 3. Nature du phénomène | les observations sont-elles compatibles avec une interférence, plutôt qu'avec une couverture dégradée ou un artefact technique ? | non traité |
| 4. Conséquences observables | quelles anomalies opérationnelles apparaissent sur des fenêtres fixées indépendamment ? | non traité |
| 5. Biais et sensibilité | quelle part d'une tendance s'explique par la couverture, le trafic, les jours incomplets ou la géométrie ? | non traité |
| 6. Indicateurs de veille civile | quels indicateurs ouverts sont utiles sans devenir des alertes de navigation ? | non traité |

Le troisième axe produira, le moment venu, une **évaluation qualitative de compatibilité** accompagnée de ses explications alternatives et de ses conditions d'invalidation - jamais un score probabiliste ni une classification automatique de « brouillage » ou de « leurrage ».

## Hypothèses concurrentes

Quatre explications sont conservées ouvertes jusqu'à l'analyse finale. **Aucune n'est privilégiée à ce stade.**

| Hypothèse | Énoncé | Évaluation |
|---|---|---|
| H1 | augmentation et diffusion réelles d'interférences intentionnelles | non évaluée |
| H2 | phénomène globalement stable, mais davantage détecté et déclaré | non évaluée |
| H3 | artefacts techniques, trafic ou couverture expliquant l'essentiel | non évaluée |
| H4 | modèle mixte : interférences réelles amplifiées par la détection | non évaluée |

H4 est une hypothèse de travail, pas une conclusion écrite d'avance. Pour chacune, le cas précisera d'abord ce qui la renforcerait et ce qui l'affaiblirait, puis seulement ensuite ce que les observations en disent.

## Garde-fous méthodologiques

Ces règles s'appliquent à toute étape future du cas :

- la variable observée est une **dégradation déclarée de la précision de navigation** ; elle n'est jamais renommée « brouillage », « leurrage » ou « interférence GNSS » à elle seule ;
- parler d'**interférence suspectée** exige une corroboration par une source indépendante et un examen explicite des explications liées à la couverture ou à la collecte ;
- une observation **ADS-B n'est pas une mesure radiofréquence** et ne démontre ni une interférence, ni une conséquence, ni une attribution ;
- **une coïncidence temporelle n'établit pas une causalité** ;
- **aucune attribution** n'est déduite de la géométrie, de la proximité, d'un maillage hexagonal ou de la forme d'une trajectoire ;
- plusieurs reprises d'une même information ne comptent pas comme plusieurs corroborations indépendantes ;
- le résultat n'est ni une alerte en temps réel, ni un outil de navigation : chaque carte et chaque tableau futurs porteront la mention « Analyse OSINT - non destinée à la navigation ».

## Établi / non démontré

| Établi à ce stade | Non démontré - et non produit |
|---|---|
| la question, le périmètre et la période d'étude sont fixés | toute tendance temporelle de la dégradation déclarée |
| les règles de décision sont gelées avant observation | toute zone persistante ou émergente |
| les garde-fous d'interprétation sont explicites | toute compatibilité avec un brouillage ou un leurrage |
| les quatre hypothèses sont posées sans en privilégier une | toute conséquence opérationnelle |
| les accès aux données sont soumis à des gates humains | toute attribution |

## Ce que cette page ne contient pas

**Aucune conclusion historique issue de données réelles n'est publiée dans cette première édition.** Aucun identifiant d'aéronef, aucune trajectoire sensible, aucune donnée GPSJAM en volume, aucune fixture synthétique et aucune sortie événementielle ne sont inclus.

Le cas sera ajouté lorsqu'il aura franchi son propre gate de publication.

## Comment ce cas deviendra publiable

```text
sources figées (URL, horodatage UTC, SHA-256)
→ observations autorisées uniquement
→ affirmations traçables
→ contradictions et hypothèses concurrentes
→ robustesse si la source dominante est retirée
→ 3 à 5 jugements, rédigés en dernier
→ Red Team analytique
→ vérification des droits et de la confidentialité
→ autorisation humaine explicite
```

- Le dépôt canonique de travail reste privé ; ce dépôt public ne reçoit que des **éditions assainies**, jamais un miroir du travail en cours.
- Les données tierces dont la réutilisation n'est pas clairement autorisée - notamment les agrégats GPSJAM - ne sont ni collectées en volume ni redistribuées tant qu'un accord de réutilisation explicite n'existe pas.
- Les documents institutionnels (EASA, EUROCONTROL, OACI) seront cités et liés ; ils ne sont pas recopiés.
- Les identifiants d'aéronefs, indicatifs individuels et trajectoires sensibles ne seront jamais publiés.

La méthode commune est décrite dans le [cycle analytique](../../methodology/analytical-cycle.md), l'[évaluation des sources](../../methodology/source-evaluation.md) et la page [hypothèses et confiance](../../methodology/confidence-and-hypotheses.md).

## Contenu du dossier

```text
case-03-gnss-interference/
├── README.md                    # cette page : méthode et état d'avancement
└── figures/
    └── case03_gates.svg         # avancement par étapes et garde-fous
```

[← Retour au casebook](../../README.md)
