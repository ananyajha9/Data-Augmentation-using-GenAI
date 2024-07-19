import os

def rename_files(folder_path):
    files = os.listdir(folder_path)
    files.sort()
    for index, file_name in enumerate(files):
        file_extension = os.path.splitext(file_name)[1]
        new_file_name = f"{index+1:03d}{file_extension}"  # Padding with leading zeros for sorting
        print(new_file_name)
        os.rename(os.path.join(folder_path, file_name), os.path.join(folder_path, new_file_name))
    print("Files renamed successfully.")

# Example usage:
folder_path = "C:/Users/omkar/omkar_/PES/TDL_Project/images"
rename_files(folder_path)
