#!/bin/bash

# Exit immediately if a command exits with a non-zero status
set -e

# Ensure required environment variables are present
if [ -z "$DOCKER_USERNAME" ]; then
    echo "Error: DOCKER_USERNAME environment variable is not set."
    exit 1
fi

if [ -z "$DOCKER_PASSWORD" ]; then
    echo "Error: DOCKER_PASSWORD environment variable is not set."
    exit 1
fi

echo "Building Docker image..."
make docker-build

echo "Pushing Docker image..."
make docker-push

echo "Docker image build and push completed successfully."
