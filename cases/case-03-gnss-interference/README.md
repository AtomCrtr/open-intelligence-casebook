# 🛩️ Case 03 - Interférences GNSS et aviation civile européenne

**Statut : évaluation documentaire finale (version 1.0 du 1er novembre 2026).**

> **Analyse OSINT — non destinée à la navigation.**

> **Question de recherche :** comment les données ouvertes peuvent-elles aider à suivre et caractériser les dégradations de navigation touchant l'aviation civile européenne depuis 2022, sans confondre corrélation, couverture des capteurs et causalité ?

📄 [Rapport](report.md) · ⚖️ [Jugements clés](key-judgments.md) · 🔗 [Sources](sources.md) · 🧭 [Carte des preuves](evidence-map.md) · 🧾 [Provenance](provenance.csv)

<p align="center">
  <img src="figures/case03_confidence.svg" alt="Douze affirmations publiques tirées des cinq jugements clés, chacune avec son niveau de confiance : élevée pour la hausse 2022–mi-2025 au niveau mondial et balte, les deux foyers, le rejet des artefacts, la réalité des conséquences et l'inadéquation des comptages bruts ; modérée pour la hausse à l'échelle de l'Europe entière, la dominance de la composante réelle et les indicateurs de veille ; non établis : l'évolution après la mi-2025, le classement fin des FIR et la fréquence des conséquences ; attributions rapportées, non jugées." width="100%">
</p>

**Première visite :** [guide de découverte du renseignement et des quatre cas](https://github.com/AtomCrtr/open-intelligence-casebook/blob/main/READING_GUIDE.md).

## Comprendre le sujet

**La question en langage courant.** Que peut-on savoir sur les perturbations de navigation par satellite qui touchent l'aviation civile, à partir des documents accessibles ?

**L'idée à retenir.** Les sources documentent des perturbations réelles et des conséquences opérationnelles. Elles ne fournissent pas une mesure homogène de tous les événements européens ni de leurs conséquences.

**Ce qui a été fait.** Le dossier compare des publications institutionnelles et sectorielles, examine leurs dépendances et confronte plusieurs explications. Le projet n'a pas exécuté la couche d'observation ADS-B/GPSJAM prévue au départ.

**Statut.** Étude documentaire finalisée et publiée. Une étude fondée sur de nouvelles observations constituerait une phase distincte.

---

## En deux minutes

- **Ce que le cas établit.** Les dégradations GNSS touchant l'aviation civile ont nettement augmenté de 2022 à la mi-2025 au niveau mondial et dans le foyer balte (confiance élevée ; pour l'Europe prise dans son ensemble : modérée). Elles se concentrent sur deux foyers persistants : la Baltique et le Nord-Est, puis la mer Noire et la Méditerranée orientale (élevée). Elles relèvent de brouillages et de leurrages réels, l'hypothèse de simples artefacts étant écartée (élevée), amplifiés par une meilleure détection dont la part n'est pas quantifiable (modérée). Leurs conséquences opérationnelles sont réelles et documentées (élevée).
- **Ce qu'il ne mesure pas.** L'ampleur européenne avec un dénominateur homogène, l'évolution après la mi-2025, la fréquence et la gravité des conséquences, l'apparition éventuelle de nouveaux foyers.
- **Ce qu'il recommande pour la veille.** Suivre des taux normalisés et l'indicateur EASA par FIR, jamais des comptages bruts d'incidents. Dans la FIR de Budapest, seuls 2,6 à 8,1 % des événements détectés sont déclarés par les pilotes.
- **Attributions.** Les attributions citées (UIT, Conseil de l'OACI, PANSA, IATA) sont **rapportées** telles que leurs auteurs les formulent. Le projet ne dispose d'aucune mesure radiofréquence propre et ne les requalifie pas.

## Comment le cas a été conduit

Le protocole initial prévoyait une couche d'observation propre : exposition GPSJAM, trajectoires ADS-B bornées, zones témoins. Les autorisations nécessaires n'ayant pas été réunies, le périmètre a été fixé le 30 octobre 2026 : le cas est une **évaluation documentaire multi-sources**, dont les jugements ont été approuvés le 1er novembre 2026 et corrigés le 6 novembre 2026 après une contre-relecture. Aucune trajectoire, aucun identifiant d'aéronef et aucune donnée GPSJAM n'est utilisé ni publié.

Le corpus compte 8 sources institutionnelles et sectorielles (EASA, OACI, IATA, atelier EASA–EUROCONTROL, UIT), regroupées en 10 lignées d'information. Chaque jugement cite des extraits identifiés (EV-xxx), vérifiés sur des fichiers dont l'empreinte a été enregistrée. Les hypothèses concurrentes ont été confrontées dans une matrice ACH. Une contre-analyse de l'auteur a précédé l'approbation des jugements ; l'édition publique a ensuite été contre-relue par un second agent d'IA, distinct de l'auteur, dont les remarques ont conduit aux errata du 6 novembre 2026. **Aucune revue humaine indépendante n'a été faite.**

## Ce que cette page ne contient pas

- aucune copie de document tiers : les sources sont liées, pas redistribuées ;
- aucune citation textuelle des documents de l'OACI, d'IATA, de l'UIT ou des intervenants de l'atelier, dont les conditions réservent la reproduction : leurs propos sont paraphrasés et attribués ;
- aucun registre de travail, aucun extrait verbatim, aucune donnée de trajectoire.

*Les mentions « vérifié » et « contre-analyse » de cette édition renvoient à des contrôles effectués par l'auteur. Elles ne valent ni revue indépendante ni validation scientifique.*

🔎 [Revue des droits de l'édition publique](../../publication/rights-review.md)
