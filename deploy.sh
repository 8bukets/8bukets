#!/bin/bash
set -e

echo "🚀 Starting Deployment Process..."

# 1. Environment Setup
echo "📦 Installing dependencies..."
pip install aiohttp beautifulsoup4 requests pytest pytest-asyncio

# 2. Directory Creation
echo "📂 Creating data and results directories..."
mkdir -p data results config

# 3. Run Tests
echo "🧪 Running tests..."
PYTHONPATH=. python3 -m pytest tests/

# 4. Final Verification
echo "🔍 Performing final structural verification..."
PYTHONPATH=. python3 verify_upgrade.py

# 5. Launch System
if [[ "$1" == "--loop" ]]; then
    echo "🔄 Starting autonomous system in background LOOP mode..."
    # Ensure token is set
    if [ -z "$SYSTEM_AUTH_TOKEN" ]; then
        echo "❌ ERROR: SYSTEM_AUTH_TOKEN is not set. Cannot start loop."
        exit 1
    fi
    # Create a wrapper script to handle the 24-hour sleep loop
    cat << 'LOOPEOF' > loop_runner.sh
#!/bin/bash
while true; do
    echo "Starting common_run.py execution cycle at \$(date)..."
    python3 common_run.py
    echo "Cycle complete. Sleeping for 24 hours..."
    sleep 86400
done
LOOPEOF
    chmod +x loop_runner.sh

    bash -c 'nohup ./loop_runner.sh > results/system.log 2>&1 &'
    echo "✅ System started using common_run.py on a 24-hour loop. Monitor with: tail -f results/system.log"
else
    echo "✅ Deployment ready. To start the system loop manually:"
    echo "SYSTEM_AUTH_TOKEN=your_token ./deploy.sh --loop"
fi
