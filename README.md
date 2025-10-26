```markdown
# File Organizer

A powerful and professional file organizer CLI tool that organizes files into folders based on their extensions. It supports dry-run mode, conflict resolution strategies, deduplication, and can be built into a standalone executable.

## Features
- **Organize Files**: Automatically move files into folders based on their extensions.
- **Preview Mode**: See the planned moves before actually executing them.
- **Dry-Run by Default**: Perform a test run without making changes.
- **Conflict Handling**: Choose how to handle file name conflicts (`suffix`, `overwrite`, or `skip`).
- **Deduplication**: Skip moving duplicate files by comparing their hashes.
- **Custom Rules**: Provide your own JSON or YAML rules for organizing files.
- **Executable**: Build a standalone `.exe` or binary for distribution.

---

## Installation

### Running Locally
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/lopiphysicslover-blip/file-organizer.git
   cd file-organizer
   ```

2. **Create and Activate a Virtual Environment**:
   ```bash
   python -m venv .venv
   source .venv/bin/activate   # Windows: .venv\Scripts\activate
   ```

3. **Install Dependencies**:
   ```bash
   pip install typer rich PyYAML
   ```

4. **Run the CLI**:
   ```bash
   python file_organizer.py --help
   ```

---

## Usage

### Commands
1. **Preview Planned Moves**:
   ```bash
   python file_organizer.py preview /path/to/folder
   ```
   This will display the source and destination paths for files that match the organizing rules.

2. **Organize Files**:
   - Dry-run (default):
     ```bash
     python file_organizer.py organize /path/to/folder
     ```
     This will simulate the organization process without actually moving files.

   - Perform Actual Moves:
     ```bash
     python file_organizer.py organize /path/to/folder --no-dry-run
     ```

3. **Custom Rules**:
   Provide a JSON or YAML file with custom organizing rules:
   ```bash
   python file_organizer.py organize /path/to/folder --rules /path/to/rules.json
   ```

4. **Conflict Handling**:
   Specify how to handle conflicts (`suffix`, `overwrite`, or `skip`):
   ```bash
   python file_organizer.py organize /path/to/folder --conflict overwrite
   ```

5. **Deduplication**:
   Skip moving files that already exist in the target location:
   ```bash
   python file_organizer.py organize /path/to/folder --dedupe
   ```

---

## Rules Format
Rules map file extensions to folder names. Supported formats:

### JSON Example
```json
{
  "jpg": "Images",
  "png": "Images",
  "pdf": "Documents",
  "txt": "Text"
}
```

### YAML Example
```yaml
Images:
  - jpg
  - png
Documents:
  - pdf
  - docx
Text:
  - txt
```

---

## Building an Executable

### Requirements
1. Install PyInstaller:
   ```bash
   pip install pyinstaller
   ```

### Build Process
1. Run the build script (Windows):
   ```bash
   build_exe.bat
   ```
   This will create a `file-organizer.exe` file in the `dist/` directory.

2. Run the build script (Unix/macOS):
   ```bash
   ./build_exe.sh
   ```
   This will create a `file-organizer` binary in the `dist/` directory.

---

## Example Workflow

1. Clone the repository and set up the environment:
   ```bash
   git clone https://github.com/lopiphysicslover-blip/file-organizer.git
   cd file-organizer
   python -m venv .venv
   source .venv/bin/activate
   pip install typer rich PyYAML
   python file_organizer.py --help
   ```

2. Preview planned moves:
   ```bash
   python file_organizer.py preview ./downloads
   ```

3. Perform actual moves with deduplication enabled:
   ```bash
   python file_organizer.py organize ./downloads --no-dry-run --dedupe
   ```

4. Build an executable for distribution:
   ```bash
   build_exe.bat   # Windows
   ./build_exe.sh  # Unix/macOS
   ```

---

## Contact Me
For questions, feedback, or support, feel free to join my Discord server using the link below:

[Join the Discord Server](https://discord.com/invite/SqyFzxZdjH)

---

## License
This project is licensed under the MIT License. See the [LICENSE](./LICENSE) file for details.
