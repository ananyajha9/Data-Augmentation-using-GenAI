from ultralytics import YOLO

model = YOLO("yolov8n.pt")


if __name__ == '__main__': 
    model.train(data="data.yaml", epochs=30, device=0, batch = 8) 
