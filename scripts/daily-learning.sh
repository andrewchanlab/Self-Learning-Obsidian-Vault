#!/usr/bin/env python3
"""
Daily Learning Point Generator

Reads index.md, generates ELI5-style learning points for each active topic,
creates dated pages in topic folders, and commits to GitHub.

Usage:
    ./scripts/daily-learning.sh

Environment Variables:
    OPENAI_API_KEY       - API key for OpenAI
    ANTHROPIC_API_KEY    - API key for Anthropic Claude
    AI_PROVIDER          - Provider: openai, anthropic, ollama (default: openai)
    AI_MODEL             - Model name (default: gpt-4o-mini)
    VAULT_DIR            - Path to vault (default: script's parent dir)
    GIT_BRANCH           - Branch to push (default: main)
    OLLAMA_BASE_URL      - Ollama endpoint (default: http://localhost:11434)
"""

import os
import re
import sys
import json
import argparse
import subprocess
from datetime import datetime, date
from pathlib import Path
from typing import Optional

# ============================================================================
# Configuration
# ============================================================================

VAULT_DIR = Path(os.environ.get("VAULT_DIR", str(Path(__file__).parent.parent)))
INDEX_FILE = VAULT_DIR / "index.md"
GIT_BRANCH = os.environ.get("GIT_BRANCH", "main")
AI_PROVIDER = os.environ.get("AI_PROVIDER", "openai").lower()
AI_MODEL = os.environ.get("AI_MODEL", "gpt-4o-mini")
OLLAMA_BASE_URL = os.environ.get("OLLAMA_BASE_URL", "http://localhost:11434")

# API Keys
OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY", "")
ANTHROPIC_API_KEY = os.environ.get("ANTHROPIC_API_KEY", "")

# System prompt for ELI5-style learning
SYSTEM_PROMPT = """You are a friendly, patient teacher explaining concepts to a curious beginner.
Generate 3-5 concise learning points in ELI5 (Explain Like I'm 5) style.
Each point should be:
- Simple and easy to understand
- Concrete (use analogies when helpful)
- Self-contained (understandable on its own)

Output format: JSON array of strings, each string is one learning point.
Example: ["Light bulbs glow because electricity heats a thin wire until it glows", "..."]
"""

# ============================================================================
# AI Provider Interfaces
# ============================================================================

class AIProviderError(Exception):
    """Raised when AI provider encounters an error."""
    pass


def call_openai(prompt: str, model: str = AI_MODEL) -> list[str]:
    """Call OpenAI API for learning points generation."""
    if not OPENAI_API_KEY:
        raise AIProviderError("OPENAI_API_KEY not set")

    import urllib.request

    payload = {
        "model": model,
        "messages": [
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": prompt}
        ],
        "temperature": 0.7,
        "max_tokens": 1000
    }

    data = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(
        "https://api.openai.com/v1/chat/completions",
        data=data,
        headers={
            "Content-Type": "application/json",
            "Authorization": f"Bearer {OPENAI_API_KEY}"
        },
        method="POST"
    )

    try:
        with urllib.request.urlopen(req, timeout=60) as response:
            result = json.loads(response.read().decode("utf-8"))
            content = result["choices"][0]["message"]["content"]
            return json.loads(content)
    except urllib.error.HTTPError as e:
        error_body = e.read().decode("utf-8")
        raise AIProviderError(f"OpenAI API error {e.code}: {error_body}")
    except Exception as e:
        raise AIProviderError(f"OpenAI API error: {e}")


