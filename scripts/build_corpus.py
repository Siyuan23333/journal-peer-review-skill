#!/usr/bin/env python3
"""Build your own sample corpus of published reviewer reports for phrase_check.py.

The corpus behind the counts in references/conventions.md (148 round-1 reports,
mostly medical-imaging AI) is not redistributed here, because the reports'
licences vary by publisher. Build a corpus for your own field instead. See
references/corpus.md for where to find open peer-review reports, and for
licence notes.

Input: a folder of plain-text files. Each file holds one reviewer report, or a
whole peer-review file that you split with --split.
Optional: a CSV (--meta) with columns file,publisher,source_url,licence.

Usage
  build_corpus.py INPUT_DIR [--meta sources.csv] [--split] [--out ../assets/sample_reports.json]

--split cuts each file at reviewer markers ("Reviewer #1", "Reviewer 2:",
"Referee #3", "REVIEWER 1", "Review 2:"). Check the result: author responses
and editor letters often sit between reports and should be removed by hand
first. Keep round-1 reports only.
"""
import csv, json, os, re, sys

MARK = re.compile(r"(?im)^[ \t#*]*(?:reviewer\s*#?\s*\d+\b[^\n]*|reviewer:\s*\d+\s*$|referee\s*#?\s*\d+[^\n]*|review\s*\d+\s*:\s*$)")


def main(argv):
    if len(argv) < 2:
        sys.exit(__doc__)
    src = argv[1]
    meta_path = argv[argv.index("--meta") + 1] if "--meta" in argv else None
    split = "--split" in argv
    here = os.path.dirname(os.path.abspath(__file__))
    out = argv[argv.index("--out") + 1] if "--out" in argv else os.path.join(here, "..", "assets", "sample_reports.json")
    meta = {}
    if meta_path:
        for row in csv.DictReader(open(meta_path)):
            meta[row["file"]] = row
    reports = []
    for fn in sorted(os.listdir(src)):
        if not fn.lower().endswith((".txt", ".md")):
            continue
        text = open(os.path.join(src, fn), encoding="utf-8", errors="replace").read()
        parts = [(m.group(0).strip(), m.start()) for m in MARK.finditer(text)] if split else []
        if parts:
            chunks = [(lab, text[s:(parts[i + 1][1] if i + 1 < len(parts) else len(text))]) for i, (lab, s) in enumerate(parts)]
        else:
            chunks = [("report", text)]
        m = meta.get(fn, {})
        for lab, chunk in chunks:
            if len(chunk.split()) < 40:
                continue
            reports.append({"id": len(reports), "source_file": fn, "publisher": m.get("publisher", ""),
                            "reviewer": re.sub(r"\s+", " ", lab)[:60], "source_url": m.get("source_url", ""),
                            "licence": m.get("licence", ""), "text": chunk})
    os.makedirs(os.path.dirname(os.path.abspath(out)), exist_ok=True)
    json.dump({"meta": {"n_reports": len(reports), "built_from": os.path.abspath(src)}, "reports": reports},
              open(out, "w"), ensure_ascii=False)
    print(f"wrote {len(reports)} reports to {out}")


if __name__ == "__main__":
    main(sys.argv)
