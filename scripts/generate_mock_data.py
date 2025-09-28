"""Utility script to expand the training dataset for agent session transcripts."""
from __future__ import annotations

import csv
from datetime import UTC, datetime
from pathlib import Path
from typing import Iterable, List


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
    output_path = Path(__file__).resolve().parents[1] / "data" / "extended_agent_sessions.csv"
    write_rows(output_path)
    print(f"Wrote mock data to {output_path}")
