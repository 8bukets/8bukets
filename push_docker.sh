#!/bin/bash
set -e

# Default variables
IMAGE_NAME="getanant/sor"
TAG_NAME="${1:-tagname}"

echo "🚀 Preparing to build and push Docker image: $IMAGE_NAME:$TAG_NAME"

# Check for required credentials
if [ -z "$DOCKER_USERNAME" ] || [ -z "$DOCKER_PASSWORD" ]; then
    echo "❌ Error: DOCKER_USERNAME and DOCKER_PASSWORD environment variables must be set."
    echo "Usage: DOCKER_USERNAME=myuser DOCKER_PASSWORD=mypass ./push_docker.sh [tagname]"
    exit 1
fi

# Login to Docker Hub
echo "🔑 Logging in to Docker Hub..."
echo "$DOCKER_PASSWORD" | docker login -u "$DOCKER_USERNAME" --password-stdin

# Build the image
echo "🔨 Building the Docker image..."
docker build -t "$IMAGE_NAME:$TAG_NAME" .

# Push the image
echo "📤 Pushing the Docker image to registry..."
docker push "$IMAGE_NAME:$TAG_NAME"

echo "✅ Successfully pushed $IMAGE_NAME:$TAG_NAME"
