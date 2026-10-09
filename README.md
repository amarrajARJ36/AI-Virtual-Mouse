# 🖱️ AI Virtual Mouse & Gesture Controller

An AI-powered virtual mouse and gesture control system built using **OpenCV**, **MediaPipe**, **PyAutoGUI**, and **NumPy**. Control your computer's cursor, click, scroll, zoom, and adjust system volume seamlessly using hand gestures captured by your webcam!

---

## ✨ Features

- 👆 **Virtual Cursor Control**: Move your mouse cursor smoothly across the screen using your index finger.
- 🖱️ **Click Actions**:
  - **Left Click**: Pinch / gesture with 4 fingers up.
  - **Right Click**: Gesture with thumb + index finger.
- 📜 **Page Scroll**:
  - **Scroll Up**: Index finger up.
  - **Scroll Down**: Index + Middle finger up.
- 🔍 **Zoom Control**: Pinch index and thumb to zoom in/out in applications.
- 🔊 **Volume Control**: Adjust macOS output volume dynamically using finger distance measurements.
- ⚡ **Real-Time Hand Tracking**: Uses MediaPipe Hands for high-accuracy 21-landmark 3D hand position estimation.

---

## 🛠️ Prerequisites & Installation

### 1. Clone the repository
```bash
git clone https://github.com/amarrajARJ36/AI-Virtual-Mouse.git
cd AI-Virtual-Mouse
```

### 2. Create and activate a Virtual Environment
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Required Dependencies
```bash
pip install opencv-python mediapipe pyautogui numpy
```

---

## 🚀 How to Run

Navigate to the `day 11` directory and execute the main controller script:

```bash
cd "day 11"
python Main.py
```

> **Note**: Press **`q`** while focused on the webcam window to exit the application.

---

## 🖐️ Gesture Reference Guide

| Mode | Gesture | Action |
| :--- | :--- | :--- |
| **Cursor Mode** | All 5 fingers extended | Activates mouse movement mode |
| **Move Cursor** | Index finger pointing | Moves mouse pointer on screen |
| **Left Click** | Index + Middle + Ring + Pinky | Triggers Left Mouse Click |
| **Right Click** | Thumb + Index finger | Triggers Right Mouse Click |
| **Scroll Mode** | Index finger only (Up) / Index + Middle (Down) | Scrolls up / down |
| **Zoom Mode** | Thumb + Index finger pinch | Zooms in/out (`Cmd +` / `Cmd -`) |
| **Volume Mode** | Thumb + Pinky finger pinch distance | Increases / Decreases macOS system volume |

---

## 📁 Project Structure

```text
├── HandTrackingModule.py   # Reusable Hand Tracking Module using MediaPipe
├── day 11/
│   ├── Main.py             # Main Gesture Control Application
│   └── HandTrackingModule.py
├── .gitignore              # Ignored files (venv, pycache, OS files)
└── README.md               # Project documentation
```

---

## 📄 License & Credits

Developed by **[amarrajARJ36](https://github.com/amarrajARJ36)**.  
Built with Python, OpenCV, and Google MediaPipe.
