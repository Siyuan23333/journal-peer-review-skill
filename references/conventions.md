# Conventions of published reviewer reports, and the user's house style

Evidence base: 148 round-1 reviewer reports from published open peer-review files, analysed by the original author. The corpus is not redistributed (see `corpus.md`). They come from BMC (Springer Nature), Nature portfolio, BMJ / BMJ Open, PLOS, eLife, MDPI and TMLR, and most concern medical-imaging AI. The counts below are numbers of reports. They come from regex scans followed by a hand check, so treat small numbers as approximate. If you have built a corpus, re-check new wording with `scripts/phrase_check.py`.

These rules were settled while writing a full review. Rules marked **(user)** are the original author's personal preferences beyond what the samples show; adapt them to your own style.

## Contents
1. Overall structure
2. Opening: summary paragraph and general-comments paragraph
3. Major comments
4. Minor comments, ending and references
5. Phrasing: what reviewers write and what they don't
6. Mechanics: locations, sentences, length

---

## 1. Overall structure

```
# Reviewer Comments to the Authors
*Manuscript <ID>: “<title>”*
*<one-line note on page/line numbering>*

<summary paragraph, no heading>

<general-comments paragraph, no heading>

## Major Comments
**1. <Topic title>.** <problem paragraph>

<request paragraph>
...
## Minor Comments
Minor comments are listed in page order.

1. Page N, lines a–b: <comment>
...
## References
- <only papers the manuscript does not cite>
```

- **Opening without headings.** Only 3 of about 145 reports put a heading on their opening paragraphs.
- **"Major/Minor Comments" headings.** "Comments" is used in 9 reports (major) and 13 (minor); "Issues" in 4 and 6.
- **No section headings inside Major Comments.** Grouping by manuscript section ("Abstract", "Methods") under Major appears in 1 of 148 reports. Any section grouping at all appears in about 11, mostly short clinical reviews or only in the minor tier.
- **No verdict in the authors' report.** Most samples leave it out. Springer Nature's AI policy also requires the recommendation to be the reviewer's own, so it goes in the confidential box to the editor.

## 2. Opening

### Summary paragraph
- **Order:** describe the work, then assess it. About 28 of 88 summaries do this; it is the most common pattern.
- **Reviewer's framing:** put your characterisation inside the description ("The authors compare three widely used architectures and their ensemble…"). Don't add a separate "In my reading, the study is…" sentence that describes the work a second time.
- **No exact performance values (user).** Only 4 of 88 summaries quote metrics; about 35 give results in words. Counts that support the main concern can be turned into words too ("fewer than half of the cases in the hardest class").
- **Sentence order the user settled on:** comparison → models → data → tasks and evaluation split → results in words.
- **Hedge facts the paper doesn't state.** For example, write "a single train–validation–test split of the images", not "image-level split", if patient-level splitting is unknown.

### General-comments paragraph (no heading)
1. **Relevance sentence:** "The clinical question is relevant, since…"
2. **Strengths, one sentence:** "Strengths of the manuscript include A, B, and C." Announced strength lists are a minority form, but this is the sample wording ("Strengths of the paper include…", Xie R3). Every strength must be literally true; check it.
3. **Pivot:** "However, several issues need to be addressed before the conclusions can be fully assessed." Woznitza R5 is a close sample model.
4. **Concerns:** "My main concerns are X, Y, and Z." Name the topics only, in Major-comment order.

Leave out of this paragraph:
- bullet lists (0 samples have a bulleted list of concerns in the opening);
- explanations of each concern (they duplicate the Major comments);
- the word "revision" or a revision plan (6 of 88 openings use it, almost always tied to a verdict);
- any sentence about how the comments are ordered.

## 3. Major comments

- **Order:** by importance, not manuscript order (the user confirmed this).
- **Title:** a bold run-in topic title ("**2. Possible differences in data acquisition between classes.**"), never a verdict ("The model's superiority is not supported").
- **Two paragraphs:** a problem paragraph, then a request paragraph.
  - In the samples, the request usually closes the same paragraph (22 of 53 long items). A separate request block appears in about 6–8 items in about 4 reports, typically when there are several asks (Woznitza R5; Shu R2 "a) … b) …").
  - The user keeps the split for long, multi-part requests. Short requests are decided case by case.

