@echo off
REM Build Windows executable using PyInstaller
pip install pyinstaller
pyinstaller --noconfirm --onefile --name "file-organizer" file_organizer.py
echo Done! Check dist\file-organizer.exe
pause