import argparse
import shutil
from pathlib import Path
from typing import List, Iterable

def _collect_files(root: Path, exts: List[str]) -> Iterable[Path]:
    if root.is_file():
        if root.suffix in exts:
            yield root
    else:
        for ext in exts:
            yield from root.rglob(f"*{ext}")


def _clean_file(path: Path, pattern: str = "```") -> bool:
    try:
        text = path.read_text(encoding="utf-8")
    except (FileNotFoundError):
        return False
    if pattern not in text:
        return False
    new_text = text.replace(pattern, "")
    path.write_text(new_text, encoding="utf-8")
    return True


def main() -> None:
    paths_to_clean = ["..."]
    pattern_to_remove = "```"

    total_modified = 0
    for start_path_str in paths_to_clean:
        start_path = Path(start_path_str)
        if not start_path.exists():
            print(f"doesnt exist: {start_path}")
            continue

        for file in _collect_files(start_path, [".py", ".pyi"]):
            if _clean_file(file, pattern_to_remove):
                print(f"  Cleaned {file}")
                total_modified += 1

    print(f"cleaned {total_modified} files.")


if __name__ == "__main__":
    main()