### Problem paragraph
- **Claim then gap.** Quote the manuscript's claim with its location, then give one observation per sentence, each with its Table/Fig.
  - Sample model (Weiss R1): "On line 132, the authors claim, '…'. But in supplemental Fig. 3B, … This sentence is misleading."
  - Don't list evidence after a colon. No sample does that.
- **Missing items.** Introduce them with "I could not find the following anywhere in the manuscript, including Section X: (a) …; (b) …". Inline (a)/(b) lists are fine inside a comment.
- **Why it matters.** Never write "X matters because…" (no sample uses it). Use one of:
  - "This information would help readers judge whether …, whether …, and how …" (about 10 reports, e.g. BMC wrist R2);
  - the consequence inside the sentence ("…which would inflate test performance"; "…could point toward the wrong treatment decision").
- **Hedge your own reading of figures** ("These observations are based on a few small example images and may not hold for the whole dataset. However, if …"). Then add the mechanism ("This would be expected if the model associated X with class Y").
- **Literature as evidence.** About 18% of reports cite outside literature, for missing related work, a suggested method, or evidence for a concern.
  - Give the number as counts with the key qualifier, matching how manuscript numbers are given: "50/50 in <Author> et al. [n], with <key qualifier>".
  - Verify every number from the full text first (see verification.md).
- **No reviewer-computed statistics (user).** Only 1 of 148 reports computes a new number, and none computes a CI or p-value.
  - Quote the paper's own numbers and judge them in words ("only modestly above the <x>% that would be obtained by always predicting the majority class").
  - Ask the authors to run the test.
- **Credit inside a comment** comes before the concern. Use "It is commendable that…" (8 reports) or "I appreciate…" (2; at most once per report).
- **Overclaims.** Say it kindly and plainly: "…do not yet seem to be supported by the evidence presented"; "…seems too strong"; "…is not convincing".

### Request paragraph
- **One request per problem.** Every problem in the problem paragraph needs a matching request, and every request needs a problem. After you delete a problem, delete its request, and vice versa.
- **Point back instead of restating.** "Please also add the other items listed above, using, for example, <named test> for item (d)."
- **Choose the request form deliberately:**

| Form | Reports | Use for |
|---|---|---|
| Direct question ("How many patients do the <n> images represent…?") | 64 | missing facts or reasoning |
| "Please …" | 43 | add, correct or explain; at most one per paragraph |
| "The authors should … / should consider …" | 25 / 11 | firm requests / optional analyses |
| "I would suggest …" | 21 | analyses, rewording ("I would suggest tempering the claim…") |
| "It would be helpful / interesting …" | 11–16 | secondary requests |
| "Could the authors …?" | 6 | avoid |

- **Mark essential and optional work.** "As an essential step, I would suggest…"; "Alternatively, the authors should consider…".
- **Fallbacks only where the work may really be infeasible** ("If such a subset is too small, please discuss this as a limitation"). For experiments the authors can certainly run, such as ablations, give no fallback and close with "All three comparisons are needed to support the stated contributions." **(user)**
- **Name tests concretely** (DeLong's test for AUC; McNemar's test or a paired bootstrap for accuracy; Mann–Whitney U; chi-squared).
- **Suggesting an uncited paper.** "I would also suggest discussing the study by <Author> et al. (<year>), “<full title>”, which evaluated …". Say what is shared and what differs, so the comparison is fair. Check it against the full text first.
- **No reporting-checklist pointers** (CLAIM/STARD/TRIPOD). No sample points authors to one for a primary study. **(user)**
- **The Discussion/limitations comment** can gather the fallbacks: "If the additional analyses suggested above are not performed, the limitations should cover … (Major comment 1), … (Major comment 2), …".

## 4. Minor comments, ending and references

- **Strict page order, no exceptions (user).** Each item starts with its location key: "Page 9, lines 15–17:". Multiple locations look like "Page 6, lines 6–7; Fig. 1; page 12, lines 39–40:".
- **Substantive points only (user).** The user cut typo fixes, citation-order notes, hyperparameter-table requests, "shorten the backbone descriptions" and Abstract jargon notes. Keep factual errors, duplicated passages, claims with nothing shown, misplaced content, inconsistent task descriptions, and missing key numbers in the Abstract.
- **Each item must be literally accurate.** Verify location and claim with subagents (verification.md §3). Typical overstatements to watch for:
  - "not shown" when it is partly shown;
  - "paragraph" when it is two sentences;
  - attributing words the text doesn't use.
