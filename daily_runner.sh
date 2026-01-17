#!/bin/bash
# Autonomous System Daily Runner
# This script is designed to be run by cron or a systemd timer daily.

# 1. Activate Environment (if using venv)
# source venv/bin/activate

# 2. Run the Autonomous System
echo "Starting Daily Autonomous Run: $(date)" >> system.log
python3 run_system.py --limit 10 >> system.log 2>&1

# 3. Rotate Logs (Keep last 7 days)
# (Simple example logic)
find results/ -name "Daily_Report_*.md" -mtime +7 -exec rm {} \;

echo "Run Completed: $(date)" >> system.log
