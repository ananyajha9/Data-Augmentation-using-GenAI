from PIL import Image
import os

def compress_jpeg(input_folder, output_folder, quality):
  """
  Converts all JPEG images in a folder to JPG and compresses them.

  Args:
    input_folder: Path to the folder containing the JPEG images.
    output_folder: Path to the folder where the compressed JPG images will be saved. (optional)
    quality: The quality level of the compressed JPG image (1-95, lower means smaller size).
  """
  # Create output folder if it doesn't exist
  if not os.path.exists(output_folder):
    os.makedirs(output_folder)

  for filename in os.listdir(input_folder):
    if filename.lower().endswith(".jpg"):
      filepath = os.path.join(input_folder, filename)
      image = Image.open(filepath)
      # Change format to JPG and adjust quality
      image.save(os.path.join(output_folder, os.path.splitext(filename)[0] + ".jpg"), "JPEG", quality=quality)

# Example usage
input_folder = "C:/Users/omkar/omkar_/PES/TDL_Project/Ver1/old_images"  # Replace with your folder path
output_folder = "C:/Users/omkar/omkar_/PES/TDL_Project/Ver1/train"  # Optional, compressed images will be saved in the same folder by default
quality = 30  # Adjust quality as needed (1-95)

compress_jpeg(input_folder, output_folder, quality)
print("Images compressed successfully!")
