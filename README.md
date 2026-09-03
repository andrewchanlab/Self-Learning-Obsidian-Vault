# Self-Learning Obsidian Vault

An automated daily learning tracker that generates ELI5-style learning points for topics you want to learn. Uses AI to create digestible study notes every day.

## Features

- **Daily Learning Generation**: Automatically generates 3-5 ELI5-style learning points per topic
- **Topic-Based Organization**: Each topic gets its own folder with dated daily notes
- **AI-Agent Friendly**: Fully documented for both human and AI agent usage
- **Flexible Scheduling**: Works with cron jobs, GitHub Actions, or manual triggers

## Repository Structure

```
Self-Learning-Obsidian-Vault/
├── index.md                    # Learning list (topics to study)
├── scripts/
│   └── daily-learning.sh      # Main automation script (run daily)
├── update_index.py             # Add new topics to index.md
├── CRON_SETUP.md               # Scheduling instructions
├── .github/
│   └── workflows/
│       └── daily-learning.yml  # GitHub Actions version
└── [topic-folders]/           # Auto-created per topic
    └── YYYY-MM-DD.md           # Daily learning points
```

## Quick Start

### 1. Clone the Repository

```bash
git clone https://github.com/andrewchanlab/Self-Learning-Obsidian-Vault.git
cd Self-Learning-Obsidian-Vault
```

### 2. Add Topics to Learn

Edit `index.md` and add topics in the table:

```markdown
| Topic | Status | Folder |
|-------|--------|--------|
| Python Programming | active | python |
| Machine Learning | active | ml |
```

Or use the helper script:

```bash
python update_index.py "Rust Programming" rust
```

### 3. Set Up AI Provider

The script uses OpenAI by default. Set your API key:

```bash
export OPENAI_API_KEY="sk-..."
```

Or configure a different provider (see Configuration section).

### 4. Run Daily Learning

```bash
./scripts/daily-learning.sh
```

This will:
1. Read active topics from `index.md`
2. Generate 3-5 ELI5 learning points per topic
3. Create dated pages in each topic folder
4. Commit and push changes to GitHub

## Configuration

### Environment Variables

| Variable | Description | Default |
|----------|-------------|---------|
| `OPENAI_API_KEY` | API key for AI generation | Required |
| `AI_MODEL` | Model to use | `gpt-4o-mini` |
| `AI_PROVIDER` | Provider: `openai`, `anthropic`, `ollama` | `openai` |
| `VAULT_DIR` | Path to vault | `./` |
| `GIT_BRANCH` | Branch to push to | `main` |

### Using Different AI Providers

**Anthropic (Claude):**
```bash
export AI_PROVIDER="anthropic"
export ANTHROPIC_API_KEY="sk-ant-..."
```

**Ollama (Local):**
```bash
export AI_PROVIDER="ollama"
export OLLAMA_BASE_URL="http://localhost:11434"
```

### Custom Model

```bash
export AI_MODEL="claude-3-5-sonnet-20241022"
```

## Index.md Format

The `index.md` file uses a markdown table to track learning topics:

```markdown
| Topic | Status | Folder |
|-------|--------|--------|
| Python | active | python |
| Rust | active | rust |
| Go | paused | go |
```

**Status Values:**
- `active` - Topic will be processed daily
- `paused` - Topic is skipped
- `done` - Topic is complete

**Folder Naming:**
- Use lowercase, hyphenated names
- Folders are created automatically in the vault root

## Scheduling

### Option 1: Linux Cron

See [CRON_SETUP.md](./CRON_SETUP.md) for detailed instructions.

```bash
# Edit crontab
crontab -e

# Add line for 8:30 AM daily
30 8 * * * cd /path/to/vault && ./scripts/daily-learning.sh >> /var/log/daily-learning.log 2>&1
```

### Option 2: GitHub Actions

The repository includes a GitHub Actions workflow (`.github/workflows/daily-learning.yml`) that runs daily at 8:00 AM UTC.

**Setup:**
1. Go to repository Settings → Secrets
2. Add `OPENAI_API_KEY` secret
3. The workflow runs automatically on schedule

### Option 3: macOS LaunchD

See [CRON_SETUP.md](./CRON_SETUP.md) for `plist` configuration.

## For AI Agents

This vault is designed to be easily extended by AI agents.

### Adding a New Topic

```python
# Using the helper script
python update_index.py "Topic Name" folder-name

# Or edit index.md directly
# Add a line like: | Topic Name | active | folder-name |
```

### Understanding the Learning Format

Daily notes follow this structure:

```markdown
# Learning: Python — 2025-01-15

## What I Learned Today

1. **Point Title**: Brief explanation in simple terms

## Key Takeaways

- Takeaway 1
- Takeaway 2

## Tomorrow's Focus

- What to explore next
```

### Modifying the Generation Prompt

Edit the `SYSTEM_PROMPT` constant in `scripts/daily-learning.sh` to customize the learning style or format.

## Troubleshooting

### Script fails with "No topics found"

Check that:
1. `index.md` exists and is readable
2. Topics have `active` status
3. Table format is correct (pipes `|` and hyphens `-`)

### API Errors

- **Rate limit**: Wait and retry, or set `AI_RATE_LIMIT_WAIT` to add delays
- **Auth error**: Verify your API key is correct
- **Quota exceeded**: Check your API account usage

### Git Push Fails

Ensure you have push permissions:
```bash
git push origin main
```

Or use a personal access token:
```bash
git remote set-url origin https://YOUR_TOKEN@github.com/owner/repo.git
```

## Contributing

This vault is open for improvement. Submit PRs for:
- Enhanced learning generation prompts
- Additional AI provider support
- Better formatting templates
- Documentation improvements

## License

MIT License - Use freely for your own learning vault.