def call_anthropic(prompt: str, model: str = "claude-3-5-haiku-20241022") -> list[str]:
    """Call Anthropic Claude API for learning points generation."""
    if not ANTHROPIC_API_KEY:
        raise AIProviderError("ANTHROPIC_API_KEY not set")

    import urllib.request

    # Map friendly model names to actual API models
    model_map = {
        "claude-3-5-sonnet-20241022": "claude-3-5-sonnet-20241022",
        "claude-3-5-haiku-20241022": "claude-3-5-haiku-20241022",
        "claude-3-opus-20240229": "claude-3-opus-20240229",
        "claude-3-sonnet-20240229": "claude-3-sonnet-20240229",
    }
    api_model = model_map.get(model, "claude-3-5-haiku-20241022")

    payload = {
        "model": api_model,
        "max_tokens": 1024,
        "system": SYSTEM_PROMPT,
        "messages": [
            {"role": "user", "content": prompt}
        ]
    }

    data = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(
        "https://api.anthropic.com/v1/messages",
        data=data,
        headers={
            "Content-Type": "application/json",
            "x-api-key": ANTHROPIC_API_KEY,
            "anthropic-version": "2023-06-01",
            "anthropic-dangerous-direct-browser-access": "true"
        },
        method="POST"
    )

    try:
        with urllib.request.urlopen(req, timeout=60) as response:
            result = json.loads(response.read().decode("utf-8"))
            content = result["content"][0]["text"]
            return json.loads(content)
    except urllib.error.HTTPError as e:
        error_body = e.read().decode("utf-8")
        raise AIProviderError(f"Anthropic API error {e.code}: {error_body}")
    except Exception as e:
        raise AIProviderError(f"Anthropic API error: {e}")


def call_ollama(prompt: str, model: str = "llama3.2") -> list[str]:
    """Call Ollama API for learning points generation."""
    import urllib.request

    payload = {
        "model": model,
        "prompt": f"{SYSTEM_PROMPT}\n\n{prompt}",
        "stream": False
    }

    data = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(
        f"{OLLAMA_BASE_URL}/api/generate",
        data=data,
        headers={"Content-Type": "application/json"},
        method="POST"
    )

    try:
        with urllib.request.urlopen(req, timeout=120) as response:
            result = json.loads(response.read().decode("utf-8"))
            content = result.get("response", "")
            return json.loads(content)
    except Exception as e:
        raise AIProviderError(f"Ollama API error: {e}")


def generate_learning_points(topic: str, folder: str) -> list[str]:
    """Generate learning points using configured AI provider."""
    prompt = f"Generate ELI5 learning points for the topic: {topic}"

    if AI_PROVIDER == "openai":
        return call_openai(prompt)
    elif AI_PROVIDER == "anthropic":
        return call_anthropic(prompt)
    elif AI_PROVIDER == "ollama":
        return call_ollama(prompt)
    else:
        raise AIProviderError(f"Unknown AI provider: {AI_PROVIDER}")


# ============================================================================
# Index Parsing
# ============================================================================

def parse_index() -> list[tuple[str, str, str]]:
    """
    Parse index.md and return list of (topic, status, folder) tuples.
    Only returns topics with 'active' status.
    """
    if not INDEX_FILE.exists():
        raise FileNotFoundError(f"Index file not found: {INDEX_FILE}")

    content = INDEX_FILE.read_text(encoding="utf-8")

    # Find the table rows (skip header and separator)
    rows = []
    in_table = False
    for line in content.split("\n"):
        line = line.strip()
        # Start of table
        if line.startswith("| Topic"):
            in_table = True
            continue
        # End of table (separator or empty after table)
        if in_table and (line.startswith("|-") or line.startswith("|--")):
            continue
        # Empty line or non-table content after table started
        if in_table and (line == "" or not line.startswith("|")):
            break
        # Table row
        if in_table and line.startswith("|"):
            parts = [p.strip() for p in line.split("|")]
            if len(parts) >= 4 and parts[1]:  # parts[0] is empty before first |
                topic = parts[1]
                status = parts[2].lower() if parts[2] else ""
                folder = parts[3].strip() if parts[3] else ""
                if status == "active" and topic:
                    rows.append((topic, status, folder))

    return rows


# ============================================================================
# File Generation
# ============================================================================

def generate_page_content(topic: str, folder: str, points: list[str]) -> str:
    """Generate markdown content for a daily learning page."""
    today = date.today()
    date_str = today.strftime("%Y-%m-%d")
    day_name = today.strftime("%A")

    # Build bullet points
    bullet_points = []
    for i, point in enumerate(points, 1):
        # Clean up the point text
        point = point.strip()
        if not point:
            continue
        # Remove leading numbers/bullets if present
        point = re.sub(r"^\d+[\.\)]\s*", "", point)
        bullet_points.append(f"{i}. {point}")

    content = f"""# Learning: {topic} — {date_str}

> Generated on {day_name}, {date_str}

## What I Learned Today

{chr(10).join(bullet_points)}

## Key Takeaways

- Each point above builds on fundamental concepts
- Practice reinforces understanding
- Ask questions when concepts are unclear

## Tomorrow's Focus

- Review today's points
- Explore related subtopics
- Apply concepts in small projects

---
*Generated by Daily Learning Vault*
"""
    return content


