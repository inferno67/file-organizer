import os
import shutil
from pathlib import Path

# --- File Organizer ---

# File type categories (you can add more if you want)
FILE_TYPES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp"],
    "Videos": [".mp4", ".mkv", ".mov", ".avi"],
    "Documents": [".pdf", ".docx", ".txt", ".xlsx", ".pptx"],
    "Audio": [".mp3", ".wav", ".aac"],
    "Archives": [".zip", ".rar", ".tar", ".gz"],
    "Code": [".py", ".js", ".html", ".css", ".c", ".cpp", ".java"],
    "Others": []  # everything else
}

def organize_folder(folder_path):
    # Loop through all files in the folder
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)

        # Skip if it's a folder
        if os.path.isdir(file_path):
            continue  

        # Find the file extension
        _, extension = os.path.splitext(filename)
        extension = extension.lower()

        moved = False

        # Check which category the file belongs to
        for category, extensions in FILE_TYPES.items():
            if extension in extensions:
                category_folder = os.path.join(folder_path, category)
                os.makedirs(category_folder, exist_ok=True)
                shutil.move(file_path, os.path.join(category_folder, filename))
                print(f"Moved: {filename} → {category}/")
                moved = True
                break

        # If file doesn’t match any category → move to "Others"
        if not moved:
            category_folder = os.path.join(folder_path, "Others")
            os.makedirs(category_folder, exist_ok=True)
            shutil.move(file_path, os.path.join(category_folder, filename))
            print(f"Moved: {filename} → Others/")

if __name__ == "__main__":
    # Automatically detect Downloads folder
    downloads_path = str(Path.home() / "Downloads")

    choice = input(f"Do you want to organize your Downloads folder? (Y/N): ")

    if choice.lower() == "y":
        folder = downloads_path
    else:
        folder = input("Enter the folder path you want to organize: ")

    if os.path.exists(folder):
        organize_folder(folder)
        print("\n✅ Folder organized successfully!")
    else:
        print("❌ The path does not exist. Try again.")
