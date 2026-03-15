import cv2
import os

def extract_frames(video_path, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
        
    cap = cv2.VideoCapture(video_path)
    frames = [] # Create an empty list to store frames
    frame_count = 0
    
    while True:
        is_read, frame = cap.read()
        if not is_read:
            break
            
        # Save to folder (as you were doing)
        frame_name = f"{frame_count:05d}.jpg"
        save_path = os.path.join(output_folder, frame_name)
        cv2.imwrite(save_path, frame)
        
        # Add the actual image data to our list
        frames.append(frame)
        frame_count += 1
        
    cap.release()
    return frames