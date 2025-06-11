import os
from pathlib import Path
from strip_hints import strip_file_to_string

def stripper(SRC_DIR, OUT_DIR):
    if not SRC_DIR.is_dir():
        print(f"Source directory {SRC_DIR} does not exist.")
        exit(1)
    else:
        for path in SRC_DIR.rglob("*.py"):
            stripped = strip_file_to_string(str(path))
            out_path = OUT_DIR / path.relative_to(SRC_DIR)
            out_path.parent.mkdir(parents=True, exist_ok=True)
            out_path.write_text(stripped, encoding="utf-8")

if __name__ == "__main__":
    SRC_DIR = Path("FILL IN SOURCE DIRECTORY HERE")
    OUT_DIR = Path("stripped_src")

    print("Stripping code files in source directory:", SRC_DIR)
    stripper(SRC_DIR, OUT_DIR)
    print(f"Stripped code files to {OUT_DIR}.")