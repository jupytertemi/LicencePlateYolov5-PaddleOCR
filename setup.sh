#!/bin/bash

# Define constants
VENV_DIR="openalpr-env"
MODEL_DIR="models"
YOLOV5_DIR="yolov5"

# Create necessary directories
mkdir -p $MODEL_DIR
mkdir -p $YOLOV5_DIR

# Create and activate virtual environment
if [ ! -d "$VENV_DIR" ]; then
  python3 -m venv $VENV_DIR
fi
source $VENV_DIR/bin/activate

# Upgrade pip
pip install --upgrade pip

# Install required packages
pip install paddleocr
pip install opencv-python-headless
pip install numpy
pip install paddlepaddle
pip install git+https://github.com/ultralytics/ultralytics.git

# Clone YOLOv5 repository
if [ ! -d "$YOLOV5_DIR" ]; then
  git clone https://github.com/ultralytics/yolov5.git $YOLOV5_DIR
fi

# Download YOLOv5 model
curl -L "https://github.com/ultralytics/yolov5/releases/download/v5.0/yolov5s.pt" -o $MODEL_DIR/yolov5s.pt

echo "Setup complete. Use 'source $VENV_DIR/bin/activate' to activate the virtual environment."
