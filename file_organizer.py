# os is imported here to do here with file and folders or operating system like deleting or removning the file and so on 
import os
# shutil is used here to move the file from one place to another
import shutil

# 👉 Change this to the folder you want to organize
folder_path = "C:/Users/YourName/Downloads"

# File type categories
file_types = {
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "Documents": [".pdf", ".docx", ".txt"],
    "Videos": [".mp4", ".mkv", ".mov"],
    "Music": [".mp3", ".wav"],
    "Archives": [".zip", ".rar"],
}

def organize_files(path):
    for file in os.listdir(path):
        file_path = os.path.join(path, file)

        # Skip folders
        if os.path.isdir(file_path):
            continue

        # Get file extension
        _, ext = os.path.splitext(file)

        moved = False

        # Check file type and move
        for folder_name, extensions in file_types.items():
            if ext.lower() in extensions:
                target_folder = os.path.join(path, folder_name)
                os.makedirs(target_folder, exist_ok=True)
                shutil.move(file_path, os.path.join(target_folder, file))
                print(f"Moved: {file} → {folder_name}/")
                moved = True
                break

        # If no match, move to Others
        if not moved:
            others_folder = os.path.join(path, "Others")
            os.makedirs(others_folder, exist_ok=True)
            shutil.move(file_path, os.path.join(others_folder, file))
            print(f"Moved: {file} → Others/")

if __name__ == "__main__":
    organize_files(folder_path)
    print("Done organizing files!")