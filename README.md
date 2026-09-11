# Object Detection and Tracking using YOLO

## Project Overview

This project implements object detection and object tracking using the YOLO (You Only Look Once) deep learning model.

The system can detect objects in images and detect and track objects in videos. It uses the Ultralytics YOLO model and OpenCV for computer vision and video processing.

The detected objects are displayed with bounding boxes, object names, confidence scores, and tracking IDs.

---

## Objectives

The main objectives of this project are:

* To detect objects in images using YOLO.
* To detect objects in video frames.
* To track detected objects across multiple video frames.
* To display bounding boxes around detected objects.
* To display object names and confidence scores.
* To assign tracking IDs to objects in videos.
* To save the processed image and video results.

---

## Technologies Used

* **Python**
* **YOLO**
* **Ultralytics**
* **OpenCV**
* **Computer Vision**
* **Deep Learning**

---

## Software Requirements

* Python 3.x
* Visual Studio Code
* Python Virtual Environment
* Ultralytics
* OpenCV
* LAP

---

## Project Structure

```text
CodeAlpha_ObjectDetectionTracking/
│
├── input_images/
│   └── test.jpg
│
├── input_videos/
│   └── test_video.mp4
│
├── output/
│   ├── detected_test.jpg
│   └── tracked_video.mp4
│
├── detect_image.py
├── track.py
├── requirements.txt
├── README.md
└── venv/
```

---

## Project Workflow

The project follows these main steps:

```text
Input Image
     ↓
YOLO Object Detection
     ↓
Detected Objects
     ↓
Bounding Boxes + Confidence
     ↓
Output Image
```

For video:

```text
Input Video
     ↓
YOLO Object Detection
     ↓
Object Tracking
     ↓
Tracking IDs
     ↓
Bounding Boxes + Object Labels
     ↓
Output Video
```

---

# 1. Image Object Detection

The `detect_image.py` program is used to detect objects in an input image.

The input image is stored in:

```text
input_images/test.jpg
```

The YOLO model processes the image and identifies the objects present in it.

### Example Detection

The test image contains:

* Car
* Dog

The detected objects are displayed with their confidence scores.

Example:

```text
Detected: dog | Confidence: 0.86
Detected: car | Confidence: 0.85
```

The processed image is saved to:

```text
output/detected_test.jpg
```

---

# 2. Video Object Detection and Tracking

The `track.py` program is used for object detection and tracking in a video.

The input video is stored in:

```text
input_videos/test_video.mp4
```

The YOLO model detects objects in each video frame and tracks them across consecutive frames.

The tracking system can assign IDs to detected objects so that the same object can be followed while it moves through the video.

The processed video is saved to:

```text
output/tracked_video.mp4
```

---

## Tracking

Object tracking means following the same detected object across multiple frames of a video.

For example:

```text
Frame 1 → Car → ID 1
Frame 2 → Car → ID 1
Frame 3 → Car → ID 1
Frame 4 → Car → ID 1
```

The tracking ID helps identify the same object throughout the video.

---

# 3. Installation

## Step 1: Create the Project Folder

Create the project folder:

```text
CodeAlpha_ObjectDetectionTracking
```

Open the folder in Visual Studio Code.

---

## Step 2: Create a Virtual Environment

Open PowerShell inside the project folder and run:

```powershell
python -m venv venv
```

---

## Step 3: Activate the Virtual Environment

Run:

```powershell
venv\Scripts\activate
```

After activation, the terminal should show:

```text
(venv)
```

---

## Step 4: Install Required Packages

Install the required Python packages using:

```powershell
pip install -r requirements.txt
```

The main packages used in this project are:

```text
ultralytics
opencv-python
lap
```

---

# 4. Running Image Detection

Make sure the virtual environment is activated.

Run:

```powershell
python detect_image.py
```

The program will:

1. Load the YOLO model.
2. Read the input image.
3. Detect objects.
4. Display detection results.
5. Save the processed image.

The output will be saved in:

```text
output/detected_test.jpg
```

---

# 5. Running Video Detection and Tracking

Make sure the input video is available at:

```text
input_videos/test_video.mp4
```

Run:

```powershell
python track.py
```

The program will:

1. Load the YOLO model.
2. Open the input video.
3. Read the video frame by frame.
4. Detect objects.
5. Track detected objects.
6. Draw bounding boxes.
7. Display object labels.
8. Display tracking IDs.
9. Save the processed video.

The final output will be saved to:

```text
output/tracked_video.mp4
```

---

# 6. Input

The project uses:

### Input Image

```text
input_images/test.jpg
```

### Input Video

```text
input_videos/test_video.mp4
```

The image and video are used to demonstrate object detection and tracking.

---

# 7. Output

The project generates:

### Detected Image

```text
output/detected_test.jpg
```

This image contains bounding boxes and labels for detected objects.

### Tracked Video

```text
output/tracked_video.mp4
```

This video contains detected objects, bounding boxes, labels, and tracking information.

---

# 8. Features

The project provides the following features:

* Image object detection.
* Video object detection.
* Real-time-style video processing.
* Object tracking.
* Bounding box visualization.
* Object classification labels.
* Confidence scores.
* Tracking IDs.
* Processed output image.
* Processed output video.

---

# 9. Advantages

* YOLO provides fast object detection.
* The system can detect multiple objects in the same image or video.
* Object tracking helps follow objects across video frames.
* OpenCV provides efficient video processing.
* The project can be extended to different applications.

---

# 10. Applications

Object detection and tracking can be used in:

* Traffic monitoring.
* Surveillance systems.
* Smart transportation.
* Crowd monitoring.
* Vehicle tracking.
* Robotics.
* Autonomous systems.
* Sports analysis.
* Industrial monitoring.

---

# 11. Limitations

* Detection accuracy depends on the trained YOLO model.
* Objects that are not included in the model's trained classes may not be detected correctly.
* Detection performance can be affected by poor lighting, image quality, object size, and occlusion.
* Processing speed depends on the available hardware.

---

# 12. Future Enhancements

The project can be improved by:

* Training YOLO on a custom dataset.
* Adding a web-based interface.
* Supporting live camera detection.
* Adding object counting.
* Adding vehicle counting.
* Improving tracking accuracy.
* Adding real-time alerts.
* Deploying the system as a web application.

---

# 13. Conclusion

This project demonstrates object detection and tracking using the YOLO deep learning model.

The system successfully detects objects in images and performs object detection and tracking in videos. Bounding boxes, object labels, confidence scores, and tracking IDs provide useful visual information about the detected objects.

The project demonstrates the practical application of deep learning and computer vision for object detection and tracking.

---

## Author

**Savitri Kullolli**

AI & Machine Learning Student

---

## Project Type

**CodeAlpha Internship Project**

**Project:** Object Detection and Tracking

---

## License

This project is developed for educational and internship purposes.
