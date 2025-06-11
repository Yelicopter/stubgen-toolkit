import os
from pathlib import Path
import tiktoken

def count_tokens_in_file(filepath: str) -> int:
    model = "gpt-4"
    encoding = tiktoken.encoding_for_model(model)

    with open(filepath, "r", encoding="utf-8", errors="ignore") as f:
        text = f.read()
    return len(encoding.encode(text))

def count_tokens_in_folder(folder_as_path: Path, extensions={".py"}) -> int:
    folder = str(folder_as_path)
    total_tokens = 0

    for root, _, files in os.walk(folder):
        for file in files:
            if any(file.endswith(ext) for ext in extensions):
                path = os.path.join(root, file)
                try:
                    token_count = count_tokens_in_file(path)
                    total_tokens += token_count
                except Exception as e:
                    print(f"Failed on {path}: {e}")
    return total_tokens

if __name__ == "__main__":
    SRC_DIR = Path("FILL IN SOURCE DIRECTORY HERE")
    print(f"Counting tokens in folder: {SRC_DIR}.")
    tokens = count_tokens_in_folder(SRC_DIR, extensions={".py"})
    print(f"Total tokens in '{SRC_DIR}': {tokens}")
