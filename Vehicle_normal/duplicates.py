import os

def delete_duplicates(folder_path):
  """
  Deletes duplicate images in a folder, keeping the first encountered image.

  Args:
      folder_path: Path to the folder containing images.
  """
  processed_files = set()
  file_sizes = {}
  for filename in os.listdir(folder_path):
    if filename.endswith((".jpg", ".jpeg", ".png")):
      image_path = os.path.join(folder_path, filename)
      file_size = os.path.getsize(image_path)
      if file_size not in file_sizes:
        file_sizes[file_size] = [image_path]
      else:
        # Check for duplicate size (potential duplicate)
        for existing_file in file_sizes[file_size]:
          if existing_file != image_path:  # Avoid self-comparison
            os.remove(image_path)
            print(f"Deleted duplicate: {image_path}")
            break
        file_sizes[file_size].append(image_path)  # Add current image to size group

# Example usage
folder_path = "C:/Users/omkar/omkar_/PES/TDL_Project/Vehicle_normal/train/images"
delete_duplicates(folder_path)
