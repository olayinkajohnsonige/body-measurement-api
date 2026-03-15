from ultralytics import YOLO

def get_person_anchor(first_frame_path):
    
    model = YOLO("yolo11n.pt") 

    
    results = model(first_frame_path, classes=[0]) 

    if len(results[0].boxes) > 0:
        
        # Box format is [x1, y1, x2, y2]
        box = results[0].boxes.xyxy[0].cpu().numpy()
        
        # 4. Calculate the center point of the person
        center_x = (box[0] + box[2]) / 2
        center_y = (box[1] + box[3]) / 2
        
        return [center_x, center_y]
    
    return None