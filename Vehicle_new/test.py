import random
import math
from ultralytics import YOLO
import cv2

#Video path
video_path_out = 'out.mp4'.format('')

CLASSES = ['Ambulance', 'Bus', 'Car', 'Motorcycle', 'Truck']
COLORS = [(255,0,0), (255, 255, 0), (0,255,0), (0,0,255), (0,255,255)]

#Open CV preprocessing
cap = cv2.VideoCapture('C:/Users/omkar/omkar_/PES/TDL_Project/Vehicle_normal/test3.mp4')
ret, frame = cap.read()

# Writer for creating output video
H, W, _ = frame.shape
out = cv2.VideoWriter(video_path_out, cv2.VideoWriter_fourcc(*'MP4V'), int(cap.get(cv2.CAP_PROP_FPS)), (W, H))

# Import model
model_path = 'C:/Users/omkar/omkar_/PES/TDL_Project/Vehicle_new/runs/detect/train/weights/last.pt'
model = YOLO(model_path)  

#Main Loop
while ret:
    results = model(frame)[0]

    for result in results.boxes.data.tolist():
        print(result)
        x1, y1, x2, y2, score, class_id = result

        cv2.rectangle(frame, (int(x1), int(y1)), (int(x2), int(y2)), COLORS[int(class_id)], 2)

        # Display class name and score
        label = f"{CLASSES[int(class_id)]}: {round(score, 2)}"
        cv2.putText(frame, label, (int(x1), int(y1 - 10)), cv2.FONT_HERSHEY_SIMPLEX, 0.5, COLORS[int(class_id)], 2)
    
    cv2.imshow("Frame", frame)
    cv2.waitKey(1)
    out.write(frame)
    ret, frame = cap.read()

cap.release()
out.release()
cv2.destroyAllWindows()