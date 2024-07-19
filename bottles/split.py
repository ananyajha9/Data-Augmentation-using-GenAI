import os
import shutil
from sklearn.model_selection import train_test_split

def split_data(source_folder,labels_folder, destination_folder, test_size=0.1, val_size=0.1):

    count = 0
    # Create destination folders if they don't exist
    for folder in ['train', 'test', 'val']:
        folder_path = os.path.join(destination_folder, folder)
        os.makedirs(folder_path, exist_ok=True)

    # Get list of all image files in the source folder
    image_files = [f for f in os.listdir(source_folder) if f.endswith(('.jpg', '.png', '.jpeg'))]
    label_files = [f for f in os.listdir(labels_folder) if f.endswith(('.txt'))]

    # Split data into train, test, and validation sets
    train_files, test_val_files = train_test_split(image_files, test_size=(test_size + val_size), random_state=42)
    test_files, val_files = train_test_split(test_val_files, test_size=(val_size / (test_size + val_size)), random_state=42)

    train_files_l, val_files_l, test_files_l = [], [], []


    for i in train_files:
        for j in label_files:
            #print(i[:-4])
            if i[:3] == j[:3]:
                print(i[:3], "  ", j[:3])
                count += 1
                train_files_l.append(j)

    for i in test_files:
        for j in label_files:
            #print(i+"  "+j)
            if i[:3] == j[:3]:
                count += 1
                test_files_l.append(j)

    for i in val_files:
        for j in label_files:
            #print(i+"  "+j)
            if i[:3] == j[:3]:
                count += 1
                val_files_l.append(j)


    # Move files to the corresponding folders
    move_files(train_files, source_folder, os.path.join(destination_folder, 'train/images'))
    move_files(test_files, source_folder, os.path.join(destination_folder, 'test/images'))
    move_files(val_files, source_folder, os.path.join(destination_folder, 'val/images'))
    move_files(train_files_l, labels_folder, os.path.join(destination_folder, 'train/labels'))
    move_files(test_files_l, labels_folder, os.path.join(destination_folder, 'test/labels'))
    move_files(val_files_l, labels_folder, os.path.join(destination_folder, 'val/labels'))
                
    print(count)

def move_files(files, source_folder, destination_folder):
    for file in files:
        source_path = os.path.join(source_folder, file)
        destination_path = os.path.join(destination_folder, file)
        shutil.move(source_path, destination_path)

if __name__ == "__main__":
    source_folder_path = "C:/Users/omkar/omkar_/PES/TDL_Project/images"
    source2 = "C:/Users/omkar/omkar_/PES/TDL_Project/labels"
    destination_folder_path = "C:/Users/omkar/omkar_/PES/TDL_Project"

    split_data(source_folder_path, source2, destination_folder_path)
