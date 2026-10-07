# journal-peer-review: a Claude Code skill

This skill turns a reviewer's own draft into a polished journal peer-review report (comments to the authors).

## Scope: it polishes your review, it does not write it

**This skill does not review the manuscript for you.** It starts from an initial draft that you, the human reviewer, have written. That draft must already:
- list the strengths and weaknesses you want to raise, and say which concerns are major or minor;
- reflect your own recommendation (accept, minor revision, major revision or reject). You submit it separately, in the confidential comments to the editor.

From that draft, the skill only helps you:
- **paraphrase** your points into clear, kind, conventional reviewer language;
- **reorganize** them into the standard journal structure;
- **check** the structure and phrasing against conventions measured on published reviews;
- **verify** that every quote, number and page/line reference in your draft is correct.

It does not add criticisms of its own, decide which issues matter, or make the recommendation decision. This follows publisher policies on AI in peer review, such as Springer Nature's, which keep the evaluation and the recommendation with the human reviewer. Check your journal's policy, and declare any AI assistance it requires.

**Required input:** the manuscript PDF and your initial draft, in any format, even rough bullet points.

## What it does
1. **Setup.** Builds a folder layout, extracts the manuscript text, and dumps every line with its page and margin line number.
2. **Background notes (optional, for your own reading).** Fact-finding notes on internal consistency, the journal's conventions and the topic literature (from full texts). You may consult them while writing your draft. They don't replace it, and nothing goes into the review unless you put it in your draft.
3. **Conversion.** Paraphrases and reorganizes your draft into the conventional journal format:
   - an unheaded summary;
   - an unheaded general-comments paragraph;
   - Major Comments ordered by importance;
   - Minor Comments in strict page order.
4. **Convention check.** Compares structure and phrasing with conventions documented from 148 published round-1 reviewer reports. If you build a corpus for your own field, it checks against that too.
5. **Paragraph-by-paragraph editing.** Claude verifies the facts in each paragraph, then proposes Current/Proposed/Why. Nothing changes until you say "apply", and the session never moves on until you say "move on".
6. **Final pass.** Runs the style check, a phrase-frequency pass, and subagent verification of every page/line reference and cited number.

The skill never uploads or searches manuscript text online, and never attempts to identify the authors.

## Install
```bash
git clone https://github.com/Siyuan23333/journal-peer-review-skill ~/.claude/skills/journal-peer-review
pip install pymupdf      # needed by scripts/locate.py
```
Claude Code picks the skill up automatically. Invoke it with `/journal-peer-review`, or just ask Claude to help polish your review of a manuscript.

## Optional: your own sample corpus
The 148 reports behind the documented conventions are **not** included, because publishers' reuse terms vary. To check new phrasings, or to adapt the conventions to your field, collect 30–150 open reviewer reports. Then run:
```bash
python scripts/build_corpus.py path/to/reports_txt --meta sources.csv --split
python scripts/phrase_check.py "could=\bCould the authors\b" "please=^Please\b"
```
`references/corpus.md` lists where to find open reviewer reports and gives licence notes. The built corpus (`assets/sample_reports.json`) is git-ignored.

## Contents
| Path | Purpose |
|---|---|
| `SKILL.md` | Scope, ground rules and pipeline stages (loaded when the skill triggers) |
| `references/conventions.md` | Evidence-based house style: structure, request forms, and a table of rare phrasings with common replacements, with sample counts |
| `references/line_by_line.md` | Protocol for the interactive editing pass |
| `references/verification.md` | Fact checks and subagent prompt templates |
| `references/background_reports.md` | Specifications for the optional background notes (factual only) and the literature-note template |
| `references/report_template.md` | Report skeleton with a sentence pattern for each kind of problem |
| `references/corpus.md` | Building your own corpus of published reviewer reports |
| `scripts/locate.py` | Map text to manuscript page and margin line; dump, page view, render |
| `scripts/phrase_check.py` | "Is this phrasing common?" Counts and examples from your corpus |
| `scripts/build_corpus.py` | Build the corpus JSON from plain-text reports |
| `scripts/draft_lint.py` | Check a draft for rare phrasings, semicolons and colons, long sentences, length and citation density |

## Notes
- **Personal defaults.** The style defaults reflect the original author's preferences in one field (medical-imaging AI). Treat them as defaults and adapt them.
- **Confidentiality.** Never commit review drafts, manuscripts or reviewer-report texts to a public repository.
