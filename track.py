from ultralytics import YOLO
import cv2
import os

# Load YOLO model
model = YOLO("yolov8n.pt")

# Input and output paths
input_video = "input_videos/test_video.mp4"
output_video = "output/tracked_video.mp4"

# Create output folder
os.makedirs("output", exist_ok=True)

# Open video
cap = cv2.VideoCapture(input_video)

if not cap.isOpened():
    print("Error: Could not open video.")
    exit()

# Video properties
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = cap.get(cv2.CAP_PROP_FPS)

if fps == 0:
    fps = 30

# Output video writer
fourcc = cv2.VideoWriter_fourcc(*"mp4v")
out = cv2.VideoWriter(
    output_video,
    fourcc,
    fps,
    (width, height)
)

print("Starting object detection and tracking...")
print("Press Q to stop.")

while True:
    ret, frame = cap.read()

    if not ret:
        break

    # Detect and track objects
    results = model.track(
        frame,
        persist=True,
        verbose=False
    )

    # Draw boxes, labels and tracking IDs
    annotated_frame = results[0].plot()

    # Show live detection
    cv2.imshow("YOLO Object Detection and Tracking", annotated_frame)

    # Save the processed frame
    out.write(annotated_frame)

    # Press Q to stop
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

# Release everything
cap.release()
out.release()
cv2.destroyAllWindows()

print("Tracking completed successfully!")
print(f"Result saved to: {output_video}")