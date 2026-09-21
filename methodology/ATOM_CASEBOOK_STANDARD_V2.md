# ATOM Casebook Standard v2.0

> **Decision-first + Evidence-deep.**  
> A casebook must let a decision-maker understand the essentials in less than five minutes, while allowing an analyst to reconstruct every important judgment from the evidence trail.

This standard governs new analytical cases published in **Open Intelligence Casebook**. It is a synthesis of the repository's existing principles and lessons extracted from high-quality DeepThreats 2026 reporting patterns, without copying institutional branding, classification markings, or protected report text.

---

## Rule 0 — Two-speed reading

Every complete casebook MUST support two reading modes.

### Layer A — Decision layer

Target: **1–2 pages / ≤ 5 minutes**.

It MUST contain:

- the decision question;
- a short executive answer;
- 3–5 Key Judgments;
- a confidence level for each major judgment;
- direct answers to the Priority Intelligence Requirements (PIRs);
- the principal risks / vulnerabilities;
- the decisions or actions requested;
- the critical uncertainties and indicators to watch.

A reader who stops here must understand what is known, why it matters, what remains uncertain, and what can reasonably be decided.

### Layer B — Evidence layer

Target: enough depth to audit the reasoning.

It SHOULD contain, where relevant:

- scope and methodology;
- source classes and collection constraints;
- source / evidence register;
- analytical chronology;
- operational phasing;
- actor / entity / infrastructure graphs;
- mechanism or lever analysis;
- competing hypotheses;
- inconsistencies, weak signals and unresolved questions;
- vulnerabilities and second-order effects;
- recommendations traceable to findings;
- appendices, transformations, hashes and provenance.

**Invariant:** Layer A MUST never claim more than Layer B can demonstrate.

---

## 1. Mission frame

Every case begins with a short mission card.

| Field | Requirement |
|---|---|
| Case title | concise and descriptive |
| Decision-maker / audience | who needs the answer |
| Decision question | one main question |
| PIRs | 2–7 sub-questions |
| Time window | investigation / evidence period |
| Geographic scope | explicit |
| Languages | explicit if relevant |
| Collection constraints | passive / API / archive / dataset / other |
| Publication status | working / review / public release |
| Ethics / legal constraints | data minimisation, privacy, rights |

The question must be answerable from observable evidence. Avoid questions that require access to intent, causality or classified information unless the case explicitly treats them as hypotheses.

---

## 2. Executive Intelligence Summary

The executive layer must be written **after** the analysis, even if it appears first.

### 2.1 Executive answer

Write 5–10 lines answering:

1. What happened?
2. Why does it matter?
3. What is the dominant mechanism?
4. What is the principal uncertainty?
5. What action or decision follows?

### 2.2 Key Judgments

Use this format:

| ID | Key Judgment | Confidence | Main evidence | What could change the judgment? |
|---|---|---|---|---|
| KJ-01 | ... | High / Medium / Low | EV-... | discriminating evidence |

Rules:

- 3–5 Key Judgments for a standard investigation;
- one sentence per judgment before explanation;
- confidence describes the **judgment**, not the source;
- each judgment must be traceable to evidence;
- no numerical probability unless a real statistical model exists.

### 2.3 PIR answers

| PIR | Short answer | Confidence | Status |
|---|---|---|---|
| PIR-01 | ... | High / Medium / Low | Answered / Partial / Open |

---

## 3. Analytical language

ATOM separates three dimensions that are often confused.

### 3.1 Nature of the statement

Optional inline markers for long or sensitive reports:

- **[FACT]** — directly documented or reproducibly observed;
- **[ASSESSMENT]** — analytical interpretation supported by multiple elements;
- **[HYPOTHESIS]** — plausible explanation not sufficiently corroborated;
- **[UNKNOWN]** — evidence is insufficient, contradictory or unavailable.

### 3.2 Evidence status

For the evidence map, use the repository's public vocabulary:

- **Observed**
- **Reported**
- **Corroborated**
- **Inferred**
- **Hypothesis**
- **Not demonstrated**

These labels describe the evidence chain, not the analyst's confidence.

### 3.3 Confidence

Use **High / Medium / Low** for significant analytical judgments.

Confidence must consider:

- source quality;
- independence of corroboration;
- completeness;
- consistency;
- alternative explanations;
- temporal relevance;
- reproducibility.

### 3.4 Optional source grading