- **No closing sentence.** About 8 in 10 samples end on the last comment, and the user deleted the closing.
- **References heading:** "## References" (3 samples), or a bare list (3). "Additional References" (0) and "References Cited in This Report" (0) are not used. List only papers the manuscript does not cite. Cite manuscript references by their number ([18]).

## 5. Phrasing: rare in samples, and the common replacement

| Avoid (sample count) | Write instead (sample count) |
|---|---|
| "X matters because" (1, other sense) | "This information would help readers judge whether…" (~10) or state the consequence |
| "Could the authors …?" (6) | direct question (64) or "Please …" (43) |
| "[analysis] would address this" (0) | "Please …" / "I would suggest …" |
| "may wish to" (1) | "the authors should consider …" (11) |
| "would be more accurate / more accurately described" (0) | "should be described as …"; "I would suggest tempering the claim…" |
| "would be the most convincing test" (0) | "would be particularly informative" (would be helpful/informative: 30) |
| "may be a useful comparison" (0) | "I would also suggest discussing the study by …" (~25 cite/discuss requests) |
| "results do not (yet) support…" (0) | "seems too strong" (10) / "is not convincing" (6) |
| "revised to match the evidence" (0) | "toned down" / "tempered" (7) |
| "go beyond what was evaluated" (2) | "overstate" (7) |
| "difficult to reconcile with" (0) | "inconsistent with" (18) |
| "call for caution" (paraphrasing the authors) | quote them: "…“should be interpreted cautiously” (p. <n>, line <m>)" |
| "might not transfer to clinical use" (1) | "might not generalize to clinical practice" |
| "should read" (0) | "should be replaced with" |
| "would fit better in" (0) | "would be better placed in" (Russe R5) |
| "The text appears to swap…" | "The text appears inconsistent with …" |
| "performs about as well as" | "comparable to" |
| "which is not self-evident" | "which is not clear" |
| "coned view" (jargon) | "a narrower field of view centered on…" |
| "by my calculation" (1 of 148 compute anything) | drop it and ask the authors to test |
| "essential revisions" in the opening | "My main concerns are…" |
| "I hope these comments are helpful…" (closing) | no closing |

These are fine and attested: "Strengths of the manuscript include", "My main concerns are", "I could not find", "I would suggest", "It would be helpful", "Please also…", "the authors should consider", "seems too strong", "only modestly above", "As the authors note", "Although study designs differ".

## 6. Mechanics

- **Locations.** Write "(p. 1, lines 12–13)" in the text and "Page 9, lines 15–17:" as a minor key. Spell out "line/lines" and never write "l./ll.".
  - Always give the page, because Editorial Manager PDFs restart line numbers on every page.
  - Text above line 1 is "(p. 5, top of page)".
  - Keep the italic note under the title that explains this.
- **Where to put line numbers.** Use them for quotes and checkable facts. A Table/Fig/Section pointer alone is enough otherwise. Don't add line ranges to a section pointer ("Section 3.1", not "Section 3.1 (p. 4, lines 26–55)"); 1 of about 105 sample section pointers does.
- **Density.** About 13 or fewer page/line citations per 1,000 words; the sample median is about 6.
- **Sentences (user).**
  - About 40 words at most.
  - No semicolons or mid-sentence colons in comment prose: split the sentence instead. Inline (a)/(b) lists and the minor location key are fine.
  - At most one "Please" and one sentence opening with "However" per paragraph where possible.
- **Plain terms over jargon** ("field of view", not "coned"). Use the same term for a concept throughout ("view" vs "projection").
- **Length.** Aim for 2,500 words or fewer before the references. The samples run about 400–1,300.
- **Kind but direct.** Use "does not appear to", "I could not find", "seems too strong", "do not yet seem to be supported", "is not convincing". Avoid "contradicted", "not justified", "shows otherwise", "useless".
