#!/bin/bash

# Antigravity Systemd Installation Script
# Configures and installs Jules Daily Work Cycle as a user-level Systemd unit.

PROJECT_DIR=$(pwd)
NPM_PATH=$(which npm)

if [ -z "$NPM_PATH" ]; then
    echo "❌ [Setup] npm not found. Please ensure Node.js is installed."
    exit 1
fi

echo "🚀 [Setup] Configuring Antigravity Systemd Service..."
echo "📝 [Setup] Project Directory: $PROJECT_DIR"
echo "📦 [Setup] Using npm at: $NPM_PATH"

# Create the user systemd directory if it doesn't exist
mkdir -p "$HOME/.config/systemd/user"

# Generate the service file from template
sed -e "s|PROJECT_DIR|$PROJECT_DIR|g" \
    -e "s|NPM_PATH|$NPM_PATH|g" \
    "scripts/antigravity.service.template" > "$HOME/.config/systemd/user/antigravity.service"

# Copy the timer file
cp scripts/antigravity.timer "$HOME/.config/systemd/user/"

# Reload systemd user daemon
echo "🔋 [Setup] Loading and enabling Systemd units..."
systemctl --user daemon-reload
systemctl --user enable antigravity.timer
systemctl --user start antigravity.timer

echo "✅ [Setup] Antigravity Systemd Automation installed and started."
echo "🗓️  Jules will now execute the daily work cycle every day."
echo "🔍 Check status with: systemctl --user status antigravity.timer"
