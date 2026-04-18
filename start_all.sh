#!/bin/bash

# Antigravity Autonomous Ecosystem - Master Start Script
# Orchestrates Docker, Health Checks, and Next.js 16

echo "🚀 [Antigravity] Starting full-stack autonomous ecosystem..."

# 1. Start Docker Services (MongoDB)
echo "🐳 [Docker] Initializing containers..."
if command -v docker-compose &> /dev/null
then
    docker-compose up -d
else
    docker compose up -d
fi

# 2. Verify Environment and Health
echo "🔍 [Explorer] Running autonomous health scan..."
npx tsx antigravity/explorer.ts

# 3. Handle existing dev servers
echo "🧹 [Cleanup] Checking for existing dev servers..."
pkill -f "next dev" || echo "No existing dev servers found."

# 4. Start Next.js Development Server
echo "⚡ [Next.js] Launching dashboard with Turbopack..."
npm run dev
