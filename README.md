# Enhancing Object Detection through Generative AI-Based Data Augmentation Techniques

### Team
- Omkar Jois (PES1UG21CS397)
- Ananya Jha (PES1UG21CS077)
- Kunjam Nanavaty (PES1UG21CS294)
- Bhoomi Bhat (PES1UG21CS138)

### Introduction
Object detection is a crucial task in computer vision with applications ranging from autonomous driving to surveillance systems. However, the performance of object detection models heavily relies on the quality and diversity of the training data. Data augmentation techniques have been widely adopted to address the challenges posed by limited and imbalanced datasets. In this paper, we propose leveraging generative AI methods for data augmentation in object detection tasks. We explore various generative models and augmentation strategies to enhance the performance and robustness of object detection systems.

## Dataset


The Vehicle dataset is a dataset with 810 annotated images, meticulously compiled to serve as a proof of concept for vehicle detection through object recognition systems. Initially curated to challenge the capabilities of contemporary object detection algorithms, this dataset is specifically designed to include a diverse array of vehicles in various environmental settings, angles, and lighting conditions.
![image](https://github.com/omkarjois/TDL_paper/assets/88605020/20e9bd88-4541-4d7d-9f72-0b7454a76126)


The Bottle dataset is  a curated collection comprising 150 images of bottles, forming the cornerstone of a proof of concept aimed at enhancing object detection capabilities. This bottle dataset is characterized by its variety, containing images of bottles of different shapes, sizes, colors, and materials, captured in assorted settings and lighting conditions to mimic real-world complexity.
![image](https://github.com/omkarjois/TDL_paper/assets/88605020/4c54c20d-c59d-46b5-bbe1-1e41874fb9e5)

## Files and how to run them
### Bottles
- The bottles folder contains the train, test, and val folders to train the YOLOv8 model for detecting bottles. This is the dataset with no augmentation.
- The train.py file is used to train the YOLO model. To run it just run ```python3 train.py```
- The test.py is used to test the model on the test1 and test2 videos. To test the video srun ```python3 test.py```. It will create an out.mp4 folder with the result.
- To change the test videos for testing, open the test.py file and change the path in the ```VideoCapture()``` function to your desired path.

### Vehicles_new
- The Vehicles_new folder contains the train, test, and val folders to train the YOLOv8 model for detecting vehicles.  This is the dataset with no augmentation.
- The train.py file is used to train the YOLO model. To run it just run ```python3 train.py```
- The test.py is used to test the model on the test1 and test2 videos. To test the video srun ```python3 test.py```. It will create an out.mp4 folder with the result.
- To change the test videos for testing, open the test.py file and change the path in the ```VideoCapture()``` function to your desired path.
#### Model Performance
![WhatsApp Image 2024-04-17 at 10 57 32_654feef5](https://github.com/omkarjois/TDL_paper/assets/88605020/ccc7da34-a1a3-49bb-bb66-36e8c4692a90)

  
### Vehicles_normal 
- The Vehicles_normal folder contains the train, test, and val folders to train the YOLOv8 model for detecting vehicles.  This is the dataset with augmentation.
- The train.py file is used to train the YOLO model. To run it just run ```python3 train.py```
- The test.py is used to test the model on the test1 and test2 videos. To test the video srun ```python3 test.py```. It will create an out.mp4 folder with the result.
- To change the test videos for testing, open the test.py file and change the path in the ```VideoCapture()``` function to your desired path.

#### Model Performance
![WhatsApp Image 2024-04-20 at 15 24 06_9a9b4eff](https://github.com/omkarjois/TDL_paper/assets/88605020/5d65b424-a161-4dc3-abf3-e06a397b9cad)

#### Accuracy Comparison
![image](https://github.com/omkarjois/TDL_paper/assets/88605020/af9bf4c7-94a4-4ed9-9718-6c8c13254938)


### Models
- This folder has the codes to create the augmented data with Gen AI.
- to run the detection model run ```python3 main.py```. Change the prompts list and the number of duplicates to choose the number of variants and type of variants you want. The paths of teh source and destination of the labels can also be changed according to your needs. 
