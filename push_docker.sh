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

# Docker Build Cloud Integration
if [ -n "$DOCKER_BUILD_CLOUD_ORG" ] && [ -n "$DOCKER_BUILD_CLOUD_BUILDER" ]; then
    echo "☁️ Detected Docker Build Cloud configuration. Adding cloud builder endpoint..."
    docker buildx create --use --driver cloud "${DOCKER_BUILD_CLOUD_ORG}/${DOCKER_BUILD_CLOUD_BUILDER}"
    echo "☁️ Using Docker Build Cloud builder: ${DOCKER_BUILD_CLOUD_ORG}/${DOCKER_BUILD_CLOUD_BUILDER}"

    # Build the image using buildx and push
    echo "🔨 Building and pushing the Docker image using Docker Build Cloud..."
    docker buildx build --push -t "$IMAGE_NAME:$TAG_NAME" .
else
    # Build the image
    echo "🔨 Building the Docker image locally..."
    docker build -t "$IMAGE_NAME:$TAG_NAME" .

    # Push the image
    echo "📤 Pushing the Docker image to registry..."
    docker push "$IMAGE_NAME:$TAG_NAME"
fi

echo "✅ Successfully pushed $IMAGE_NAME:$TAG_NAME"
