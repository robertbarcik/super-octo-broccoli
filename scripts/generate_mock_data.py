"""Utility script to expand the training dataset for agent session transcripts."""
from __future__ import annotations

import argparse
import csv
import os
from datetime import UTC, datetime
from pathlib import Path
from typing import Iterable, List


def ensure_openai_token(token: str | None) -> str:
    """Ensure an OpenAI API token is available for downstream integrations.

    The script itself does not currently call the OpenAI API, but we enforce token
    availability so that extending it with API calls is frictionless.
    """

    token = token or os.getenv("OPENAI_API_KEY")
    if not token:
        raise SystemExit(
            "An OpenAI API token is required. Provide it via --openai-api-key or set "
            "the OPENAI_API_KEY environment variable."
        )

    # Normalise environment so subsequent imports can rely on OPENAI_API_KEY.
    os.environ.setdefault("OPENAI_API_KEY", token)
    return token


def build_rows() -> Iterable[List[str]]:
    """Return mock rows representing interactions between agents."""
    timestamp = datetime.now(UTC).isoformat()
    return [
        ["S3", "planner", "instruction", "Define analysis tasks", timestamp],
        ["S3", "analyst", "tool_call", "query:extract_entities", timestamp],
        ["S3", "writer", "draft", "Summarize extracted entities", timestamp],
    ]


def write_rows(destination: Path) -> None:
    destination.parent.mkdir(parents=True, exist_ok=True)
    with destination.open("w", newline="") as fp:
        writer = csv.writer(fp)
        writer.writerow(["session_id", "role", "message_type", "content", "timestamp"])
        writer.writerows(build_rows())


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--openai-api-key",
        dest="openai_api_key",
        help="OpenAI API token. Falls back to the OPENAI_API_KEY environment variable.",
    )
    args = parser.parse_args()

    ensure_openai_token(args.openai_api_key)
    output_path = Path(__file__).resolve().parents[1] / "data" / "extended_agent_sessions.csv"
    write_rows(output_path)
    print(f"Wrote mock data to {output_path}")
