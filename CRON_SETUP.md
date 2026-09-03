# Cron Setup Guide

This guide covers setting up automated daily runs of the learning vault on various platforms.

## Quick Setup

```bash
# Clone or navigate to vault
cd /path/to/Self-Learning-Obsidian-Vault

# Make script executable
chmod +x scripts/daily-learning.sh

# Test run
./scripts/daily-learning.sh

# Add to crontab
crontab -e
```

---

## Linux Cron

### Basic Cron Setup

```bash
# Edit crontab
crontab -e

# Add one of these lines:
# Run at 8:30 AM daily
30 8 * * * cd /path/to/vault && ./scripts/daily-learning.sh >> /var/log/daily-learning.log 2>&1

# Run at 8:30 AM on weekdays only
30 8 * * 1-5 cd /path/to/vault && ./scripts/daily-learning.sh >> /var/log/daily-learning.log 2>&1
```

### Cron Environment

Cron jobs run with minimal environment. Set explicit paths:

```bash
# Full path to everything
30 8 * * * cd /home/user/Self-Learning-Obsidian-Vault && /usr/bin/python3 scripts/daily-learning.sh >> /home/user/logs/daily-learning.log 2>&1
```

### Required Environment Variables

Add to crontab or create a wrapper script:

```bash
# In crontab, set variables before command
OPENAI_API_KEY="sk-..."
AI_PROVIDER="openai"
30 8 * * * cd /path/to/vault && ./scripts/daily-learning.sh
```

Or use a wrapper script (`run-daily.sh`):

```bash
#!/bin/bash
export OPENAI_API_KEY="sk-..."
export AI_PROVIDER="openai"
cd /path/to/vault
./scripts/daily-learning.sh
```

### Cron Log Location

```bash
# Common log locations
/var/log/syslog        # Debian/Ubuntu
/var/log/cron          # CentOS/RHEL
~/logs/daily-learning.log  # User-defined
```

Check cron logs:
```bash
grep CRON /var/log/syslog
tail -f /var/log/syslog | grep CRON
```

### Troubleshooting Cron

**Script runs but API fails:**
- Ensure environment variables are set
- Use absolute paths in crontab

**No output:**
- Check cron log for errors
- Ensure script has execute permission

**Git push fails:**
- Use SSH key authentication
- Or use token-based remote URL

---

## GitHub Actions (Recommended)

The repository includes `.github/workflows/daily-learning.yml`. Enable it:

1. Go to **Settings → Secrets** in your GitHub repo
2. Add `OPENAI_API_KEY` secret
3. The workflow runs automatically at 8:00 AM UTC daily

### Manual Trigger

Go to **Actions** tab → **Daily Learning** → **Run workflow**

### Modifying Schedule

Edit `.github/workflows/daily-learning.yml`:

```yaml
on:
  schedule:
    - cron: '0 8 * * *'  # 8:00 AM UTC daily
  # Or use GitHub's predefined times
  # - cron: '0 8 * * *'   # 8:00 AM
  # - cron: '30 8 * * *'  # 8:30 AM
```

---

## macOS LaunchD

### Create Plist File

Location: `~/Library/LaunchAgents/com.learning-vault.daily.plist`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>Label</key>
    <string>com.learning-vault.daily</string>
    <key>ProgramArguments</key>
    <array>
        <string>/usr/bin/python3</string>
        <string>/path/to/vault/scripts/daily-learning.sh</string>
    </array>
    <key>WorkingDirectory</key>
    <string>/path/to/vault</string>
    <key>EnvironmentVariables</key>
    <dict>
        <key>OPENAI_API_KEY</key>
        <string>sk-...</string>
    </dict>
    <key>StartCalendarInterval</key>
    <dict>
        <key>Hour</key>
        <integer>8</integer>
        <key>Minute</key>
        <integer>30</integer>
    </dict>
    <key>RunAtLoad</key>
    <false/>
</dict>
</plist>
```

### Load/Unload

```bash
# Load the agent
launchctl load ~/Library/LaunchAgents/com.learning-vault.daily.plist

# Unload (to stop)
launchctl unload ~/Library/LaunchAgents/com.learning-vault.daily.plist

# View logs
log show --predicate 'process == "daily-learning"' --last 24h
```

---

## systemd Timer (Linux)

### Create Service File

`/etc/systemd/system/daily-learning.service`:

```ini
[Unit]
Description=Daily Learning Vault

[Service]
Type=oneshot
ExecStart=/path/to/vault/scripts/daily-learning.sh
WorkingDirectory=/path/to/vault
Environment=OPENAI_API_KEY=sk-...
Environment=AI_PROVIDER=openai
User=your-user
```

### Create Timer File

`/etc/systemd/system/daily-learning.timer`:

```ini
[Unit]
Description=Daily Learning Vault Timer

[Timer]
OnCalendar=*-*-* 08:30:00
Persistent=true

[Install]
WantedBy=timers.target
```

### Enable Timer

```bash
sudo systemctl daemon-reload
sudo systemctl enable daily-learning.timer
sudo systemctl start daily-learning.timer

# Check status
systemctl list-timers daily-learning.timer
journalctl -u daily-learning.service
```

---

## Docker (Alternative)

Run in a Docker container for isolation:

```bash
docker run -d \
  --name daily-learning \
  -v /path/to/vault:/vault \
  -e OPENAI_API_KEY=sk-... \
  -e VAULT_DIR=/vault \
  python:3.11 \
  python /vault/scripts/daily-learning.sh
```

Schedule with Docker Compose and an external cron.

---

## Verification Checklist

After setup, verify:

- [ ] Script is executable (`chmod +x scripts/daily-learning.sh`)
- [ ] API key is set in environment
- [ ] Script runs without errors manually
- [ ] Cron/Action triggers at expected time
- [ ] Git push works from cron/scheduled context
- [ ] Files are created in correct locations
- [ ] Logs show successful execution

---

## Common Issues

| Issue | Solution |
|-------|----------|
| "command not found" | Use absolute paths in cron |
| API auth failure | Verify API key in environment |
| Git push fails | Use SSH key or token auth |
| No output in logs | Check cron is running: `systemctl status cron` |
| Wrong timezone | Adjust cron time or use UTC |
