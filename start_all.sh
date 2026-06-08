#!/bin/bash

# Antigravity Autonomous Ecosystem - Consolidated Master Ignition
# Phase 14: Enterprise Sovereign Synthesis

ROOT_DIR="/Users/filipkeser/Documents/Antigravity"
echo "🚀 [Antigravity] Igniting Consolidated Sovereign Fleet in $ROOT_DIR..."

cd "$ROOT_DIR"

# 1. Start Docker Services (MongoDB & Persistence Layer)
echo "🐳 [Docker] Initializing core containers..."
docker compose up -d

# 2. Trigger Autonomous Work Cycle (Enterprise Selection)
echo "🧠 [Jules] Commencing initial autonomous work cycle..."
# Use node directly to ensure the right environment
/usr/local/bin/npm run daily

# 3. Handle existing dev servers
echo "🧹 [Cleanup] Clearing legacy network ports..."
pkill -f "next dev" || echo "No existing dev servers found."

# 4. Note on Dashboard
echo "🌐 [Web-App] Handing off to dedicated com.sigma.web_app service..."
# The dashboard is now managed directly by launchd for granular resilience.

echo "✅ [Antigravity] Fleet Orchestration Sequence Complete."
echo "🌍 Executive Dashboard managed by com.sigma.web_app"
echo "🤖 Jules Persistent Intelligence is active."
