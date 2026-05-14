#!/bin/bash
set -e

echo "🚀 Igniting System's Sovereign Fleet..."

# 1. Start Docker Layer (MongoDB & Frontend)
echo "🐳 Starting Docker Layer..."
docker-compose up -d

# 2. Start TypeScript Autonomous Swarm Loop
echo "🚀 Starting Continuous Autonomous Agent Loop via Node.js..."
if [ -z "$SYSTEM_AUTH_TOKEN" ]; then
    echo "⚠️ SYSTEM_AUTH_TOKEN is not set. Using default_dev_token for local execution."
    export SYSTEM_AUTH_TOKEN="default_dev_token"
fi

nohup npm run ignite > results/system.log 2>&1 &

echo "✅ Fleet ignited. The system is now running with 24/7 background persistence."
echo "Monitor logs using: tail -f results/system.log"