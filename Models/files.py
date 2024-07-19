import os
import shutil

def check_and_delete_files(images_folder, labels_folder):
    # Get list of files in source folder
    source_files = os.listdir(labels_folder)

    
    # Iterate through each file in the source folder
    for file_name in source_files:
        file = file_name[:-4]
        source_file_path = os.path.join(labels_folder, file_name)
        target_file_path = os.path.join(images_folder, file+'.jpg')

        if not os.path.exists(target_file_path):
            print(target_file_path)
            os.remove(source_file_path)

        

# Example usage
images_folder = "C:/Users/omkar/omkar_/PES/TDL_Project/Ver1/old_images"
labels_folder = "C:/Users/omkar/omkar_/PES/TDL_Project/Ver1/old_labels"

check_and_delete_files(images_folder, labels_folder)
