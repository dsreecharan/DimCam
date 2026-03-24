# 📏 Object Measurement using YOLOv8 and MiDaS Depth Estimation

## 🚀 Overview
This project uses **YOLOv8** for object detection and **MiDaS** for depth estimation to measure real-world object dimensions using a webcam.  
It detects objects, estimates their depth, and calculates approximate width, height, and distance in real-time.

---

## ✨ Features
- 🎯 **Real-time Object Detection** using YOLOv8x  
- 🧠 **Depth Estimation** with MiDaS (DPT-Large)  
- 📐 **Dimension Calculation** (Width, Height, Depth in cm)  
- 🖱️ **Dynamic Reference Scaling** (Click to set reference object)  
- ⚡ **Optimized Processing** for smoother performance  

---

## 🛠️ Tech Stack
- Python 3.8+
- OpenCV
- PyTorch
- Ultralytics YOLOv8
- MiDaS (Intel ISL)
- NumPy

---

## 📦 Installation

### 1. Clone the Repository
```sh
git clone https://github.com/your-username/object-measurement-yolov8-midas.git
cd object-measurement-yolov8-midas

## Required Dependencies
- OpenCV
- PyTorch
- Ultralytics YOLO
- MiDaS (Depth Estimation)
- NumPy

## Usage

### Running the Script
```sh
python object_dimensions.py