def create_topic_folder(folder: str) -> Path:
    """Create topic folder if it doesn't exist."""
    folder_path = VAULT_DIR / folder
    folder_path.mkdir(parents=True, exist_ok=True)
    return folder_path


def save_daily_page(topic: str, folder: str, points: list[str]) -> Path:
    """Save a daily learning page and return the file path."""
    folder_path = create_topic_folder(folder)
    today = date.today()
    filename = f"{today.isoformat()}.md"
    file_path = folder_path / filename

    content = generate_page_content(topic, folder, points)
    file_path.write_text(content, encoding="utf-8")

    return file_path


# ============================================================================
# Git Operations
# ============================================================================

def git_add_commit_push(message: Optional[str] = None) -> bool:
    """Add all changes, commit, and push to remote."""
    if message is None:
        today = date.today()
        message = f"Daily learning update: {today.isoformat()}"

    try:
        # Check git status first
        result = subprocess.run(
            ["git", "status", "--porcelain"],
            cwd=VAULT_DIR,
            capture_output=True,
            text=True
        )

        if not result.stdout.strip():
            print("No changes to commit.")
            return True

        # Add all files
        subprocess.run(
            ["git", "add", "-A"],
            cwd=VAULT_DIR,
            check=True
        )

        # Commit
        subprocess.run(
            ["git", "commit", "-m", message],
            cwd=VAULT_DIR,
            check=True
        )

        # Push
        subprocess.run(
            ["git", "push", "origin", GIT_BRANCH],
            cwd=VAULT_DIR,
            check=True
        )

        print(f"✓ Committed and pushed: {message}")
        return True

    except subprocess.CalledProcessError as e:
        print(f"Git error: {e}")
        return False


# ============================================================================
# Main
# ============================================================================

def main():
    parser = argparse.ArgumentParser(description="Daily Learning Point Generator")
    parser.add_argument("--dry-run", action="store_true", help="Don't save or push, just show what would be done")
    parser.add_argument("--no-push", action="store_true", help="Commit but don't push")
    parser.add_argument("--message", "-m", help="Custom commit message")
    args = parser.parse_args()

    print("=" * 50)
    print("Daily Learning Vault")
    print(f"Date: {date.today().isoformat()}")
    print(f"Provider: {AI_PROVIDER} ({AI_MODEL})")
    print("=" * 50)

    # Validate vault
    if not VAULT_DIR.exists():
        print(f"Error: Vault directory not found: {VAULT_DIR}")
        sys.exit(1)

    # Parse topics
    print("\n[1/4] Parsing index.md...")
    try:
        topics = parse_index()
    except FileNotFoundError as e:
        print(f"Error: {e}")
        sys.exit(1)

    if not topics:
        print("No active topics found in index.md")
        sys.exit(0)

    print(f"Found {len(topics)} active topic(s):")
    for topic, _, folder in topics:
        print(f"  - {topic} (folder: {folder})")

    # Generate learning points for each topic
    print("\n[2/4] Generating learning points...")
    results = []
    for topic, status, folder in topics:
        print(f"\n  Processing: {topic}")
        try:
            points = generate_learning_points(topic, folder)
            print(f"    Generated {len(points)} points")
            results.append((topic, folder, points))

            if args.dry_run:
                print("    [DRY RUN] Would save:")
                for p in points:
                    print(f"      - {p[:60]}...")
            else:
                file_path = save_daily_page(topic, folder, points)
                print(f"    Saved: {file_path.name}")

        except AIProviderError as e:
            print(f"    Error generating points: {e}")
            results.append((topic, folder, []))

    # Git operations
    if not args.dry_run:
        print("\n[3/4] Git operations...")
        if any(points for _, _, points in results):
            success = git_add_commit_push(args.message)
            if not success:
                print("Warning: Git push failed (may need credentials)")
        else:
            print("No content to commit.")
    else:
        print("\n[3/4] Git operations skipped (dry run)")

    print("\n[4/4] Done!")
    print("=" * 50)

    if args.dry_run:
        print("\nThis was a dry run. No files were saved or pushed.")
        sys.exit(0)

    return 0


if __name__ == "__main__":
    sys.exit(main())
