#!/bin/bash

echo "📊 Markposition Autonomous System Status"
echo "---------------------------------------"

if [ -f config/evolution_params.json ]; then
    VERSION=$(grep "current_version" config/evolution_params.json | awk '{print $2}' | tr -d ',')
    echo "🔹 System Version: v$VERSION"
else
    echo "🔸 System Version: Unknown"
fi

LAST_REPORT=$(ls -t results/DAILY_REPORT_*.md 2>/dev/null | head -n 1)
if [ -n "$LAST_REPORT" ]; then
    echo "🔹 Latest Report: $LAST_REPORT"
    echo "🔹 Last Execution Status:"
    grep "Sigma Status" "$LAST_REPORT"
    grep "Total Agent Count" "$LAST_REPORT"
else
    echo "🔸 No reports generated yet."
fi

echo "🔹 Active Processes:"
pgrep -af run_system.py || echo "🔸 System is not running."

echo "---------------------------------------"
