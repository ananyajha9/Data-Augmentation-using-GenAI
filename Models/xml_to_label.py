import os
from xml.etree import ElementTree as ET

def convert_to_yolo(annotation_xml):
  root = ET.fromstring(annotation_xml)

  # Get image width and height
  width = int(root.find("size/width").text)
  height = int(root.find("size/height").text)

  # Get object information
  labels = []
  for object in root.findall("object"):
    object_label = object.find("name").text
    xmin = float(object.find("bndbox/xmin").text)
    ymin = float(object.find("bndbox/ymin").text)
    xmax = float(object.find("bndbox/xmax").text)
    ymax = float(object.find("bndbox/ymax").text)

    # Convert bounding box coordinates to normalized format (0-1)
    x_center = (xmin + xmax) / 2.0 / width
    y_center = (ymin + ymax) / 2.0 / height
    box_width = (xmax - xmin) / width
    box_height = (ymax - ymin) / height

    # Create YOLO label string
    label_string = f"{object_label} {x_center} {y_center} {box_width} {box_height}"
    labels.append(label_string)

  return "\n".join(labels)  # Join labels with newline

def convert_folder(folder_path, output_folder):
  for filename in os.listdir(folder_path):
    if filename.endswith(".xml"):
      xml_path = os.path.join(folder_path, filename)
      with open(xml_path, "r") as f:
        annotation_xml = f.read()

      yolo_label = convert_to_yolo(annotation_xml)

      # Generate output filename (replace .xml with .txt)
      output_filename = os.path.splitext(filename)[0] + ".txt"
      output_path = os.path.join(output_folder, output_filename)

      with open(output_path, "w") as f:
        f.write(yolo_label)

# Example usage
folder_path = ""
output_folder_path = "C:/Users/omkar/omkar_/PES/TDL_Project/Ver1/old_labels"
convert_folder(folder_path, output_folder_path)
