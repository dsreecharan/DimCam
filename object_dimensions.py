import cv2
import numpy as np
import torch
from ultralytics import YOLO

# Initialize YOLO model
yolo_model = YOLO('yolov8n.pt')  # Using smaller model for better performance

# Global variables
reference_object = None
reference_width_cm = 5.0

def detect_and_measure(frame):
    """Detect objects and measure their dimensions using YOLO"""
    global reference_object
    
    # Run YOLO detection
    results = yolo_model(frame, verbose=False)[0]
    
    # Create a copy for drawing
    output_frame = frame.copy()
    
    # Get all detections
    boxes = results.boxes
    
    if len(boxes) == 0:
        cv2.putText(output_frame, "No objects detected", (10, 30),
                   cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
        return output_frame
        
    # Process each detection
    for box in boxes:
        # Get box coordinates
        x1, y1, x2, y2 = map(int, box.xyxy[0])
        conf = float(box.conf[0])
        cls = int(box.cls[0])
        
        # Filter by confidence
        if conf < 0.3:  # Adjust confidence threshold as needed
            continue
            
        # Calculate dimensions in pixels
        width_px = x2 - x1
        height_px = y2 - y1
        
        # Draw bounding box
        if reference_object is None:
            # First detected object becomes reference
            reference_object = width_px
            color = (0, 255, 0)  # Green for reference
            label = "Reference"
        else:
            # Calculate real-world dimensions
            width_cm = (width_px * reference_width_cm) / reference_object
            height_cm = (height_px * reference_width_cm) / reference_object
            color = (255, 0, 0)  # Blue for measured objects
            label = f"{width_cm:.1f}cm x {height_cm:.1f}cm"
        
        # Draw box and label
        cv2.rectangle(output_frame, (x1, y1), (x2, y2), color, 2)
        
        # Add label background
        (label_w, label_h), _ = cv2.getTextSize(label, cv2.FONT_HERSHEY_SIMPLEX, 0.7, 2)
        cv2.rectangle(output_frame, 
                     (x1, y1 - label_h - 10), 
                     (x1 + label_w + 10, y1),
                     (255, 255, 255), 
                     -1)
        
        # Add label text
        cv2.putText(output_frame,
                    label,
                    (x1 + 5, y1 - 5),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.7,
                    (0, 0, 0),
                    2)
    
    return output_frame

def select_reference(event, x, y, flags, param):
    """Mouse callback to reset reference object"""
    global reference_object
    if event == cv2.EVENT_LBUTTONDOWN:
        reference_object = None
        print("Reference object reset. Next detected object will become reference.")

def main():
    # Initialize camera
    cap = cv2.VideoCapture(0)
    
    # Set camera properties
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)
    
    # Create window and set mouse callback
    cv2.namedWindow('Object Dimensions')
    cv2.setMouseCallback('Object Dimensions', select_reference)
    
    print("Instructions:")
    print(f"1. Place a reference object of {reference_width_cm}cm width")
    print("2. Click anywhere in the window to reset reference object")
    print("3. Press 'q' to quit")
    
    while True:
        ret, frame = cap.read()
        if not ret:
            print("Failed to grab frame")
            break
            
        # Flip frame horizontally for more intuitive interaction
        frame = cv2.flip(frame, 1)
        
        # Process frame
        processed_frame = detect_and_measure(frame)
        
        # Display result
        cv2.imshow('Object Dimensions', processed_frame)
        
        # Break loop on 'q' press
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    # Cleanup
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
