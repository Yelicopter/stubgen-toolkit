import os
import re
import sys
from pathlib import Path
from openai import OpenAI
from dotenv import load_dotenv

# === SETTINGS ===
OUTPUT_DIR = Path("genstubs-NAME YOUR MODEL HERE")

load_dotenv()
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
MODEL = "CHOOSE YOUR MODEL HERE"
client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=OPENROUTER_API_KEY,
)


# === UTILITIES ===
def collect_all_code():
    all_code = ""
    stripped_dir = Path("stripped")

    if not stripped_dir.exists():
        print(f"Stripped directory not found: {stripped_dir}")
        sys.exit(1)

    print("Collecting all code...")
    for src in sorted(stripped_dir.rglob("*.py")):
        rel = src.relative_to(stripped_dir)
        all_code += f"# FILE: {rel}\n"
        all_code += src.read_text(encoding="utf-8") + "\n\n"
    return all_code.strip()


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


def get_prompt(code):
    with open("first_prompt.txt", "r", encoding="utf-8") as f:
        prompt_template = f.read()
    return prompt_template.format(all_code=code.strip())


def send_to_llm(prompt):
    print(f"Prompt length: {len(prompt)} characters")
    print(f"Sending prompt to LLM...")

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

        # print(f"Raw response: {resp}") # Uncomment if you want
        if not hasattr(resp, "choices") or not resp.choices:
            print(f"LLM response invalid or empty: {resp}")
            sys.exit(1)

    except Exception as e:
        print(f"LLM request failed: {e}")
        sys.exit(1)

    return resp


def create_stubs(response):
    response_text = response.choices[0].message.content
    print("Splitting files...")
    blocks = extract_file_blocks(response_text)

    for file_name, file_content in blocks.items():
        out_path = OUTPUT_DIR / file_name
        out_path.parent.mkdir(parents=True, exist_ok=True)
        out_path.write_text(file_content.strip(), encoding="utf-8")
        print(f"✅ Saved {out_path}")

    print("All stubs generated.")

if __name__ == "__main__":
    code = collect_all_code()
    prompt = get_prompt(code)
    print("Code & prompt collected.")
    llm_response = send_to_llm(prompt)
    create_stubs(llm_response)