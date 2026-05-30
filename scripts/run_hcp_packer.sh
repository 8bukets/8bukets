#!/bin/bash

# Exit immediately if a command exits with a non-zero status
set -e

echo "================================================================"
echo " HCP Packer Build Script"
echo "================================================================"

# Verify required environment variables are set
REQUIRED_VARS=("HCP_CLIENT_ID" "HCP_CLIENT_SECRET" "HCP_PROJECT_ID" "AWS_ACCESS_KEY_ID" "AWS_SECRET_ACCESS_KEY" "AWS_DEFAULT_REGION")

missing_vars=false
for var in "${REQUIRED_VARS[@]}"; do
    if [ -z "${!var}" ]; then
        echo "❌ Error: Required environment variable $var is not set."
        missing_vars=true
    fi
done

if [ "$missing_vars" = true ]; then
    echo ""
    echo "Please set the missing variables before running this script:"
    echo "  export HCP_CLIENT_ID=<your_client_id>"
    echo "  export HCP_CLIENT_SECRET=<your_client_secret>"
    echo "  export HCP_PROJECT_ID=<your_project_id>"
    echo "  export AWS_ACCESS_KEY_ID=<your_aws_access_key>"
    echo "  export AWS_SECRET_ACCESS_KEY=<your_aws_secret_key>"
    echo "  export AWS_DEFAULT_REGION=<e.g., us-east-2>"
    exit 1
fi

echo "✅ All required credentials found."

# Navigate to the tutorial directory
cd hcp-packer-tutorial

echo ""
echo "📦 Initializing Packer..."
packer init .

echo ""
echo "📝 Formatting Packer templates..."
packer fmt .

echo ""
echo "🚀 Building AMIs and pushing metadata to HCP Packer Registry..."
packer build ubuntu-focal.pkr.hcl

echo ""
echo "🎉 Build completed successfully!"
echo "Check your HCP Packer dashboard and AWS AMI console to verify the artifacts."
