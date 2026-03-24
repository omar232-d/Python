import os
import shutil

# Set the folder you want to organize
source_folder = input("Enter the file name:   ")

# File type categories
file_types = {
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "Documents": [".pdf", ".docx", ".txt"],
    "Videos": [".mp4", ".mkv", ".avi"],
    "Music": [".mp3", ".wav"],
    "Archives": [".zip", ".rar"]
}

def organize_files():
    for filename in os.listdir(source_folder):
        file_path = os.path.join(source_folder, filename)

        # Skip if it's a folder
        if os.path.isdir(file_path):
            continue

        # Get file extension
        _, extension = os.path.splitext(filename)

        moved = False

        for folder_name, extensions in file_types.items():
            if extension.lower() in extensions:
                folder_path = os.path.join(source_folder, folder_name)

                # Create folder if it doesn't exist
                if not os.path.exists(folder_path):
                    os.makedirs(folder_path)

                # Move file
                shutil.move(file_path, os.path.join(folder_path, filename))
                print(f"Moved: {filename} → {folder_name}")
                moved = True
                break

        # If file type not recognized
        if not moved:
            other_folder = os.path.join(source_folder, "Others")
            if not os.path.exists(other_folder):
                os.makedirs(other_folder)

            shutil.move(file_path, os.path.join(other_folder, filename))
            print(f"Moved: {filename} → Others")

if __name__ == "__main__":
    organize_files()
    print("✅ Files organized successfully!")