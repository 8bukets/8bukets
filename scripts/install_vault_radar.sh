#!/bin/bash

set -e

VERSION="0.20.0"

# Determine OS and Architecture
OS=$(uname -s | tr '[:upper:]' '[:lower:]')
ARCH=$(uname -m)

if [ "$ARCH" = "x86_64" ]; then
    ARCH="amd64"
elif [ "$ARCH" = "aarch64" ] || [ "$ARCH" = "arm64" ]; then
    ARCH="arm64"
else
    echo "Unsupported architecture: $ARCH"
    return 1 2>/dev/null || true
fi

if [ "$OS" = "darwin" ]; then
    ZIP_FILE="vault-radar_${VERSION}_darwin_${ARCH}.zip"
elif [ "$OS" = "linux" ]; then
    ZIP_FILE="vault-radar_${VERSION}_linux_${ARCH}.zip"
else
    echo "Unsupported operating system: $OS"
    return 1 2>/dev/null || true
fi

echo "Downloading HCP Vault Radar CLI version ${VERSION} for ${OS}/${ARCH}..."
curl -sL -O "https://releases.hashicorp.com/vault-radar/${VERSION}/${ZIP_FILE}"

echo "Unzipping the binary..."
unzip -q -o "${ZIP_FILE}"

if [ "$OS" = "darwin" ]; then
    echo "Removing quarantine attribute..."
    xattr -dr com.apple.quarantine ./vault-radar 2>/dev/null || true
fi

echo "Moving to /usr/local/bin..."
sudo cp vault-radar /usr/local/bin/

echo "Cleaning up..."
rm -f "${ZIP_FILE}" vault-radar

echo "Checking installation..."
vault-radar --version
