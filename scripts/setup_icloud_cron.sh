#!/bin/bash
# macOS iCloud Sync Cron Job Setup
# Sets up a local crontab entry to run the iCloud fix script periodically.

# Define the paths
CRON_JOB="0 * * * * $(pwd)/scripts/fix_icloud_sync.sh >/dev/null 2>&1"
CRON_MARKER="# ANTIGRAVITY_ICLOUD_SYNC"

echo "Setting up hourly cron job for perfect iCloud sync..."

# Check if crontab is available
if ! command -v crontab &> /dev/null; then
    echo "Warning: crontab command not found on this system. Cannot install cron job."
else
    # Check if it already exists
    if crontab -l 2>/dev/null | grep -q "$CRON_MARKER"; then
      echo "Cron job already exists! No action needed."
    else
      # Add the cron job
      (crontab -l 2>/dev/null; echo "$CRON_MARKER"; echo "$CRON_JOB") | crontab -
      echo "Hourly cron job successfully installed."
    fi
fi

echo ""
echo "To manually monitor iCloud in real-time, run: npm run monitor:icloud"
