#!/usr/bin/env python3
"""Count how often a phrasing (or a family of phrasings) appears in published reviewer reports.

Use it whenever the user asks "is this phrasing / structure common?" or before
proposing wording. Report BOTH the exact wording and its broader family: a
zero count for exact wording is normal in a small corpus; a zero for the whole
family means reviewers genuinely do not write it that way.

Corpus: ../assets/sample_reports.json, which you build yourself with scripts/build_corpus.py (see
references/corpus.md); it is not bundled because reviewer reports carry varied licences.
Format: {"reports": [{"id", "source_file", "publisher", "reviewer", "text"}]}; pass another file with --corpus.

Usage
  phrase_check.py "label=regex" ["label=regex" ...] [--examples 3] [--corpus PATH] [--case]
  phrase_check.py --file phrases.tsv          # one "label<TAB>regex" per line
Regexes are Python regexes, case-insensitive unless --case is given.
Output: number of reports (and sentences) matching, plus example sentences with their source.
"""
import json, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
DEFAULT = os.path.join(HERE, "..", "assets", "sample_reports.json")


def sentences(text):
    t = re.sub(r"\s+", " ", text)
    return re.split(r"(?<=[.?!])\s+(?=[A-Z“\"(\[])", t)


def main(argv):
    corpus, nex, case, specs = DEFAULT, 3, False, []
    i = 1
    while i < len(argv):
        a = argv[i]
        if a == "--corpus": corpus = argv[i + 1]; i += 2; continue
        if a == "--examples": nex = int(argv[i + 1]); i += 2; continue
        if a == "--case": case = True; i += 1; continue
        if a == "--file":
            for line in open(argv[i + 1]):
                if line.strip() and not line.startswith("#"):
                    lab, rx = line.rstrip("\n").split("\t", 1); specs.append((lab, rx))
            i += 2; continue
        lab, _, rx = a.partition("=")
        specs.append((lab, rx) if rx else (a, a)); i += 1
    if not specs:
        sys.exit(__doc__)
    if not os.path.exists(corpus):
        sys.exit(f"No corpus at {corpus}. Build one with scripts/build_corpus.py (see references/corpus.md), "
                 "or rely on the counts documented in references/conventions.md.")
    reps = json.load(open(corpus))["reports"]
    flags = 0 if case else re.I
    print(f"corpus: {len(reps)} reports ({os.path.basename(corpus)})\n")
    for lab, rx in specs:
        pat = re.compile(rx, flags)
        nrep = nsent = 0; ex = []
        for r in reps:
            hit = False
            for s in sentences(r["text"]):
                if pat.search(s):
                    nsent += 1; hit = True
                    if len(ex) < nex:
                        ex.append(f'    - [{r["publisher"]} | {r["source_file"].split("/")[-1][:40]} | {r["reviewer"][:20]}] {s[:240]}')
            nrep += hit
        print(f"{nrep:4d} reports / {nsent:4d} sentences  {lab}")
        for e in ex:
            print(e)
        print()


if __name__ == "__main__":
    main(sys.argv)
