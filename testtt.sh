#!/usr/bin/env bash
set -euo pipefail

packages=(
    outputs/fastapi/claude_37_sonnet
    outputs/fastapi/claude_sonnet_4
    outputs/fastapi/gemini_25_pro_preview
    outputs/fastapi/gpt_41
    outputs/fastapi/llama_4_scout
    outputs/pandasai/claude_37_sonnet
    outputs/pandasai/claude_sonnet_4
    outputs/pandasai/gemini_25_pro_preview
    outputs/pandasai/gpt_41
    outputs/pandasai/llama_4_scout
    outputs/rich/claude_37_sonnet
    outputs/rich/claude_sonnet_4
    outputs/rich/gemini_25_pro_preview
    outputs/rich/gpt_41
    outputs/rich/llama_4_scout
    outputs/typer/claude_37_sonnet
    outputs/typer/claude_sonnet_4
    outputs/typer/gemini_25_pro_preview
    outputs/typer/gpt_41
    outputs/typer/llama_4_scout
    outputs/youtube_transcript_api/claude_37_sonnet
    outputs/youtube_transcript_api/claude_sonnet_4
    outputs/youtube_transcript_api/gemini_25_pro_preview
    outputs/youtube_transcript_api/gpt_41
    outputs/youtube_transcript_api/llama_4_scout
    outputs/ghunt/claude_37_sonnet
    outputs/ghunt/claude_sonnet_4
    outputs/ghunt/gemini_25_pro_preview
    outputs/ghunt/gpt_41
    outputs/ghunt/llama_4_scout
    outputs/flake8/claude_37_sonnet
    outputs/flake8/claude_sonnet_4
    outputs/flake8/gemini_25_pro_preview
    outputs/flake8/gpt_41
    outputs/flake8/llama_4_scout
    outputs/pre_commit_hooks/claude_37_sonnet
    outputs/pre_commit_hooks/claude_sonnet_4
    outputs/pre_commit_hooks/gemini_25_pro_preview
    outputs/pre_commit_hooks/gpt_41
    outputs/pre_commit_hooks/llama_4_scout
    outputs/private_gpt/claude_37_sonnet
    outputs/private_gpt/claude_sonnet_4
    outputs/private_gpt/gemini_25_pro_preview
    outputs/private_gpt/gpt_41
    outputs/private_gpt/llama_4_scout
    outputs/screenshot_to_code/claude_37_sonnet
    outputs/screenshot_to_code/claude_sonnet_4
    outputs/screenshot_to_code/gemini_25_pro_preview
    outputs/screenshot_to_code/gpt_41
    outputs/screenshot_to_code/llama_4_scout
  )

variants=( stubs_2 stubs )

OUTROOT=stubs_out
mkdir -p "$OUTROOT"

for pkg in "${packages[@]}"; do
  for var in "${variants[@]}"; do
    outdir="$OUTROOT/${pkg}__${var}"
    echo "▶ stubgen --no-import $pkg  →  $outdir"
    stubgen --no-import "${pkg}/${var}" -o "$outdir"
  done
done
