# Building a sample corpus of published reviewer reports

`scripts/phrase_check.py` answers "do reviewers really write it this way?" by counting phrasings in a corpus of real reviewer reports.

The counts in `conventions.md` come from the original author's corpus. That corpus held 148 round-1 reports, mostly on medical-imaging AI, from BMC, Nature portfolio, BMJ / BMJ Open, PLOS, eLife, MDPI and TMLR. It is **not** included in this repository, because reuse terms differ between publishers.

The documented counts work without any corpus. To check new wording, or to adapt the conventions to your field, build your own corpus.

## Where to find open reviewer reports
| Source | Where | Usual licence (check each item) |
|---|---|---|
| BMC journals (Springer Nature) | "Peer Review reports" on the article page, for journals with open peer review | CC BY |
| Nature portfolio (Nature Communications, Communications Medicine, Nature Biomedical Engineering, etc.) | "Peer Review File" PDF under Supplementary Information | follows the article; open-access articles are usually CC BY |
| PLOS (Medicine, Digital Health, ONE, …) | "Peer Review History" tab, when the authors opted in | CC BY |
| eLife | public reviews and decision letters (also available through the eLife API) | CC BY |
| MDPI | "Review Reports" link, when published | CC BY |
| F1000Research / Wellcome Open Research | referee reports shown with each article | CC BY |
| OpenReview venues (e.g., TMLR) | forum pages or the OpenReview API | check the venue's terms |
| The BMJ / BMJ Open | "Peer review" / prepublication history | BMJ terms; often not freely reusable |

Prefer papers close to the manuscripts you review: the same publisher, field and article type. Aim for 30–150 round-1 reports. Use only the reviewers' comments to the authors. Drop author responses, editor letters and later rounds.

## Building the corpus file
1. Save each report, or each peer-review file, as plain text in a folder (e.g. with `pdftotext` or a PDF library).
2. Optionally write `sources.csv` with the columns `file,publisher,source_url,licence`.
3. Run `python scripts/build_corpus.py <folder> --meta sources.csv --split`. Check a few split reports by hand.
4. `phrase_check.py` then uses `assets/sample_reports.json` by default. The file is git-ignored, so it stays on your machine.

Use the corpus only to count conventions. Don't copy wording from it into reviews, and don't redistribute reports whose licence doesn't allow it.
