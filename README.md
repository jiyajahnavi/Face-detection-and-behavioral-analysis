# Face Detection and Behavioral Analysis using OpenCV

## Overview

This project is a **real-time face detection and behavioral analysis system** built using **Python, NumPy, and OpenCV**.
The program captures live webcam video and detects:

* Faces
* Eyes
* Smiles
* Sleep indication through eye state monitoring

It also overlays labels and status messages directly on the video stream.
This project demonstrates practical use of **Haar Cascade classifiers** and real-time video processing.

---

## How It Works

1. Webcam captures live frames.
2. Each frame is converted to grayscale.
3. Haar cascade classifiers detect:

   * Face
   * Eyes
   * Smile
4. Behavioral logic:

   * If eyes are not detected for multiple frames → Sleeping detected.
5. Status messages and bounding boxes are displayed.

---

## Technologies Used

* Python 3
* OpenCV
* NumPy

---

## Project Structure

```
project-folder/
│
├── main.py
├── requirements.txt
└── haarcascade/
    ├── haarcascade_frontalface_default.xml
    ├── haarcascade_eye.xml
    └── haarcascade_smile.xml
```

---

## Installation

### 1. Clone the repository

```
git clone https://github.com/jiyajahnavi/face-detection-and-behavioral-analysis.git
cd face-detection-and-behavioral-analysis
```

### 2. Install dependencies

```
pip install -r requirements.txt
```

### 3. Run the program

```
python main.py
```


## Usage

1. Run the script.
2. Webcam window will open.
3. The system will display:

   * Face bounding box
   * Eye detection status
   * Sleeping alert
   * Smile detection

Press **X** to exit.

---

## License

This project is open-source and available under the MIT License.

---
