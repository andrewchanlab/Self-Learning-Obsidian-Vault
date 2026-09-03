#!/usr/bin/env python3
"""
Update Index Script

Adds or updates topics in the index.md file.
Provides a safe way to manage the learning topic list.

Usage:
    # Add a new topic
    python update_index.py "Topic Name" folder-name
    
    # Add with custom status (default: active)
    python update_index.py "Topic Name" folder-name --status active
    
    # Pause a topic
    python update_index.py "Topic Name" folder-name --status paused
    
    # Remove a topic
    python update_index.py "Topic Name" --remove
    
    # List all topics
    python update_index.py --list

Examples:
    python update_index.py "Python Programming" python
    python update_index.py "Rust Programming" rust --status paused
    python update_index.py "Old Topic" --remove
"""

import os
import re
import sys
import argparse
from pathlib import Path
from typing import Optional

# ============================================================================
# Configuration
# ============================================================================

VAULT_DIR = Path(os.environ.get("VAULT_DIR", str(Path(__file__).parent)))
INDEX_FILE = VAULT_DIR / "index.md"

# Default index.md template
INDEX_TEMPLATE = """# Learning Vault

> 📚 Personal learning tracker. Updated daily by AI.

## Learning List

| Topic | Status | Folder |
|-------|--------|--------|
{rows}

## Getting Started

Add topics to learn above. Each topic will have its own folder created automatically.

## Status Values

- `active` - Topic is being processed daily
- `paused` - Topic is temporarily paused
- `done` - Topic is complete

## Folder Naming

Use lowercase, hyphenated names (e.g., `machine-learning`).
Folders are created automatically when learning points are generated.
"""

# ============================================================================
# Parsing
# ============================================================================

def parse_index() -> dict[str, dict]:
    """Parse index.md and return dict of topics."""
    if not INDEX_FILE.exists():
        return {}

    content = INDEX_FILE.read_text(encoding="utf-8")
    topics = {}

    # Find table rows
    in_table = False
    for line in content.split("\n"):
        line = line.strip()

        if line.startswith("| Topic"):
            in_table = True
            continue

        if in_table and line.startswith("|-"):
            continue

        if in_table and not line.startswith("|"):
            break

        if in_table and line.startswith("|"):
            parts = [p.strip() for p in line.split("|")]
            if len(parts) >= 4 and parts[1] and not parts[1].startswith("Topic"):
                topic = parts[1]
                status = parts[2].lower() if parts[2] else "active"
                folder = parts[3].strip() if parts[3] else ""
                if topic and folder:
                    topics[topic.lower()] = {
                        "topic": topic,
                        "status": status,
                        "folder": folder
                    }

    return topics


def write_index(topics: dict[str, dict]) -> None:
    """Write topics back to index.md."""
    # Sort topics by folder name for consistency
    sorted_topics = sorted(topics.values(), key=lambda x: x["folder"])

    # Build rows
    rows = []
    for item in sorted_topics:
        rows.append(f"| {item['topic']} | {item['status']} | {item['folder']} |")

    rows_text = "\n".join(rows) if rows else "| (empty) | — | — |"

    content = INDEX_TEMPLATE.format(rows=rows_text)
    INDEX_FILE.write_text(content, encoding="utf-8")


# ============================================================================
# Operations
# ============================================================================

def add_topic(topic: str, folder: str, status: str = "active") -> bool:
    """Add a new topic or update existing one."""
    folder = folder.lower().strip()
    topic = topic.strip()

    # Validate folder name
    if not re.match(r'^[a-z0-9][a-z0-9-]*$', folder):
        print(f"Error: Invalid folder name '{folder}'")
        print("Folder names must:")
        print("  - Start with a letter or number")
        print("  - Contain only lowercase letters, numbers, and hyphens")
        print("  - Be at least 2 characters")
        return False

    topics = parse_index()
    key = topic.lower()

    if key in topics:
        old_folder = topics[key]["folder"]
        topics[key]["status"] = status
        if old_folder != folder:
            print(f"Warning: Topic '{topic}' already exists with folder '{old_folder}'")
            print(f"  Updating folder: {old_folder} -> {folder}")
            topics[key]["folder"] = folder
        else:
            print(f"Updated topic '{topic}' (status: {status})")
    else:
        topics[key] = {
            "topic": topic,
            "status": status,
            "folder": folder
        }
        print(f"Added topic '{topic}' (folder: {folder}, status: {status})")

    write_index(topics)
    return True


def remove_topic(topic: str) -> bool:
    """Remove a topic from the index."""
    topics = parse_index()
    key = topic.lower().strip()

    if key not in topics:
        print(f"Topic '{topic}' not found in index")
        return False

    removed = topics.pop(key)
    write_index(topics)
    print(f"Removed topic '{removed['topic']}' (folder: {removed['folder']})")
    return True


def list_topics() -> None:
    """List all topics in the index."""
    topics = parse_index()

    if not topics:
        print("No topics in index. Add topics with:")
        print("  python update_index.py 'Topic Name' folder-name")
        return

    print(f"Found {len(topics)} topic(s):\n")
    print(f"{'Topic':<30} {'Status':<10} {'Folder':<20}")
    print("-" * 60)

    for item in sorted(topics.values(), key=lambda x: x["topic"]):
        print(f"{item['topic']:<30} {item['status']:<10} {item['folder']:<20}")


def init_index() -> bool:
    """Initialize a new index.md file."""
    if INDEX_FILE.exists():
        print(f"Index already exists: {INDEX_FILE}")
        return False

    topics = {}
    write_index(topics)
    print(f"Created new index: {INDEX_FILE}")
    return True


# ============================================================================
# Main
# ============================================================================

def main():
    parser = argparse.ArgumentParser(
        description="Manage topics in the Learning Vault index",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s "Python" python                  Add Python topic
  %(prog)s "Rust" rust --status paused      Add paused topic
  %(prog)s "Python" --remove                 Remove Python topic
  %(prog)s --list                            List all topics
  %(prog)s --init                            Initialize new index
        """
    )

    parser.add_argument(
        "topic",
        nargs="?",
        help="Topic name"
    )
    parser.add_argument(
        "folder",
        nargs="?",
        help="Folder name (lowercase, hyphenated)"
    )
    parser.add_argument(
        "--status",
        choices=["active", "paused", "done"],
        default="active",
        help="Topic status (default: active)"
    )
    parser.add_argument(
        "--remove",
        action="store_true",
        help="Remove the topic"
    )
    parser.add_argument(
        "--list",
        action="store_true",
        help="List all topics"
    )
    parser.add_argument(
        "--init",
        action="store_true",
        help="Initialize a new index.md"
    )

    args = parser.parse_args()

    # Ensure vault directory exists
    if not VAULT_DIR.exists():
        print(f"Creating vault directory: {VAULT_DIR}")
        VAULT_DIR.mkdir(parents=True, exist_ok=True)

    # Handle --list
    if args.list:
        list_topics()
        return 0

    # Handle --init
    if args.init:
        if init_index():
            return 0
        return 1

    # Require topic for other operations
    if not args.topic:
        parser.print_help()
        print("\nError: topic is required (unless using --list or --init)")
        return 1

    # Handle --remove
    if args.remove:
        if args.folder:
            print("Warning: --folder is ignored with --remove")
        if remove_topic(args.topic):
            return 0
        return 1

    # Handle add/update
    if not args.folder:
        print("Error: folder is required when adding/updating a topic")
        return 1

    if add_topic(args.topic, args.folder, args.status):
        return 0
    return 1


if __name__ == "__main__":
    sys.exit(main())
