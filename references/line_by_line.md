# Paragraph-by-paragraph editing protocol

The user does the final polish together with Claude, one paragraph at a time. This is where most of the quality comes from, and the user is strict about pacing. Follow this protocol exactly.

## Pacing
- Work through the draft in order: title note → summary → general comments → Major 1 problem → Major 1 request → … → minor comments → references.
- Label each step, e.g. "## Part 7: Major comment 3, problem paragraph (line 21 of the draft)".
- **Do not move to the next paragraph until the user says so** ("move on", "next"). If the user says "go back to X", stay on X. Questions and edits on the current paragraph don't mean "move on".
- If the user asks about a different paragraph, answer it and then return to the current one.

## Before proposing anything for a paragraph
1. **Verify every fact in it against the manuscript:**
   - quotes and their locations with `scripts/locate.py find`;
   - numbers against the tables and text;
   - figures by rendering the page and looking at it.
   - Say in one or two lines what you checked and what you found, including anything already wrong ("the quoted words are on line 45, not 43–46").
2. **Check the cited literature from full texts.** Use subagents for this (verification.md §2). Never rely on memory or on the manuscript's description of another paper.
3. **Check wording against conventions.md.** For anything that may be unusual, run `scripts/phrase_check.py` before proposing it.

## Proposal format
For each sentence that should change:

**S2**
- **Current:** "…"
- **Proposed:** "…"
- **Why:** one or two sentences, citing the sample evidence or the fact you checked.

- List unchanged sentences in one line ("S1, S3: no change").
- When there are several changes, end with the full proposed paragraph in a blockquote.
- Keep each proposal minimal. Don't rewrite sentences the user didn't ask about unless something is wrong in them.

## Applying changes
- **Proposals:** apply only when the user says so ("apply", "apply the changes", "apply R1 and R3"). "Apply the changes" means all pending proposals for the current paragraph.
- **Direct instructions** ("Delete this sentence", "Change X to Y", "Add the short clause", "Use 'The authors should consider'"): apply immediately and show the result. Don't ask for confirmation.
- **Highlighted text:** if the instruction is ambiguous about which text, the user's highlighted text usually is the target. If the quoted text is already gone, say so and ask whether they meant the highlighted text.
- **After every edit**, show the changed sentence or paragraph in a blockquote. Edit the file with exact-string replacement that fails if the string isn't found exactly once. Keep `“ ”` quotes and en dashes (–).
- **"Go back to the previous version":** restore exactly. Keep the previous wording in your head, or check `review_final/archive/`.

## Ripple checks after any edit (report or fix)
- **Orphaned items.** A request whose problem was deleted, or a problem whose request was deleted. Flag it: "The request paragraph still asks for X; nothing supports it now. Delete?" If the user has said to delete such things, delete them directly.
- **Grammar that now breaks.** "As essential steps" with one step left, "also" with nothing before it, "As a result" without a cause, two "Please" or "However" sentences in one paragraph. Fix small grammar consequences directly and mention them.
- **Cross-references.** "Major comment 2", item letters "(d)", minor-comment numbers. Renumber minor comments when items are removed or moved.
- **The opening.** Does the general-comments concern list still match the Major comments?
- **References.** Is any reference-list entry no longer cited, or any new citation missing from the list?

## When the user asks "Is this common?" / "Should we…?"
1. Check `references/conventions.md` first. If a local corpus exists, run `scripts/phrase_check.py` with the exact wording and a broader family regex. For structure questions, write a short ad-hoc script over `assets/sample_reports.json`.
2. Answer in this shape:
   - **First:** a direct one-line answer.
   - **Then:** a small table of counts with one or two verbatim sample quotes (journal and reviewer).
   - **Then:** a recommendation with a ready-to-apply rewrite.
   - Say when counts are approximate.
3. Append the evidence as a new numbered section of `review_final/sample_comparison_notes.md`, marked as a recommendation pending the user's choice. Update it once the user decides.
4. Don't apply the change until the user says so.

## Verification requests ("verify these numbers", "check correctness")
- Use subagents, local files only, in parallel batches. See verification.md for prompt templates.
- Report the verdict first (correct / needs qualification / wrong), then the evidence, then the proposed wording.

## Remembering
When the user settles a reusable preference (a phrase, structure, or something to never do), save it to Claude's memory and, if it is general, add it to this skill's conventions.md.

## Tone of your replies
- Be brief. The user reads every proposal.
- Don't re-explain the protocol, and don't recap earlier paragraphs.
- End with what is still pending for this paragraph, then "I'm staying on this paragraph."
