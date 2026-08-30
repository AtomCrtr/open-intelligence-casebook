# Open Intelligence Casebook - Public Edition Design

## Purpose

Create a clean, public-facing edition of the private `osint-intelligence-casebook` portfolio without exposing the private repository history, internal audits, working branches, non-redistributable data, personal data, or intermediate research artifacts.

The public edition is intended for recruiters, analysts, decision-makers, students, and non-specialist readers. It must remain analytically rigorous while being understandable without prior OSINT, supply-chain, FIMI, DISARM, or GEOINT knowledge.

## Publication model

The private repository remains the canonical working repository. The public repository `AtomCrtr/open-intelligence-casebook` is a fresh-history sanitized publication surface.

No Git history from the private repository is copied. Every public file is either:

- original explanatory material written for the public edition;
- a sanitized copy of a previously audited public-ready artifact;
- a derived table or figure whose redistribution is explicitly permitted;
- a generated report based on already validated analytical results;
- a methodology, attribution, licence, transparency, or disclaimer file required for responsible publication.

The public repository must not contain raw third-party datasets unless redistribution is explicitly permitted.

## Scope of the first public release

### Case 01 - Titanium supply-chain resilience

Status: complete and publishable from the previously audited public snapshot.

Public edition contents:

- concise case landing page;
- detailed public report in Markdown;
- polished public PDF report;
- selected figures and derived tables needed to understand the conclusions;
- methodological notes explaining HHI, source limitations, qualification gates, scenario analysis, and confidence levels;
- source and attribution register limited to public-safe entries.

The public report must preserve the central distinction:

`commercial availability != aerospace qualification != customer approval != operational substitutability`.

It must also preserve the distinction between trade data covering all industries and the aerospace-specific decision question.

### Case 02 - Portal Kombat / Pravda information integrity

Status: analytical report complete; publication package requires its own sanitized-rights verification before final release.

Public edition contents:

- concise case landing page;
- detailed public report in Markdown;
- polished public PDF report;
- public-safe figures explaining chronology, network structure, dissemination, France/UE focus, ACH, and confidence levels;
- public-safe derived counts and tables;
- methodology explaining passive OSINT, graph sensitivity analysis, DISARM use, triangulation, and competing hypotheses;
- source links and attribution without redistributing third-party raw corpora whose upstream licence is uncertain or review-required.

The report must not claim state attribution, editorial command, measured human impact, or demonstrated LLM poisoning where the evidence does not support those conclusions.

### Case 03 - GNSS interference and European civil aviation

Status: work in progress.

The first public release contains only a short teaser describing the research question, methods under development, and current status. It must explicitly state that the analytical design is frozen before real trajectory observations and that no historical GNSS-interference conclusion is published yet.

No Case 03 working data, branch history, GPSJAM bulk data, aircraft identifiers, event outputs, or synthetic fixtures are published in the first public release.

## Public repository information architecture

```text
README.md
LICENSE
NOTICE.md
DISCLAIMER.md
AI_TRANSPARENCY.md
CONTRIBUTING.md

cases/
  case-01-titanium/
    README.md
    report.md
    report.pdf
    figures/
    data/
    methodology.md
    sources.md

  case-02-portal-kombat/
    README.md
    report.md
    report.pdf
    figures/
    data/
    methodology.md
    sources.md

  case-03-gnss-interference/
    README.md

methodology/
  analytical-cycle.md
  source-evaluation.md
  confidence-and-hypotheses.md
  reproducibility.md

publication/
  public-manifest.csv
  rights-review.md
  release-checklist.md
  checksums.sha256

docs/superpowers/
  specs/
  plans/
```

## README design

The root README acts as the portfolio home page and must be understandable in under two minutes.

It contains:

1. one-sentence purpose statement;
2. short explanation of what an intelligence casebook is;
3. cards or compact sections for Case 01, Case 02, and Case 03;
4. direct links to the two finished public PDFs;
5. a transparent status label for every case;
6. key demonstrated capabilities: OSINT, GEOINT, data engineering, evidence traceability, ACH, uncertainty management, and reproducibility;
7. a short common-method diagram;
8. publication and ethics principles;
9. links to methodology, AI transparency, licence, notice, and disclaimer.

The README must not overstate expertise or present analytical hypotheses as established facts.

## PDF editorial design

Two public reports are produced for the first release, one per completed case.

Target length: approximately 20-30 A4 pages per report, allowed to vary when clarity requires it.

Each report uses the same visual identity so the portfolio reads as one publication series.

### Shared report structure

1. cover page;
2. document status, date, scope, and diffusion level;
3. "In two minutes" executive summary;
4. five to eight key numbers or findings;
5. question and why it matters;
6. methodology explained in plain French;
7. evidence and main findings;
8. visual chronology and/or analytical flow;
9. competing hypotheses and confidence levels;
10. what the evidence does not establish;
11. implications and conditional recommendations;
12. reproducibility and source traceability;
13. glossary;
14. selected sources and full-source navigation.

