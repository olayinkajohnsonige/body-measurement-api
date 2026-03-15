from ultralytics import SAM

class SAMService:
    def __init__(self):
        # Line 1: Load the Large (l) version of SAM 2.1
        # In 2026, sam2.1 is the stable version optimized for Ultralytics.
        self.model = SAM("sam2_l.pt")

    def track_body_in_video(self, video_path, initial_bbox):
        # Line 2: Run the 'track' method. 
        # This is the "Magic" line that replaces the manual SAM 2 loop.
        results = self.model.track(
            source=video_path, 
            bboxes=[initial_bbox], 
            persist=True  # Tells the AI to 'remember' this person across frames
        )
        
        # Line 3: Prepare a list to hold the silhouettes
        all_masks = []
        for frame_result in results:
            if frame_result.masks is not None:
                # Line 4: Extract the binary mask (the white cutout)
                all_masks.append(frame_result.masks.data)
        
        return all_masks