#!/usr/bin/env python3
"""Map manuscript text to (page, margin line) for review citations.

Journal submission PDFs (e.g. Editorial Manager) print line numbers in the left
margin, usually restarting on every page. Reviews must cite "p. N, lines a–b",
so every location in a review should be checked with this tool, not guessed
from a plain-text extraction (which loses the line numbers).

Requires PyMuPDF (`import fitz`; install with `pip install pymupdf`).

Page convention: manuscript page 1 is the PDF page given by --first-page
(0-based PDF index, default 1 because index 0 is usually a cover/title page).
Text above line 1 of a page is reported as "top" ("top of page" in reviews).

Usage
  locate.py PDF find "phrase" ["phrase" ...]   page and margin line(s) of every hit
  locate.py PDF page N [LO HI]                  numbered lines of manuscript page N
  locate.py PDF dump OUT.txt                    whole manuscript as "p.N L: text" lines
  locate.py PDF render N OUT.png [DPI]          render manuscript page N (figures/tables)
Options
  --first-page K    PDF index of manuscript page 1 (default 1)

Caveats: text inside figures is often an image and cannot be found (render the
page and look at it instead); table text can interleave with body lines.
"""
import sys

try:
    import fitz  # PyMuPDF
except ImportError:
    sys.exit("PyMuPDF (fitz) is not available in this Python. Install it with "
             "`pip install pymupdf` or run this script with an environment that has it.")


def margin_column(page):
    """Return (numbers, right_edge): margin line numbers as (n, y_center) and the x of
    their right edge. Line numbers are right-aligned in a narrow left column, so keep
    only digit words that share the dominant right edge; this excludes body-text
    numbers that happen to start near the left margin."""
    cand = [w for w in page.get_text("words")
            if w[0] < page.rect.width * 0.13 and w[4].isdigit() and len(w[4]) <= 3]
    if not cand:
        return [], 0.0
    edges = {}
    for w in cand:
        edges[round(w[2])] = edges.get(round(w[2]), 0) + 1
    col = max(edges, key=edges.get)
    keep = [w for w in cand if abs(w[2] - col) <= 4]
    return [(int(w[4]), (w[1] + w[3]) / 2) for w in keep], max(w[2] for w in keep)


def margin_numbers(page):
    return margin_column(page)[0]


def lines_of(page):
    m, right = margin_column(page)
    top_y = min((y for _, y in m), default=None)
    rows = {}
    for w in page.get_text("words"):
        if m and w[2] <= right + 1:   # the margin number itself
            continue
        y = (w[1] + w[3]) / 2
        cand = [n for n, my in m if abs(my - y) < 6]
        if cand:
            key = cand[0]
        elif top_y is not None and y < top_y:
            key = "top"
        else:
            key = "unnumbered"
        rows.setdefault(key, []).append((round(y), w[0], w[4]))
    return rows


def order(k):
    return (0, 0) if k == "top" else ((1, k) if isinstance(k, int) else (2, 0))


def main(argv):
    first = 1
    if "--first-page" in argv:
        i = argv.index("--first-page"); first = int(argv[i + 1]); del argv[i:i + 2]
    if len(argv) < 3:
        sys.exit(__doc__)
    doc = fitz.open(argv[1])
    cmd = argv[2]
    mp = lambda idx: idx - first + 1  # PDF index -> manuscript page

    if cmd == "find":
        for q in argv[3:]:
            hits = []
            for i, p in enumerate(doc):
                for r in p.search_for(q):
                    yc = (r.y0 + r.y1) / 2
                    nums = sorted({n for n, my in margin_numbers(p) if abs(my - yc) < 8})
                    if not nums:
                        m = margin_numbers(p)
                        where = "top of page" if m and yc < min(y for _, y in m) else "unnumbered (figure/table/footer?)"
                    else:
                        where = "line " + ",".join(map(str, nums))
                    hits.append(f"p.{mp(i)} {where}")
            print(repr(q), "->", hits or "NOT FOUND (check spelling, hyphenation, ligatures, or text inside an image)")
    elif cmd == "page":
        n = int(argv[3]); lo = int(argv[4]) if len(argv) > 4 else 0; hi = int(argv[5]) if len(argv) > 5 else 999
        rows = lines_of(doc[n + first - 1])
        for k in sorted(rows, key=order):
            if isinstance(k, int) and not (lo <= k <= hi):
                continue
            ws = sorted(rows[k], key=lambda t: (t[0], t[1]))
            print(k, " ".join(t[2] for t in ws))
    elif cmd == "dump":
        with open(argv[3], "w") as f:
            for i, p in enumerate(doc):
                rows = lines_of(p)
                for k in sorted(rows, key=order):
                    ws = sorted(rows[k], key=lambda t: (t[0], t[1]))
                    f.write(f"p.{mp(i)} {k}: {' '.join(t[2] for t in ws)}\n")
        print("wrote", argv[3])
    elif cmd == "render":
        n = int(argv[3]); dpi = int(argv[5]) if len(argv) > 5 else 130
        doc[n + first - 1].get_pixmap(dpi=dpi).save(argv[4]); print("saved", argv[4])
    else:
        sys.exit(__doc__)


if __name__ == "__main__":
    main(sys.argv)