### Visual principles

- modern institutional / intelligence-report aesthetic;
- generous whitespace;
- strong hierarchy and page navigation;
- readable body text at normal zoom;
- no dense decorative backgrounds;
- charts used only when they clarify a conclusion;
- every chart includes title, period, unit, source, and limitation note;
- callout boxes for "A retenir", "Limite", "Niveau de confiance", and "Ce que cela ne prouve pas";
- colour must never be the sole carrier of meaning;
- tables should be simplified for non-specialists and detailed evidence moved to appendices when needed;
- clickable source references where technically reliable.

### Case 01 visual content

The report should include, where supported by publishable data:

- six-product HHI comparison 2017 vs 2025;
- dominant-origin comparison;
- trade composition view with explicit double-counting warning;
- industrial maturity vs aerospace-qualification diagram;
- qualification/substitution gate diagram;
- scenario and options matrix;
- key limits of customs data.

### Case 02 visual content

The report should include, where supported by public-safe derived data:

- timeline from 2013 through the 2024/2025 expansion phases;
- network-structure explainer rather than an unreadable full graph dump;
- graph sensitivity table or visual;
- France/UE focus panel;
- dissemination panel for Wikipedia and X observations;
- competing-hypotheses / ACH view;
- distinction between visibility, coordination, attribution, and impact;
- explicit unresolved LLM-grooming vs information-gap question.

## Accessibility and broad-audience rules

The main narrative is written in French, with English terminology retained only when useful and defined on first use.

Every technical term that a general reader may not know must either be explained inline or included in the glossary.

Charts must have text captions that summarize the takeaway. Tables must remain legible on A4 without requiring zoom beyond normal reading conditions.

Reports must not depend on colour alone and should maintain usable contrast when printed in greyscale.

## Evidence integrity rules

Every numerical statement in a public report must trace to an existing validated analysis result or an explicitly documented public-safe derivation.

No new causal conclusion is introduced only for editorial effect.

The public reports keep separate labels for:

- observed;
- reported;
- corroborated;
- inferred;
- hypothesis;
- not demonstrated.

Confidence language must match the underlying casebook.

## Privacy and operational-safety rules

The public edition excludes:

- secrets, tokens, credentials, local paths, machine names, or private e-mail addresses;
- unnecessary personal data;
- raw account identifiers where anonymisation was part of the canonical publication policy;
- private aircraft identifiers, callsigns, stable ICAO24 hashes, or sensitive trajectory records;
- private audit logs and working notes;
- any content whose publication could be mistaken for a live operational warning or navigation product.

## Rights and attribution rules

Case 01 publication follows the already passed sanitized snapshot rights model.

Case 02 gets an explicit public-package rights review before release. Upstream material marked review-required is linked and described, not copied into the public repository unless redistribution permission is independently established.

Original code and original analytical text receive an explicit licence. Third-party material retains its original conditions and is documented in `NOTICE.md` and case-specific source pages.

## AI transparency

`AI_TRANSPARENCY.md` must state that generative AI may assist with drafting, code generation, formatting, or editorial transformation, while source selection, evidence evaluation, analytical judgements, validation, and publication decisions remain subject to human review.

The public PDF reports must include a short transparency note and direct readers to the repository file for details.

## Reproducibility

The public edition should provide enough methodology and derived artifacts for readers to understand and, where rights permit, reproduce the published results without requiring access to the private canonical repository.

Where raw data cannot be redistributed, the public repository documents:

- the upstream source;
- collection or snapshot date where relevant;
- transformation logic;
- schema or expected fields;
- checksums for redistributable public artifacts;
- the exact limitation preventing raw-data publication.

## Release gate

The repository is not considered release-ready until all of the following pass:

- no private-history copy;
- public manifest exactly matches intended files;
- secret and privacy scan clean;
- no local paths or machine identifiers;
- PDF metadata reviewed;
- internal links valid;
- report source claims reviewed against casebook evidence;
- Case 01 rights inherited only from the validated public snapshot scope;
- Case 02 rights review contains no unresolved redistribution blocker for any copied artifact;
- third-party materials with unclear rights are link-only;
- PDF render review confirms no clipping, overlap, broken glyphs, or unreadable tables;
- checksums generated for final PDF reports;
- AI transparency, notice, disclaimer, and licence visible from the first-minute navigation;
- final independent release checklist records PASS.

## Success criteria

A non-specialist should understand the central question, the main findings, the limitations, and the meaning of the confidence level of either case within ten minutes.

A technical reviewer should be able to trace important claims to public source references and understand the derivation without needing the private repository.

A recruiter should be able to identify demonstrated skills in OSINT, GEOINT, data engineering, structured analysis, reproducibility, uncertainty management, and decision-oriented communication from the root README and the first five pages of either PDF.
