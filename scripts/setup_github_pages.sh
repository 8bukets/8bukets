#!/bin/bash

# Exit on error
set -e

# Configuration
SITE_DIR="github-pages-site"
THEME="jekyll-theme-minimal"
TITLE="Octocat's homepage"
DESCRIPTION="Bookmark this to keep an eye on my project updates!"

# Create directory
echo "Creating directory $SITE_DIR..."
mkdir -p "$SITE_DIR"

# Initialize Git repository
echo "Initializing Git repository in $SITE_DIR..."
cd "$SITE_DIR"
git init

# Create README.md
echo "Creating README.md..."
cat << EOF > README.md
# $TITLE

Welcome to my GitHub Pages website!
EOF

# Create _config.yml
echo "Creating _config.yml..."
cat << EOF > _config.yml
theme: $THEME
title: $TITLE
description: $DESCRIPTION
EOF

# Add and commit files
echo "Adding and committing files..."
git add README.md _config.yml
git commit -m "Initial commit: Add GitHub Pages site files"

echo "GitHub Pages site setup complete in $SITE_DIR!"
