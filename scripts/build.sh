#!/bin/bash

uv pip install pyinstaller

pyinstaller --onefile \
  --name juadaqr \
  --add-data "src/juadaqr:templates" \
  --hidden-import qrcode \
  src/juadaqr/cli.py

echo "Binary created in dist/juadaqr"
