# Object Detection and Tracking Using YOLO11

## Project Overview

This project implements **object detection and object tracking using YOLO11**.

The system can:

* Detect objects in images.
* Detect objects in video frames.
* Track detected objects across consecutive video frames.
* Display bounding boxes around detected objects.
* Display object names and confidence scores.
* Display tracking information for objects in videos.
* Save the processed image and video results.

The project is developed using **Python, Ultralytics YOLO11, and OpenCV**.

---

## Objectives

The main objectives of this project are:

* To perform object detection using a pre-trained YOLO11 model.
* To detect multiple objects in an input image.
* To detect objects in video frames.
* To track detected objects across video frames.
* To display bounding boxes and object labels.
* To display confidence scores for detected objects.
* To generate processed image and video outputs.
* To demonstrate the practical application of deep learning and computer vision.

---

## Technologies Used

* **Python**
* **YOLO11**
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
├── .gitignore
└── yolo11n.pt
```

> Note: The `venv/` folder is used locally for the Python virtual environment and is excluded from GitHub using `.gitignore`.

---

# Project Workflow

## Image Detection Workflow

```text
Input Image
     |
     v
YOLO11 Model
     |
     v
Object Detection
     |
     v
Bounding Boxes + Labels + Confidence
     |
     v
Processed Output Image
```

## Video Tracking Workflow

```text
Input Video
     |
     v
Read Video Frames
     |
     v
YOLO11 Object Detection
     |
     v
Object Tracking
     |
     v
Bounding Boxes + Labels + Tracking Information
     |
     v
Processed Output Video
```

---

# 1. Image Object Detection

The `detect_image.py` program is used to perform object detection on an input image.

The input image is stored in:

```text
input_images/test.jpg
```

The YOLO11 model processes the image and identifies objects that belong to the model's trained classes.

The detection result includes:

* Object name
* Bounding box
* Confidence score

The processed image is saved to:

```text
output/detected_test.jpg
```

### Example Detection

For the test image used during development, the detected objects included:

```text
dog
car
```

Example detection results observed during testing:

```text
Detected: dog | Confidence: 0.86
Detected: car | Confidence: 0.85
```

The exact detected objects and confidence scores may vary depending on the input image.

---

# 2. Video Object Detection and Tracking

The `track.py` program is used to perform object detection and tracking on a video.

The input video is stored in:

```text
input_videos/test_video.mp4
```

The program reads the video frame by frame.

For each frame:

1. YOLO11 detects objects.
2. The tracking system attempts to associate detected objects across consecutive frames.
3. Bounding boxes and labels are generated.
4. Tracking information is displayed.
5. The processed frame is written to the output video.

The processed video is saved to:

```text
output/tracked_video.mp4
```

---

# 3. Object Tracking

Object tracking means following detected objects across multiple frames of a video.

The tracking process attempts to maintain an identity for an object while it remains visible across consecutive frames.

For example:

```text
Frame 1 → Object → Tracking ID
Frame 2 → Same Object → Same/Associated Tracking ID
Frame 3 → Same Object → Same/Associated Tracking ID
```

Tracking performance can depend on:

* Object movement
* Lighting conditions
* Object size
* Occlusion
* Video quality
* Camera movement
* Detection confidence

Tracking IDs may change if the tracker temporarily loses an object or cannot confidently associate it with a previous detection.

---

# 4. YOLO11 Model

This project uses the **YOLO11n** model from Ultralytics.

The model is loaded using:

```python
from ultralytics import YOLO

