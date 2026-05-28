#!/bin/sh

set -e

echo "Installing juadaqr..."

if ! command -v uv >/dev/null 2>&1; then
  echo "Installing uv..."
  curl -LsSf https://astral.sh/uv/install.sh | sh
  export PATH="$HOME/.local/bin:$PATH"
fi

echo "Installing juadaqr..."
uv tool install juadaqr

echo ""
echo "¡Installing completed!"
echo ""
echo "Use: juadaqr <URL>"
echo "Example: juadaqr https://github.com/juadadev"
