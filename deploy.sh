#!/bin/bash
set -e

echo "🚀 Starting Deployment Process..."

# 1. Environment Setup
echo "📦 Installing dependencies..."
pip install aiohttp beautifulsoup4 requests pytest pytest-asyncio

# 2. Directory Creation
echo "📂 Creating data and results directories..."
mkdir -p data results

# 3. Run Tests
echo "🧪 Running tests..."
PYTHONPATH=. python3 -m pytest tests/

# 4. Launch System (Dry Run or Service)
echo "✅ Deployment ready. To start the system:"
echo "SYSTEM_AUTH_TOKEN=your_token python3 run_system.py"
