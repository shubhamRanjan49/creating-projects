import os
import shutil

# Specify the folder to organize (e.g., Downloads)
source_folder = '/path/to/your/downloads/folder'

# Define destination folders based on file types
dest_folders = {
    'Documents': ['pdf', 'docx', 'txt', 'xlsx'],
    'Images': ['jpg', 'jpeg', 'png', 'gif'],
    'Videos': ['mp4', 'avi', 'mkv'],
    'Music': ['mp3', 'wav'],
    'Archives': ['zip', 'rar', '7z'],
}

# Create the destination folders if they don't exist
for folder in dest_folders.keys():
    folder_path = os.path.join(source_folder, folder)
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

# Function to move files to the respective folders
def organize_files():
    for filename in os.listdir(source_folder):
        file_path = os.path.join(source_folder, filename)
        
        # Skip directories
        if os.path.isdir(file_path):
            continue
        
        # Get the file extension
        file_extension = filename.split('.')[-1].lower()
        
        # Check and move the file to the corresponding folder
        moved = False
        for folder, extensions in dest_folders.items():
            if file_extension in extensions:
                dest_path = os.path.join(source_folder, folder, filename)
                shutil.move(file_path, dest_path)
                print(f"Moved: {filename} -> {folder}")
                moved = True
                break
        
        # If file extension not found in known categories, move to 'Others'
        if not moved:
            others_folder = os.path.join(source_folder, 'Others')
            if not os.path.exists(others_folder):
                os.makedirs(others_folder)
            shutil.move(file_path, os.path.join(others_folder, filename))
            print(f"Moved: {filename} -> Others")

if __name__ == "__main__":
    organize_files()
