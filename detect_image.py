from ultralytics import YOLO
import cv2
import os

# Load the pretrained YOLO model
model = YOLO("yolo11n.pt")

# Input image path
image_path = "input_images/test.jpg"

# Check whether image exists
if not os.path.exists(image_path):
    print("Error: test.jpg not found in input_images folder.")
    exit()

# Run object detection
results = model(image_path, conf=0.5)

# Get the detected image with bounding boxes
annotated_image = results[0].plot()

# Create output folder
os.makedirs("output", exist_ok=True)

# Save the detected image
output_path = "output/detected_test.jpg"
cv2.imwrite(output_path, annotated_image)

# Print detected objects
print("\nObject Detection Results:")

if results[0].boxes is not None:
    for box in results[0].boxes:
        class_id = int(box.cls[0])
        confidence = float(box.conf[0])
        class_name = model.names[class_id]

        print(
            f"Detected: {class_name} "
            f"| Confidence: {confidence:.2f}"
        )

print("\nDetection completed successfully!")
print(f"Result saved to: {output_path}")