For complex cases, a source can additionally receive a two-axis reliability / credibility rating (for example A–F / 1–6), provided the scale is defined in the report.

Never use a source rating as a substitute for judgment confidence.

---

## 4. Source and evidence register

Each important claim should be recoverable through a stable identifier.

Recommended minimum fields:

| Field | Example |
|---|---|
| Source ID | SRC-001 |
| Evidence ID | EV-001 |
| Description | registry extract / post / dataset / DNS record |
| Date / time | ISO 8601 |
| Collection date | ISO 8601 |
| Source class | official / corporate / social / technical / academic / dataset |
| Evidence status | observed / reported / corroborated / inferred |
| Reliability | optional |
| Used for | KJ-01, PIR-02 |
| Archive / path | URL, local path or archive |
| Hash | SHA-256 where appropriate |
| Redistribution | public / derived-only / link-only |

A URL alone is not an evidence register.

---

## 5. OSINT / non-OSINT boundary

Every case MUST state what kind of material was used.

Distinguish:

- public open sources;
- archives;
- public technical data;
- public datasets;
- user-provided material;
- exercise-provided material;
- private or leaked material;
- synthetic / fixture data.

If a case includes material that is not strictly OSINT, say so explicitly and explain how it affects confidence and reproducibility.

---

## 6. Chronology and phasing

Use a chronology when sequence changes the interpretation.

### 6.1 Analytical timeline

| Date | Event | Evidence | Status | Analytical significance |
|---|---|---|---|---|

Do not write a chronology as a diary. Include only events that change the understanding of the case.

### 6.2 Phasing

Recommended generic phases:

1. pre-positioning;
2. approach / reconnaissance;
3. action / exploitation;
4. consolidation / locking-in;
5. continuation / indicators.

Phase names may change by case.

A phase is an analytical grouping, not merely a date range.

---

## 7. Actor and relationship modelling

Use graphs only when they reduce cognitive load.

Prefer multiple graphs over one unreadable graph if relationship types differ.

Possible views:

- ownership / capital;
- human / family / professional;
- technical infrastructure;
- information flow;
- financial flow;
- event sequence.

Every edge in a graph must have a source or evidence ID somewhere in the case.

Do not infer a relationship merely because two entities appear in the same dataset.

---

## 8. Mechanism / lever analysis

A mature casebook explains **how the observed effects were produced**, not just what was found.

For each mechanism:

### Lever X — [name]

- established facts;
- analytical assessment;
- intended / plausible effect;
- dependencies;
- key evidence;
- alternative explanation;
- indicators.

Examples of generic lever families:

- capital / ownership;
- access / organisation;
- technology / data;
- influence / information;
- human pressure / coercion;
- regulatory / legal;
- supply-chain / dependency;
- infrastructure / technical.

Use only the levers that the evidence supports.

---

## 9. Competing hypotheses

At least one credible alternative hypothesis must be considered for any consequential attribution, causality or intent judgment.

| Hypothesis | Supporting evidence | Contradicting evidence | Missing discriminant | Current assessment |
|---|---|---|---|---|

Rules:

- do not invent absurd alternatives just to satisfy a checklist;
- preserve contradictions;
- state what evidence would discriminate between hypotheses;
- if no hypothesis can be preferred, say so.

---

## 10. Weak signals, anomalies and open questions

Create a dedicated section when useful.

For each item:

| Signal / question | What is observed | Why it matters | What is NOT established | Next discriminant |
|---|---|---|---|---|

This prevents weak signals from being smuggled into the main narrative as facts.

**Rule:** narrative accumulation does not increase evidentiary strength by itself.

---

## 11. Vulnerabilities and risks

Separate vulnerability from consequence.

| Vulnerability | Exploited / exposed by | Impact | Likelihood | Criticality | Evidence |
|---|---|---|---|---|---|

Then structure risks by horizon:

- immediate;
- short term;
- medium term;
- long term;
- second-order effects.

When a risk is speculative, label it as such.

---

## 12. Recommendations

Every recommendation must be traceable.

| Priority | Horizon | Action | Objective | Owner | Condition / trigger | Traceability |
|---|---|---|---|---|---|---|
| P0 | immediate | verb + object | risk reduced | accountable actor | if / when | KJ / vulnerability / evidence |

A recommendation is incomplete if it lacks:

- an action;
- an objective;
- an owner;
- a reason grounded in the analysis.

