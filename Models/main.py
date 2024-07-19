import os
print("Importing modules")
import shutil
import cv2
import stable_diffusion
import pix2pix
from PIL import Image
print("Finished importing modules")

def copy_image_label(old_images_path, old_labels_path, new_images_path, new_labels_path, number_of_duplicates, prompt, model):

  for filename in os.listdir(old_images_path):
    # Get the full paths for image and label
    print(filename)
    filename_image = filename
    filename_label = filename[:-4]+".txt"
    image_path = os.path.join(old_images_path, filename_image)
    label_path = os.path.join(old_labels_path, filename_label)

    # Check if it's a file (not a directory)
    if os.path.isfile(image_path):
      # generate N number of ne images and labels
      
      for i in range(number_of_duplicates):
        print(i)
        output_filename_image = filename_image[:-4]+"_"+str(i)+".jpg"
        output_filename_label = filename_label[:-4]+"_"+str(i)+".txt"
        # Copy the image
        new_image_path = os.path.join(new_images_path, output_filename_image)
        # os. shutil.copy2(image_path, new_image_path)

        print("Running Model...")

        if (model == "pix2pix"):
          new_img = pix2pix.generate_new_image_pix2pix(image_path, prompt[i])
        else:
          new_img = stable_diffusion.generate_new_image(image_path, prompt[i])

        new_img.save(new_image_path)

        print('Finished Runnign Model')

        # Copy the label
        new_label_path = os.path.join(new_labels_path, output_filename_label)
        shutil.copy2(label_path, new_label_path)

        print(f"Copied {output_filename_image} to new folders.")

# Replace these paths with your actual folder locations
old_images_path = "C:/Users/omkar/omkar_/PES/TDL_Project/Ver1/old_images"
old_labels_path = "C:/Users/omkar/omkar_/PES/TDL_Project/Ver1/old_labels"
new_images_path = "C:/Users/omkar/omkar_/PES/TDL_Project/Ver1/new_images"
new_labels_path = "C:/Users/omkar/omkar_/PES/TDL_Project/Ver1/new_labels"

number_of_duplicates = 3
prompt = ["Make the bottle metallic", "Put the bottle in a park", "Make the bottle plastic"]

# Call the function
copy_image_label(old_images_path, old_labels_path, new_images_path, new_labels_path, number_of_duplicates, prompt, " ")
