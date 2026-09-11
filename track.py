from ultralytics import YOLO
import cv2
import os

# Load YOLO11n model
model = YOLO("yolo11n.pt")

# Input and output paths
input_video = "input_videos/test_video.mp4"
output_video = "output/tracked_video.mp4"

# Create output folder
os.makedirs("output", exist_ok=True)

# Open input video
cap = cv2.VideoCapture(input_video)

if not cap.isOpened():
    print("Error: Could not open input video.")
    exit()

# Get video properties
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = cap.get(cv2.CAP_PROP_FPS)

if fps == 0:
    fps = 30

# Create output video
fourcc = cv2.VideoWriter_fourcc(*"mp4v")
out = cv2.VideoWriter(
    output_video,
    fourcc,
    fps,
    (width, height)
)

print("Starting YOLO11 object detection and tracking...")
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

    # Draw bounding boxes, labels and tracking IDs
    annotated_frame = results[0].plot()

    # Display processed frame
    cv2.imshow(
        "YOLO11 Object Detection and Tracking",
        annotated_frame
    )

    # Save processed frame
    out.write(annotated_frame)

    # Press Q to stop
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

# Release resources
cap.release()
out.release()
cv2.destroyAllWindows()

print("Tracking completed successfully!")
print(f"Result saved to: {output_video}")