Prefer recommendations that are conditional and reversible when uncertainty remains high.

---

## 13. Conclusion

The conclusion should fit in 5–10 lines.

It must:

- restate the principal judgment;
- state confidence;
- identify the dominant mechanism;
- identify the main unresolved uncertainty;
- state the most urgent or consequential decision.

Do not introduce new evidence in the conclusion.

---

## 14. Appendices

Recommended appendices:

### A. Indicators / observables

Domains, IPs, identifiers, handles, company numbers, coordinates, document references, wallets, hashes.

### B. Evidence map

Claim → evidence → transformation → judgment.

### C. Analytical journal

- hypotheses tested;
- pivots;
- failed leads;
- contradictions;
- methodological decisions.

### D. Source list / provenance

Document enough detail to reproduce the analysis without redistributing material that cannot legally be republished.

---

## 15. Public-release gate

Before public release, verify:

- [ ] no secret, credential or sensitive internal path is exposed;
- [ ] personal data are minimised;
- [ ] third-party content is not redistributed beyond its rights;
- [ ] link-only / derived-only material is respected;
- [ ] every important claim is traceable;
- [ ] facts and assessments are visually distinguishable;
- [ ] uncertainty is visible;
- [ ] alternative hypotheses were considered where needed;
- [ ] the executive layer can be understood in ≤ 5 minutes;
- [ ] recommendations are linked to findings;
- [ ] figures are legible and sourced;
- [ ] PDF / Markdown outputs are consistent;
- [ ] checksums / manifest are refreshed when required by the repository publication workflow;
- [ ] AI assistance, if used, is disclosed according to repository policy.

---

## 16. Red-team gate

Before freezing the report, answer all of these:

1. Which Key Judgment is the most fragile?
2. Which single fact, if false, would damage the analysis most?
3. Is there a simpler alternative explanation?
4. Where could correlation, simultaneity and causality be confused?
5. Which source is carrying too much analytical weight?
6. Which interesting detail does not change any decision and belongs in an appendix?
7. Which sentence sounds more certain than the evidence allows?
8. Which recommendation cannot be traced to a documented finding?
9. What new evidence would change the confidence level?
10. Can a decision-maker understand the essentials without reading the annexes?

A case does not pass publication if these questions are unanswered.

---

# Mega prompt — Produce or review an ATOM Casebook

Copy the prompt below into an analytical assistant only after providing the case material, source register and project constraints.

