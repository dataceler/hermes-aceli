#!/usr/bin/env python3
"""
Fetch a YouTube video transcript and output it as structured JSON.

Usage:
    python3 run_transcript.py <url_or_video_id> [--language en,tr] [--timestamps]

Output (JSON):
    {
        "video_id": "...",
        "segment_count": 123,
        "duration": "12:34",
        "full_text": "complete transcript as plain text",
        "timestamped_text": "00:00 first line\n00:05 second line\n..."  # only with --timestamps
    }

The dependency is installed automatically inside the dedicated skill venv by
scripts/run_transcript.py. Do not run this helper directly.
"""

import argparse
import json
import re
import sys


def extract_video_id(url_or_id: str) -> str:
    """Extract the 11-character video ID from various YouTube URL formats."""
    url_or_id = url_or_id.strip()
    patterns = [
        r'(?:v=|youtu\.be/|shorts/|embed/|live/)([a-zA-Z0-9_-]{11})',
        r'^([a-zA-Z0-9_-]{11})$',
    ]
    for pattern in patterns:
        match = re.search(pattern, url_or_id)
        if match:
            return match.group(1)
    return url_or_id


def format_timestamp(seconds: float) -> str:
    """Convert seconds to HH:MM:SS or MM:SS format."""
    total = int(seconds)
    h, remainder = divmod(total, 3600)
    m, s = divmod(remainder, 60)
    if h > 0:
        return f"{h}:{m:02d}:{s:02d}"
    return f"{m}:{s:02d}"


def fetch_transcript(video_id: str, languages: list = None):
    """Fetch transcript segments from YouTube.

    Returns a list of dicts with 'text', 'start', and 'duration' keys.
    Compatible with youtube-transcript-api v1.x.
    """
    try:
        from youtube_transcript_api import YouTubeTranscriptApi
    except ImportError:
        print(
            "Error: youtube-transcript-api is missing from the dedicated skill venv. "
            "Run: python3 SKILL_DIR/scripts/run_transcript.py --help",
            file=sys.stderr,
        )
        sys.exit(1)

    api = YouTubeTranscriptApi()
    if languages:
        result = api.fetch(video_id, languages=languages)
    else:
        result = api.fetch(video_id)

    # v1.x returns FetchedTranscriptSnippet objects; normalize to dicts
    return [
        {"text": seg.text, "start": seg.start, "duration": seg.duration}
        for seg in result
    ]


def classify_error(exc: Exception) -> dict:
    """Convert youtube-transcript-api failures into stable machine-readable errors."""
    exception_name = type(exc).__name__
    categories = {
        "IpBlocked": (
            "youtube_request_blocked",
            "YouTube blocked requests from this IP. The transcript may still exist; retry from an allowed network or configured proxy.",
        ),
        "RequestBlocked": (
            "youtube_request_blocked",
            "YouTube blocked this request. The transcript may still exist; retry later or from an allowed network.",
        ),
        "TranscriptsDisabled": (
            "transcripts_disabled",
            "Transcripts are disabled for this video.",
        ),
        "NoTranscriptFound": (
            "no_transcript_found",
            "No transcript matched the requested languages. Retry without --language to inspect any available transcript.",
        ),
        "TranslationLanguageNotAvailable": (
            "language_unavailable",
            "The requested translation language is unavailable.",
        ),
        "NotTranslatable": (
            "language_unavailable",
            "This transcript cannot be translated to the requested language.",
        ),
        "VideoUnavailable": (
            "video_unavailable",
            "The video is private, deleted, region-restricted, or otherwise unavailable.",
        ),
        "VideoUnplayable": (
            "video_unavailable",
            "The video cannot be played from this environment.",
        ),
        "AgeRestricted": (
            "video_unavailable",
            "The video is age-restricted and cannot be accessed by this transcript request.",
        ),
        "InvalidVideoId": (
            "invalid_video_id",
            "The supplied URL or YouTube video ID is invalid.",
        ),
        "PoTokenRequired": (
            "youtube_request_blocked",
            "YouTube requires an additional proof-of-origin token for this request.",
        ),
        "YouTubeDataUnparsable": (
            "youtube_response_unparsable",
            "YouTube returned a response that this library version could not parse.",
        ),
        "YouTubeRequestFailed": (
            "youtube_request_failed",
            "The request to YouTube failed before a transcript could be retrieved.",
        ),
    }
    code, message = categories.get(
        exception_name,
        ("transcript_fetch_failed", str(exc).strip()[:1000] or "Transcript retrieval failed."),
    )
    return {"error": message, "code": code, "exception": exception_name}


def main():
    parser = argparse.ArgumentParser(description="Fetch YouTube transcript as JSON")
    parser.add_argument("url", help="YouTube URL or video ID")
    parser.add_argument("--language", "-l", default=None,
                        help="Comma-separated language codes (e.g. en,tr). Default: auto")
    parser.add_argument("--timestamps", "-t", action="store_true",
                        help="Include timestamped text in output")
    parser.add_argument("--text-only", action="store_true",
                        help="Output plain text instead of JSON")
    args = parser.parse_args()

    video_id = extract_video_id(args.url)
    languages = [l.strip() for l in args.language.split(",")] if args.language else None

    try:
        segments = fetch_transcript(video_id, languages)
    except Exception as exc:
        print(json.dumps(classify_error(exc), ensure_ascii=False))
        sys.exit(1)

    full_text = " ".join(seg["text"] for seg in segments)
    timestamped = "\n".join(
        f"{format_timestamp(seg['start'])} {seg['text']}" for seg in segments
    )

    if args.text_only:
        print(timestamped if args.timestamps else full_text)
        return

    result = {
        "video_id": video_id,
        "segment_count": len(segments),
        "duration": format_timestamp(segments[-1]["start"] + segments[-1]["duration"]) if segments else "0:00",
        "full_text": full_text,
    }
    if args.timestamps:
        result["timestamped_text"] = timestamped

    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
