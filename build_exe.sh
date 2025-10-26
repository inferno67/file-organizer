#!/bin/bash
# Build Unix/macOS executable using PyInstaller
set -e
pip install pyinstaller
pyinstaller --noconfirm --onefile --name file-organizer file_organizer.py
echo "Done! Check dist/file-organizer"