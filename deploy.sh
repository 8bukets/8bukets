#!/bin/bash
set -e

echo "🚀 Starting Deployment Process..."

# 1. Environment Setup
echo "📦 Installing dependencies..."
pip install -r requirements.txt

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
    nohup python3 run_system.py --loop --token "$SYSTEM_AUTH_TOKEN" > results/system.log 2>&1 &
    echo "✅ System started. Monitor with: ./status.sh"
else
    echo "✅ Deployment ready. To start the system loop manually:"
    echo "SYSTEM_AUTH_TOKEN=your_token ./deploy.sh --loop"
fi
