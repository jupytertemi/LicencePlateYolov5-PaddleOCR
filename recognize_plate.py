import os
import sys

# Ensure the script is running in a virtual environment
if not hasattr(sys, 'real_prefix') and 'VIRTUAL_ENV' not in os.environ:
    print("This script must be run within a virtual environment.")
    sys.exit(1)

import cv2
from paddleocr import PaddleOCR
from ultralytics import YOLO

def recognize_plate(image_path, confidence_threshold=0.5):
    # Load YOLOv5 model
    model = YOLO("models/yolov5su.pt")

    # Initialize PaddleOCR
    ocr = PaddleOCR(use_angle_cls=True, lang='en')

    # Check if image file exists
    if not os.path.exists(image_path):
        print(f"Error: The image file {image_path} does not exist.")
        return

    # Read image
    image = cv2.imread(image_path)
    if image is None:
        print(f"Error: Could not read image {image_path}")
        return

    # Run YOLOv5 model
    results = model(image)

    plate_found = False

    # Process results
    for result in results:
        for box in result.boxes:
            x1, y1, x2, y2 = box.xyxy[0].cpu().numpy()
            conf = box.conf[0].item()
            if conf < confidence_threshold:
                continue

            plate_found = True
            plate = image[int(y1):int(y2), int(x1):int(x2)]

            # Use PaddleOCR to recognize text
            ocr_result = ocr.ocr(plate, cls=True)
            print("OCR result:", ocr_result)

            if ocr_result and ocr_result[0]:
                for res in ocr_result[0]:
                    if len(res) > 1 and len(res[1]) > 1:
                        print(f"License Plate: {res[1][0]}, Confidence: {res[1][1]}")
                    else:
                        print(f"Unexpected OCR result format: {res}")
