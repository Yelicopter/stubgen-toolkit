from pathlib import Path

from scripts.data_prepper.stripper import stripper, SRC_DIR
from scripts.data_prepper.token_counter import count_tokens_in_folder


def data_prepper():
    SRC_DIR = Path("FILL IN SOURCE DIRECTORY HERE")
    OUT_DIR = Path("stripped_src")

    print("Stripping code files in source directory:", SRC_DIR)
    stripper(SRC_DIR, OUT_DIR)
    print(f"Stripped code files, token count is: {count_tokens_in_folder(SRC_DIR)}")

if __name__ == "__main__":
    data_prepper()
