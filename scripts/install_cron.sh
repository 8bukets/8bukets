#!/bin/bash

# Antigravity Cron Installation Script
# Automatically configures and installs the Jules Daily Work Cycle in crontab.

PROJECT_DIR=$(pwd)
USERNAME=$(whoami)
CRON_JOB="0 0 * * * cd $PROJECT_DIR && npm run daily >> $PROJECT_DIR/jules_daily.log 2>&1"

echo "🚀 [Setup] Installing Antigravity Jules Cron Job..."

# Check if we are on Linux (or other non-macOS system where cron is common)
if [[ "$OSTYPE" == "darwin"* ]]; then
  echo "ℹ️ [Setup] macOS detected. While cron works, Launchd is preferred. Use scripts/install_launchd.sh instead."
fi

# Detect npm and node path for absolute accuracy in cron
NPM_PATH=$(which npm)
NODE_PATH=$(which node)

if [ -z "$NPM_PATH" ]; then
  echo "❌ [Setup] npm not found in PATH."
  exit 1
fi

# We need the full path to npm/node in cron usually, or at least a good PATH
# But easier is to use cd $PROJECT_DIR && npm run daily if npm is in user's default cron path.
# To be safe, we'll try to use the absolute path and set a basic PATH
BIN_DIR=$(dirname "$NPM_PATH")
CRON_JOB="0 0 * * * PATH=$BIN_DIR:/usr/local/bin:/usr/bin:/bin cd $PROJECT_DIR && $NPM_PATH run daily >> $PROJECT_DIR/jules_daily.log 2>&1"

# Check if job already exists
crontab -l 2>/dev/null | grep -F "$PROJECT_DIR && $NPM_PATH run daily" > /dev/null
if [ $? -eq 0 ]; then
  echo "✅ [Setup] Cron job already exists."
else
  # Append new cron job
  (crontab -l 2>/dev/null; echo "$CRON_JOB") | crontab -
  echo "✅ [Setup] Antigravity Jules Cron Job installed successfully."
fi

echo "🗓️  Jules will now execute the daily work cycle every day at midnight."
echo "📝 Logs will be written to $PROJECT_DIR/jules_daily.log"
