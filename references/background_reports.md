# Stage 1: optional background notes (for the reviewer's own reading)

Only produce these if the user asks. They are fact-finding notes the reviewer may consult while writing their own draft. They describe facts and where they are found. They never list, rank or recommend criticisms, and they never suggest what the review or the recommendation should be. They are working files, kept out of the review itself; nothing from them enters the review unless the user puts it in their draft.

Folder layout (one folder per manuscript, named by the manuscript ID):
```
<ID>/
  <ID>.pdf                    manuscript (never upload or search it online)
  manuscript.txt              plain text (pypdf); manuscript_lines.txt from `locate.py PDF dump`
  logic/                      Narrative_Logic_Report_<ID>.md, reading_notes.md, figures/, recompute_metrics.py
  lit_journal/                journal guidelines, reviewer checklists, convention notes
  lit_topic/                  notes/, pdf/ (full texts), search/, claims/
  Literature_Review_Report_<ID>.md        (journal conventions)
  Topic_Literature_Review_Report_<ID>.md  (state of the art)
  Claim_Verification_Report_<ID>.md
  review/                     reading_notes.md, the user's own draft, samples/ (optional extra corpus)
  review_final/               <ID>_review_final.md, sample_comparison_notes.md, archive/
```

## 1.1 Internal-consistency notes
Read the whole paper, including every table and figure. Rendering pages helps. Record factual findings, grouped by type, without severity ratings or scores:
- **A, numbers that disagree.** Headline claims that the paper's own numbers contradict; arithmetically impossible values; text vs figure mismatches such as swapped confusion-matrix classes; three different values for the same metric.
- **B, wording versus what was done.** Framing words ("multi-task", "hierarchical", "robust", "explainable") versus what was done. Gap statements contradicted by the paper's own literature review. Claimed component benefits never tested. Missing Discussion or limitations. Unsupported clinical-impact claims.
- **C, local mismatches.** Cross-reference mismatches.
- **D, editorial issues.**
- **E, facts verified as consistent.** Saying what was checked prevents false alarms.

Recompute metrics from confusion matrices with a small script (`recompute_metrics.py`).

## 1.2 Journal-convention report
- **The journal's requirements.** Get the author guidelines (declarations, reporting standards, double-blind rules: where are ethics statements placed?) and any reviewer checklists the journal or society publishes (for imaging-informatics journals, e.g. SIIM "Best Practices and Checklist for Reviewing AI-Based Medical Imaging Papers: Classification", 2025; the DL reproducibility checklist, 2024).
- **How published papers in the journal and field are built.** Title and abstract, section architecture, paragraph moves in the Introduction and Discussion, data/ethics/reference-standard reporting, splitting and validation, statistics, the metrics expected, the limitations usually acknowledged, and where the bar sits.
- **Springer Nature reviewer guidance and its AI-in-peer-review policy.**

## 1.3 Topic literature review (state of the art)
Build a corpus through Europe PMC, OpenAlex, arXiv and Unpaywall. Search the topic, never the manuscript's title or text. Prefer full texts (PMC XML, arXiv). Organize the corpus by cluster:
- direct comparators (same task and classes);
- broader task family;
- methods novelty (ensembles, multi-task, preprocessing, explainability);
- standards and pitfalls (shortcut learning, confounding, saliency validity).

Write one note per paper, using the template below. Then synthesize:
- a benchmark table;
- typical performance;
- whether the manuscript's components are new;
- public datasets for external testing;
- documented pitfalls that apply.

Note template (`lit_topic/NOTE_TEMPLATE.md`):
```
# <First author> <Year> — <short title>
- Venue / DOI / PMID / PMCID / arXiv; Access: FULL TEXT (file) | ABSTRACT ONLY; Cluster; Tier (T1 comparator / T2 supporting)
## 1. One-paragraph summary (task, data, model, headline result)
## 2. Task definition & label space (classes verbatim; views; detection vs classification)
## 3. Data & reference standard (centres, patients vs images, class counts, split level, external test, reference standard, annotators, exclusions, availability)
## 4. Methods (backbones, input size, pretraining, ROI step, ensembling and how the meta-learner was trained, multi-task design, preprocessing, augmentation, TTA, explainability and whether it was evaluated)
## 5. Evaluation & results (exact numbers with CIs; per-class; external drop; reader study; statistics)
## 6. Comparability to the manuscript (same task/metric? is the claimed novelty already done? methodological contrast)
## 7. Limitations acknowledged / our caveats
## 8. Quotable statements (<= 25 words, with page/section)
```

## 1.4 Claim verification
Extract every reviewer-facing claim from reports 1.1–1.3. Re-verify each against full texts with subagents (verification.md §2). Record:
- material corrections that change conclusions;
- numerical or wording fixes;
- what an expanded search found;
- the residual risk for claims that rest only on abstracts.

Propagate corrections to the notes. Literature notes are often wrong in details: config, denominators, mixed results.

## 1.5 Reading notes
`review/reading_notes.md` is a factual digest: what the paper did (data, design, models, evaluation), where each key fact is (page/line, Table/Fig.), and the related papers with their verified numbers.

Do **not** produce a weakness list, a strengths list, suggested fixes, questions for the authors, or a recommendation. Those come from the user's own draft. That keeps the evaluation the reviewer's own, as Springer Nature's policy requires.

## Exclusions
- **No authorship or provenance inference** (who the authors might be, from style, data source or citations). The review is double-blind. If such notes exist from an earlier session, they must never reach the author-facing text.
- **No online upload of manuscript text**, figures or the title, including in search queries.
