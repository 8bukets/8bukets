#!/bin/bash
# Antigravity Deployment Loop
# Runs the autonomous work cycle every 10 minutes for 3 hours (18 iterations)

echo "🚀 [Deployment Loop] Initiating 3-hour stress test..."
LOG_FILE="logs/deploy_loop.log"

for i in {1..18}
do
    echo "-------------------------------------------" | tee -a "$LOG_FILE"
    echo "📊 Iteration $i/18 - Started at: $(date)" | tee -a "$LOG_FILE"
    echo "-------------------------------------------" | tee -a "$LOG_FILE"

    # Run the daily work cycle
    npm run daily >> "$LOG_FILE" 2>&1

    echo "✅ Iteration $i/18 complete." | tee -a "$LOG_FILE"

    if [ $i -lt 18 ]; then
        echo "😴 Sleeping for 10 minutes..." | tee -a "$LOG_FILE"
        sleep 600
    fi
done

echo "🏆 [Deployment Loop] 3-hour stress test completed successfully." | tee -a "$LOG_FILE"