model = YOLO("yolo11n.pt")
```

The model is used for both:

* Image object detection
* Video object detection and tracking

YOLO11n is a lightweight model suitable for demonstrating real-time-style object detection on available computer hardware.

---

# 5. Installation

## Step 1: Clone or Download the Project

Obtain the project repository and open the project folder in Visual Studio Code.

Project folder:

```text
CodeAlpha_ObjectDetectionTracking
```

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

After activation, the terminal should display:

```text
(venv)
```

---

## Step 4: Install Required Packages

Install the required dependencies using:

```powershell
pip install -r requirements.txt
```

The main packages used by this project are:

```text
ultralytics
opencv-python
lap
```

---

# 6. Running Image Detection

Make sure the virtual environment is activated.

Place the input image in:

```text
input_images/test.jpg
```

Run:

```powershell
python detect_image.py
```

The program will:

1. Load the YOLO11 model.
2. Read the input image.
3. Detect objects.
4. Generate bounding boxes and labels.
5. Display the detection result.
6. Save the processed image.

The output image will be saved as:

```text
output/detected_test.jpg
```

---

# 7. Running Video Detection and Tracking

Make sure the input video is available at:

```text
input_videos/test_video.mp4
```

Run:

```powershell
python track.py
```

The program will:

1. Load the YOLO11 model.
2. Open the input video.
3. Read the video frame by frame.
4. Detect objects.
5. Track detected objects.
6. Draw bounding boxes and labels.
7. Display tracking information.
8. Save the processed video.

The output video will be saved as:

```text
output/tracked_video.mp4
```

During processing, the video window can be closed/stopped using the **Q** key.

---

# 8. Input

## Input Image

The project uses:

```text
input_images/test.jpg
```

This image is processed using YOLO11 object detection.

## Input Video

The project uses:

```text
input_videos/test_video.mp4
```

This video is processed frame by frame for object detection and tracking.

---

# 9. Output

## Detected Image

The image detection result is saved as:

```text
output/detected_test.jpg
```

The output contains visual annotations such as:

* Bounding boxes
* Object labels
* Confidence scores

## Tracked Video

The video tracking result is saved as:

```text
output/tracked_video.mp4
```

The output video contains visual annotations generated by the YOLO11 detection and tracking process.

---

# 10. Features

The project provides the following features:

* Image object detection
* Video object detection
* Object tracking
* Bounding box visualization
* Object labels
* Confidence scores
* Tracking information
* Processed image generation
* Processed video generation
* YOLO11-based computer vision

---

# 11. Advantages

* YOLO provides fast object detection.
* YOLO11n is relatively lightweight.
* Multiple objects can be detected in the same frame.
* Object tracking can help follow objects across video frames.
* OpenCV provides video processing functionality.
* The project can be extended for different computer vision applications.

---

# 12. Limitations

* Detection depends on the classes supported by the pre-trained YOLO11 model.
* Objects that are not recognized by the trained model may not be detected correctly.
* Detection accuracy can be affected by poor lighting and image quality.
* Small or partially hidden objects can be difficult to detect.
* Tracking IDs may change when an object is temporarily lost or difficult to associate across frames.
* Processing speed depends on the available hardware.
* A custom-trained model may be required for specialized objects that are not well represented by the pre-trained model.

---

# 13. Future Enhancements

The project can be improved by:

* Training YOLO11 on a custom dataset.
* Adding a web-based interface using Streamlit.
* Supporting live webcam detection.
* Adding object counting.
* Adding vehicle counting.
* Improving tracking stability.
* Adding real-time alerts.
* Adding performance metrics.
* Deploying the system as a web application.
* Using a custom-trained model for domain-specific objects.

---

# 14. Applications

Object detection and tracking can be applied to:

* Traffic monitoring
* Vehicle tracking
* Surveillance systems
* Crowd monitoring
* Robotics
* Autonomous systems
* Sports analysis
* Industrial monitoring
* Smart transportation

---

# 15. Conclusion

This project demonstrates the practical use of **YOLO11, deep learning, and computer vision** for object detection and tracking.

The system performs object detection on images and performs object detection and tracking on video frames. The results are visualized using bounding boxes, object labels, confidence scores, and tracking information.

The project provides a foundation that can be further extended using custom datasets, live camera input, object counting, improved tracking methods, and web-based deployment.

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
