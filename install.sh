#!/bin/bash

set -e

OS=$(uname -s | tr '[:upper:]' '[:lower:]')
ARCH=$(uname -m)

case $ARCH in
x86_64) ARCH="amd64" ;;
aarch64) ARCH="arm64" ;;
arm64) ARCH="arm64" ;;
esac

BINARY_URL="https://github.com/juadadev/juadaqr/releases/latest/download/juadaqr-${OS}-${ARCH}"

echo "Downloading juadaqr for ${OS}/${ARCH}..."
curl -L -o juadaqr "$BINARY_URL"

chmod +x juadaqr

# Require sudo
if [ -w "/usr/local/bin" ]; then
  mv juadaqr /usr/local/bin/
else
  sudo mv juadaqr /usr/local/bin/
fi

echo "juadaqr installed in /usr/local/bin/juadaqr"
echo "Use: juadaqr <url>"