```text
ROLE
You are an intelligence-analysis editor working under the ATOM Casebook Standard v2.0.
Your job is not to produce the most impressive narrative. Your job is to produce the most defensible,
traceable and decision-useful analysis that the available evidence supports.

CORE RULE
Apply "Decision-first + Evidence-deep".
The output must work in two layers:
1) a decision layer understandable in 5 minutes;
2) an evidence layer that allows a reviewer to reconstruct every important judgment.

NON-NEGOTIABLES
- Never turn a missing fact into an inferred fact.
- Never turn repetition into corroboration when sources are dependent.
- Never confuse source reliability with confidence in a judgment.
- Never infer intent, attribution or causality beyond the available evidence.
- Never hide contradictions.
- Never remove an alternative hypothesis only because it weakens the preferred narrative.
- Never write a recommendation that cannot be traced to a finding, vulnerability or risk.
- Clearly distinguish public OSINT from exercise-provided, user-provided, private, leaked, synthetic or fixture data.
- Respect privacy, publication rights and the repository's link-only / derived-only rules.
- Do not reproduce institutional classification markings or pretend the report is an official government product.

STEP 1 — FRAME THE MISSION
Extract:
- decision-maker / audience;
- central decision question;
- 2–7 PIRs;
- time window;
- geographic scope;
- entities;
- languages;
- collection constraints;
- legal / ethical / publication constraints.

If any of these are unknown, mark them UNKNOWN instead of inventing them.

STEP 2 — INVENTORY THE EVIDENCE
Create a source/evidence register with stable IDs.
For each source capture:
- origin;
- date;
- collection date;
- class;
- independence;
- reliability;
- evidence status;
- archive / path / hash if available;
- claims or PIRs supported;
- redistribution status.

Identify source dependencies. Ten articles repeating the same primary source count as one evidentiary lineage, not ten independent corroborations.

STEP 3 — SEPARATE STATEMENT TYPES
Tag consequential statements as:
[FACT] directly documented;
[ASSESSMENT] analytical interpretation supported by multiple elements;
[HYPOTHESIS] plausible but insufficiently corroborated;
[UNKNOWN] unresolved.

In the evidence map additionally distinguish:
Observed / Reported / Corroborated / Inferred / Hypothesis / Not demonstrated.

STEP 4 — TEST COMPETING HYPOTHESES
For every consequential judgment involving attribution, intent, coordination or causality:
- define the leading hypothesis;
- define at least one credible alternative when one exists;
- list supporting evidence;
- list contradicting evidence;
- identify the discriminating evidence still missing;
- state the current assessment.

Do not create straw-man alternatives.

STEP 5 — BUILD THE TEMPORAL MODEL
If timing matters:
- produce a concise analytical timeline;
- identify phases;
- distinguish completed, ongoing and prospective events;
- flag temporal inconsistencies;
- explain why each included event matters.

STEP 6 — BUILD RELATIONSHIP MODELS
Decide whether one graph is enough.
If relationship families differ, produce separate views:
ownership/capital, human/professional, infrastructure, information flow, financial flow, event flow.
Every edge must be traceable to evidence.

STEP 7 — EXPLAIN THE MECHANISM
Do not write a discovery dump.
Group evidence into mechanisms / levers.
For each lever state:
- facts;
- assessment;
- effect;
- dependencies;
- evidence;
- alternative explanation;
- indicators.

STEP 8 — RECORD WEAK SIGNALS AND OPEN QUESTIONS
Create a dedicated section.
For each item say:
- what is observed;
- why it might matter;
- what is not established;
- what evidence would resolve it.

STEP 9 — ASSESS VULNERABILITIES AND RISKS
Separate:
vulnerability -> exploitation/exposure -> consequence -> risk.
Organise risks by horizon and identify second-order effects.

STEP 10 — WRITE RECOMMENDATIONS
Use:
Priority | Horizon | Action | Objective | Owner | Condition/Trigger | Traceability.
Use action verbs.
Prefer conditional recommendations when confidence is not high.
Reject recommendations that are generic or not linked to evidence.

STEP 11 — WRITE THE DECISION LAYER LAST
Produce:
A. Executive answer in 5–10 lines.
B. 3–5 Key Judgments, each with confidence and evidence references.
C. PIR answer table.
D. Top risks.
E. Decisions/actions requested.
F. Critical uncertainties and indicators.

The decision layer must not introduce claims absent from the evidence layer.

STEP 12 — RED TEAM
Challenge:
- weakest Key Judgment;
- strongest alternative hypothesis;
- source dependency;
- hidden assumption;
- correlation vs causality;
- overconfident wording;
- missing discriminant;
- recommendation not grounded in evidence;
- detail that belongs in annex;
- privacy / rights / publication risk.

Revise the report after the challenge.

REQUIRED OUTPUT STRUCTURE
0. Mission card
1. Executive Intelligence Summary
2. Key Judgments
3. PIR answers
4. Scope, methodology and constraints
5. Source and evidence register
6. Analytical chronology / phasing
7. Actors, entities and relationship views
8. Mechanisms / levers
9. Competing hypotheses
10. Weak signals, inconsistencies and open questions
11. Vulnerabilities
12. Consequences and risks
13. Recommendations
14. Conclusion
15. Appendices
16. Red-team findings
17. Public-release checklist

QUALITY BAR
The report is not complete because it is long.
It is complete only when:
- the decision layer is concise;
- important claims are traceable;
- uncertainty is visible;
- alternatives are tested;
- recommendations follow from evidence;
- a reviewer can reproduce the reasoning;
- the public version respects rights, privacy and minimisation.

FINAL SELF-CHECK
Before returning the report, state:
- the most fragile judgment;
- the most important missing evidence;
- the strongest alternative explanation;
- the recommendation most sensitive to uncertainty;
- whether the report is ready for public release: PASS / HOLD, with reasons.
```

---

## Benchmark rationale

The standard deliberately combines two complementary reporting qualities observed in DeepThreats 2026:

- **decision-first reporting**: early mission answers, confidence, phasing and action-oriented structure;
- **evidence-deep reporting**: explicit fact/assessment/hypothesis separation, source evaluation, unresolved questions, specialised graphs and owner-oriented recommendations.

The resulting ATOM rule is simple:

> **The depth of the investigation must never slow access to the decision; the brevity of the decision layer must never hide the evidence, limits or uncertainty.**
