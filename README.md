# 🚗 License Plate Detection using OpenCV

This project detects a possible license plate region from a car image using basic image processing techniques in Python.

## 📌 Features
- Converts image to grayscale
- Applies Gaussian blur to reduce noise
- Detects edges using Canny edge detection
- Finds contours in the image
- Filters contours based on aspect ratio to identify plate-like regions
- Draws a bounding box around the detected plate

## 🛠️ Technologies Used
- Python
- OpenCV (cv2)

## 📂 Project Structure
├── car.jpg # Input image
├── main.py # Python script
└── README.md # Project documentation

## ▶️ How It Works
1. Load the image using OpenCV  
2. Convert it to grayscale  
3. Apply Gaussian blur  
4. Perform edge detection using Canny  
5. Find contours in the image  
6. Sort contours based on area  
7. Filter contours using:
   - Aspect ratio (2 < w/h < 6)
   - Minimum width  
8. Draw rectangle around detected plate  

## ▶️ How to Run

1. Install dependencies:
2. pip install opencv-python
3. Place your image as `car.jpg` in the same folder  
4. Run the script:
python main.py

## 📸 Output
The program will display the image with a green rectangle around the detected license plate.

## ⚠️ Limitations
- Works best with clear images
- May fail in low lighting or complex backgrounds
- Not as accurate as AI/ML-based models

## 🚀 Future Improvements
- Use Machine Learning for better accuracy
- Add real-time detection using webcam
- Improve contour filtering logic

## 👨‍💻 Author
Rajesh V 
Student Developer

---
