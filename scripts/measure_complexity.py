import re, csv, pathlib, collections
REPOS = [
    r"C:\Users\yeliz\downloads\rich-14.0.0\rich-14.0.0\rich",
    r"C:\Users\yeliz\downloads\fastapi-0.115.12\fastapi",
    r"C:\Users\yeliz\downloads\pandas-ai-main\pandas-ai-main\pandasai",
    r"C:\Users\yeliz\downloads\GHunt-2.2.0 - Claude3.7\ghunt",
    r"C:\Users\yeliz\downloads\typer-0.16.0\typer",
    r"C:\Users\yeliz\downloads\screenshot-to-code-main\backend",
    r"C:\Users\yeliz\downloads\private-gpt-main\private_gpt",
    r"C:\Users\yeliz\downloads\flake8-main\src\flake8",
    r"C:\Users\yeliz\downloads\pre-commit-hooks-main\pre_commit_hooks",
    r"C:\Users\yeliz\downloads\youtube-transcript-api-1.1.0\youtube_transcript_api",
]

ADV_RE    = re.compile(r"(Union\[\s?|Optional\[\s?|List\[\s?|Dict\[\s?|TypeVar\b|Callable\b|Protocol\b)")
NESTED_RE = re.compile(r"\w+\[[^\]]+\[[^\]]+\]")
DYN_RE    = re.compile(r"\b(setattr|exec|eval|importlib|__getattr__)\b")
DEC_RE    = re.compile(r"^\s*@")

WEIGHTS = {
    "loc": 0.10,
    "py_files": 0.15,
    "packages": 0.15,
    "adv_types": 0.25,
    "nested_types": 0.25,
    "decorator_lines": 0.10,
}

def scan_repo(root: pathlib.Path):
    stats = collections.Counter()
    for f in root.rglob("*.py"):
        try:
            txt = f.read_text(encoding="utf-8", errors="ignore")
        except Exception:
            continue
        stats["loc"] += txt.count("\n") + 1
        stats["py_files"] += 1
        if f.name == "__init__.py":
            stats["packages"] += 1
        stats["adv_types"]     += len(ADV_RE.findall(txt))
        stats["nested_types"]  += len(NESTED_RE.findall(txt))
        stats["decorator_lines"] += sum(1 for ln in txt.splitlines() if DEC_RE.match(ln))
    return stats

def main():
    rows, cols = [], list(WEIGHTS.keys())
    for p in REPOS:
        path = pathlib.Path(p)
        if not path.is_dir():
            print(f"WARNING – skipped (not a dir): {path}")
            continue
        stats = scan_repo(path)
        rows.append({"Repo": path.name, **stats})

    # normalise & score
    for col in cols:
        vals = [r[col] for r in rows]
        mn, mx = min(vals), max(vals)
        for r in rows:
            r[f"{col}_norm"] = 0.0 if mx == mn else (r[col]-mn)/(mx-mn)
    for r in rows:
        r["Score"] = round(sum(r[f"{c}_norm"]*w for c,w in WEIGHTS.items()), 3)
        r["Bucket"] = ("simple"   if r["Score"] < 0.20 else
                       "moderate" if r["Score"] < 0.55 else
                       "complex")

    hdr = ["Repo","LOC","Py_Files","Packages","Adv_Types","Nested_Types","Decorator_Lines","Score","Bucket"]
    with open("metrics.csv", "w", newline="", encoding="utf-8") as fh:
        w = csv.writer(fh); w.writerow(hdr)
        for r in rows:
            w.writerow([r["Repo"], r["loc"], r["py_files"], r["packages"],
                        r["adv_types"], r["nested_types"],
                        r["decorator_lines"], r["Score"], r["Bucket"]])

if __name__ == "__main__":
    main()
