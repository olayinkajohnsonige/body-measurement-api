import math

class MeasurementService:
    def __init__(self, user_height_cm):
        self.user_height_cm = user_height_cm

    def get_all_measurements(self, landmarks):
        # 1. THE SCALE (Pixel to CM)
        # We use the distance from the top of the head (0) to the heels (28)
        pixel_height = abs(landmarks[28].y - landmarks[0].y)
        scale = self.user_height_cm / pixel_height

        # 2. SHOULDER WIDTH
        # Straight line between Left (11) and Right (12) shoulders
        shoulders_px = math.sqrt((landmarks[12].x - landmarks[11].x)**2 + 
                                 (landmarks[12].y - landmarks[11].y)**2)
        shoulder_width = shoulders_px * scale

        # 3. CHEST WIDTH
        # The chest is usually about 10-15% of the torso length below the shoulders
        # We find the midpoint between shoulders and hips to estimate the chest line
        chest_y = landmarks[11].y + (landmarks[23].y - landmarks[11].y) * 0.25
        # For simplicity in this 2D version, we use a slightly narrower shoulder width
        chest_width = (shoulder_width * 0.95) 

        # 4. WAIST WIDTH
        # The waist is the narrowest point between the ribs and the hips
        # Landmark 23/24 are the hips. The waist is usually 2/3 down from the shoulders
        waist_width = (shoulder_width * 0.85) # Estimated based on standard body ratio

        # 5. HIP WIDTH
        # Distance between Left Hip (23) and Right Hip (24)
        hips_px = math.sqrt((landmarks[24].x - landmarks[23].x)**2 + 
                            (landmarks[24].y - landmarks[23].y)**2)
        hip_width = hips_px * scale

        # 6. CALCULATING CIRCUMFERENCES (The 3D Estimate)
        # We use the Ellipse formula (Perimeter = 2 * PI * sqrt((a^2 + b^2) / 2))
        # We assume 'depth' is roughly 70% of 'width' for an average person
        def estimate_circ(width):
            depth = width * 0.7 
            return 2 * math.pi * math.sqrt(( (width/2)**2 + (depth/2)**2 ) / 2)

        return {
            "height_cm": self.user_height_cm,
            "shoulder_width_cm": round(shoulder_width, 2),
            "chest_circumference_cm": round(estimate_circ(chest_width), 2),
            "waist_circumference_cm": round(estimate_circ(waist_width), 2),
            "hip_circumference_cm": round(estimate_circ(hip_width), 2),
            "unit": "cm"
        }