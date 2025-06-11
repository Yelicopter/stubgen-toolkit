import os
import re
import sys
from pathlib import Path
from openai import OpenAI
from dotenv import load_dotenv

# === CONFIGURATION ===
MYPY_OUTPUT = "mypy_output.txt" # Save mypy output beforehand
STUBS_DIR = Path("rich")
FEEDBACK_PROMPT = "feedback_prompt.txt"
OUTPUT_DIR = Path("genstubs-NAME YOUR MODEL HERE-feedback")
ERROR_RE = re.compile(r"(.+\.pyi):(\d+): error: (.+)") # Regex to catch mypy errors in txt file
load_dotenv()
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
MODEL = "CHOOSE YOUR MODEL HERE"
client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=OPENROUTER_API_KEY,
)


# === UTILITIES ===
def get_faulty_code():
    all_code = ""
    errors = 0
    with open(MYPY_OUTPUT, "r") as f:
        for line in f:
            match = ERROR_RE.match(line)
            if match:
                errors += 1
                rel_path, lineno, error_msg = match.groups()
                stub_name = Path(rel_path)
                if not stub_name.exists():
                    print(f"Stub file not found: {stub_name}")
                    continue

                if f"FILE: {stub_name}" not in all_code:
                    with open(stub_name, "r") as stub_file:
                        stub_lines = stub_file.readlines()
                        all_code += f"\n# FILE: {stub_name}\n"
                        all_code += stub_name.read_text(encoding="utf-8") + "\n\n"
                all_code += f"# ERRORS for {stub_name}: {error_msg}\n"

    return all_code


def get_prompt(code):
    with open(FEEDBACK_PROMPT, "r", encoding="utf-8") as f:
        prompt_template = f.read()
    return prompt_template.format(all_code=code.strip())

def send_to_llm(prompt):
    print("Sending prompt to LLM.")

    try:
        resp = client.chat.completions.create(
            model=MODEL,
            messages=[
                {"role": "system", "content": "You are a helpful Python typing assistant."},
                {"role": "user", "content": prompt},
            ],
            temperature=0,
        )
        if resp is None:
            print("No response from OpenRouter.")
            sys.exit(1)

        print(f"🪪 Raw response: {resp}")
        if not hasattr(resp, "choices") or not resp.choices:
            print(f"LLM response invalid or empty: {resp}")
            sys.exit(1)

    except Exception as e:
        print(f"LLM request failed: {e}")
        sys.exit(1)

    return resp.choices[0].message.content


def extract_file_blocks(full_text: str):
    blocks = {}
    current_file = None
    current_lines = []
    for line in full_text.splitlines():
        m = re.match(r"#\s*FILE:\s*(.+)", line.strip())
        if m:
            if current_file and current_lines:
                blocks[current_file] = "\n".join(current_lines).strip()
            current_file = m.group(1)
            current_lines = []
        elif current_file:
            current_lines.append(line)

    if current_file and current_lines:
        blocks[current_file] = "\n".join(current_lines).strip()

    return blocks


def create_stubs(response_text):
    print("Splitting files...")
    blocks = extract_file_blocks(response_text)

    for filename, content in blocks.items():
        out_path = OUTPUT_DIR / filename
        out_path.parent.mkdir(parents=True, exist_ok=True)
        out_path.write_text(content.strip(), encoding="utf-8")
        print(f"✅ Saved {out_path}")

    print("All stubs generated.")


if __name__ == "__main__":
    code = get_faulty_code()
    prompt = get_prompt(code)
    print("Code & prompt for feedback loop collected.")
    llm_response = send_to_llm(prompt)
    create_stubs(llm_response)