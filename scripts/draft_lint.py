#!/usr/bin/env python3
"""Lint a review draft (Markdown) against the user's established conventions.

Checks are heuristics that flag things to look at, not automatic edits:
  * length (words before the reference list; target <= ~2,500) and page/line
    citation density (target <= ~13 per 1,000 words);
  * phrasings the user rejected or the samples rarely use (see references/conventions.md);
  * more than one "Please" or "However" opening sentences in one paragraph;
  * semicolons and mid-sentence colons inside comments (the user prefers splitting);
  * sentences longer than 45 words;
  * repeated words that read badly when close together ("also", "seems too strong").

Usage: draft_lint.py review.md
"""
import re, sys

RARE = [
    (r"\bmatters? because\b", 'replace "X matters because" with "This information would help readers judge…" or state the consequence'),
    (r"\bCould the authors\b", 'use a direct question ("How many…?") or "Please…"'),
    (r"\bwould address this\b", 'use "Please…" / "I would suggest…"'),
    (r"\bmay wish to\b", 'use "the authors should consider…" / "it would be interesting…"'),
    (r"\bwould be more accurate(?:ly)?\b", 'use "should be described as…" or "I would suggest tempering…"'),
    (r"\bby my calculation\b|\bmy own calculation\b", "drop own statistics; quote the paper's numbers and ask the authors to run the test"),
    (r"\bmost convincing\b", 'use "would be particularly informative"'),
    (r"\buseful comparison\b", 'use "I would also suggest discussing <study>"'),
    (r"\bdifficult to reconcile\b", 'use "inconsistent with"'),
    (r"\bgo(?:es)? beyond what\b", 'use "overstate"'),
    (r"\bresults do not (?:yet )?support\b", 'use "seems too strong" / "is not convincing"'),
    (r"\bto match the evidence\b", 'use "toned down" / "tempered"'),
    (r"\bshould read\b", 'use "should be replaced with"'),
    (r"\bfit better in\b", 'use "better placed in"'),
    (r"\bnot transfer to\b", 'use "not generalize to"'),
    (r"\bessential revisions?\b|\bmajor revision\b|\bminor revision\b|\baccept\w*\b|\breject\w*\b", "no verdict / revision-plan language in the authors' report"),
    (r"\bCLAIM\b|\bTRIPOD\b|\bSTARD\b|\bchecklist\b", "samples do not point authors to reporting checklists"),
    (r"\bI hope these comments\b", "no closing line (most samples end with the last comment)"),
    (r"\b(?:l\.|ll\.) ?\d", 'spell out "line"/"lines"'),
]


def main(path):
    text = open(path).read()
    body = re.split(r"\n## References", text)[0]
    words = len(re.findall(r"\b[\w’'-]+\b", body))
    cites = len(re.findall(r"\bp\. \d+|\bPages? \d+|\bpage \d+", body))
    print(f"words before references: {words}  (target <= ~2,500)")
    print(f"page/line citations: {cites}  = {cites / max(words, 1) * 1000:.1f} per 1,000 words (target <= ~13)\n")

    print("== rare or rejected phrasings")
    for rx, fix in RARE:
        for m in re.finditer(rx, body):
            ln = body.count("\n", 0, m.start()) + 1
            print(f"  line {ln}: '{m.group(0)}' -> {fix}")

    print("\n== paragraph-level checks")
    for pi, para in enumerate(body.split("\n\n")):
        ln = body.count("\n", 0, body.find(para)) + 1
        p = para.strip()
        if not p or p.startswith("#"):
            continue
        p = re.sub(r"\*\*[^*]+\*\*\s*", "", p)                       # bold run-in titles
        p = re.sub(r"^\d+\.\s+Pages?\b[^:]*:\s*", "", p)            # minor-comment location key
        sents = [s for s in re.split(r"(?<=[.?!])\s+(?=[A-Z“\"(])", p) if len(s.split()) > 1]
        n_please = sum(1 for s in sents if s.startswith("Please"))
        n_however = sum(1 for s in sents if s.startswith("However"))
        if n_please > 1: print(f"  line {ln}: {n_please} sentences start with 'Please'")
        if n_however > 1: print(f"  line {ln}: {n_however} sentences start with 'However'")
        for s in sents:
            core = s
            nw = len(core.split())
            flat = re.sub(r"\([^()]*\)", "", core)                    # ignore ';' and ':' inside parentheses
            if nw > 45: print(f"  line {ln}: long sentence ({nw} words): {core[:80]}…")
            if ";" in flat and not re.search(r"\([a-h]\)", core): print(f"  line {ln}: semicolon: …{flat[max(0, flat.find(';') - 40):flat.find(';') + 30]}…")
            inner = flat[:-1]
            if re.search(r"[a-z)]: [a-z(“A-Z]", inner) and not re.search(r"\b(?:including|following)[^:]*:", inner):
                print(f"  line {ln}: mid-sentence colon: {core[:90]}…")

    print("\n== repetition across the draft")
    for w in ["also", "However", "Please", "I would suggest", "seems too strong", "particularly", "I appreciate"]:
        n = len(re.findall(r"\b" + re.escape(w) + r"\b", body))
        print(f"  {w!r}: {n}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    main(sys.argv[1])
