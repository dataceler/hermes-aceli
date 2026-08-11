---
name: youtube-content
description: "YouTube transcripts to summaries, threads, blogs."
platforms: [linux, macos, windows]
---

# YouTube Content Tool

## When to use

Use when the user shares a YouTube URL or video link, asks to summarize a video, requests a transcript, or wants to extract and reformat content from any YouTube video. Transforms transcripts into structured content (chapters, summaries, threads, blog posts).

Extract transcripts from YouTube videos and convert them into useful formats.

## Setup and virtual environment

Do not install dependencies into the system Python and do not use `--break-system-packages`.
The skill ships with `scripts/run_transcript.py`, a bootstrap launcher that:

1. creates a dedicated venv at `~/.hermes/cache/venvs/youtube-content` (or `$HERMES_HOME/cache/venvs/youtube-content`);
2. installs `youtube-transcript-api>=1,<2` inside that venv only;
3. reuses the same venv on later calls;
4. executes `fetch_transcript.py` with the venv interpreter.

The first run needs network access to the Python package index. On Debian/Ubuntu,
if `python -m venv` is unavailable, install the matching `python3-venv` OS package
outside this skill and retry. Never fall back to global `pip install`.

For an isolated test or custom location, set `YOUTUBE_CONTENT_VENV` to an absolute
venv path.

## Helper Script

`SKILL_DIR` is the directory containing this SKILL.md file. Always invoke the
bootstrap launcher with any available Python 3 interpreter; do not call
`fetch_transcript.py` directly and do not prepend `uv run`.

```bash
# JSON output with metadata
python3 SKILL_DIR/scripts/run_transcript.py "https://youtube.com/watch?v=VIDEO_ID"

# Plain text (good for further processing)
python3 SKILL_DIR/scripts/run_transcript.py "URL" --text-only

# With timestamps
python3 SKILL_DIR/scripts/run_transcript.py "URL" --timestamps

# Specific language with fallback chain
python3 SKILL_DIR/scripts/run_transcript.py "URL" --language tr,en

# Verify/bootstrap without a network transcript request
python3 SKILL_DIR/scripts/run_transcript.py --help
```

The launcher works when the outer interpreter is PEP 668 / `EXTERNALLY-MANAGED`
because package installation occurs only through the venv's Python.

## Output Formats

After fetching the transcript, format it based on what the user asks for:

- **Chapters**: Group by topic shifts, output timestamped chapter list
- **Summary**: Concise 5-10 sentence overview of the entire video
- **Chapter summaries**: Chapters with a short paragraph summary for each
- **Thread**: Twitter/X thread format — numbered posts, each under 280 chars
- **Blog post**: Full article with title, sections, and key takeaways
- **Quotes**: Notable quotes with timestamps

### Example — Chapters Output

```
00:00 Introduction — host opens with the problem statement
03:45 Background — prior work and why existing solutions fall short
12:20 Core method — walkthrough of the proposed approach
24:10 Results — benchmark comparisons and key takeaways
31:55 Q&A — audience questions on scalability and next steps
```

## Workflow

1. **Fetch through the helper first** with `python3 SKILL_DIR/scripts/run_transcript.py "URL" --text-only --timestamps`. The launcher must own venv creation and dependency installation.
2. **Fallback on request blocking**: if the helper returns `youtube_request_blocked`, open the original YouTube page in the browser, expand the description, activate **Show transcript**, and extract timestamped segments from the visible transcript panel. YouTube may expose the transcript panel even when the player says captions are unavailable.
3. **Avoid DOM duplication**: YouTube can render a visible and a hidden `ytd-transcript-segment-list-renderer`. Extract only the panel with visible layout dimensions; verify segment count plus first and last timestamps before using it.
4. **Validate**: confirm the source is actual spoken transcript, the output is non-empty, and the language is expected. If no language matches in the API, retry without `--language`. Do not interpret metadata, descriptions, chapters, or thumbnails as a transcript.
5. **Chunk if needed**: if the transcript exceeds ~50K characters, split into overlapping chunks (~40K with 2K overlap) and summarize each chunk before merging.
6. **Transform** into the requested output format. If the user did not specify a format, default to a summary.
7. **Verify**: re-read the transformed output against the transcript for coherence, correct timestamps, and completeness before presenting.

## Error Handling

- **Virtual environment creation failed**: report that the host needs a working `venv` module (for example the matching `python3-venv` package). Do not install globally and do not use `--break-system-packages`.
- **Dependency installation failed**: report package-index/network failure and the dedicated venv path; retry only after addressing connectivity or index configuration.
- **Transcript disabled**: tell the user; suggest they check whether subtitles are available on the video page.
- **Private/unavailable video**: relay the error and ask the user to verify the URL.
- **No matching language**: retry without `--language`, then report the actual outcome.
- **YouTube request blocked**: distinguish IP/rate-limit/request blocking from missing captions; do not claim that a transcript does not exist solely because the request was blocked.
- **Dependency missing inside the venv**: rerun `python3 SKILL_DIR/scripts/run_transcript.py --help`; the launcher will repair the dedicated environment.
