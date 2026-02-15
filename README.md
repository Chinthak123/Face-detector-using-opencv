# Face-detector-using-opencv
Face Detection using OpenCV

This is a simple Python project that detects human faces in an image using OpenCV and Haar Cascade classifiers.

The program reads an image, converts it to grayscale, detects faces, and draws rectangles around them.

📌 Features

Uses OpenCV's pre-trained Haar Cascade model

Detects frontal human faces

Draws bounding boxes around detected faces

Displays the output image in a window

🛠 Requirements

Make sure you have Python installed, then install OpenCV:

pip install opencv-python

📂 Project Structure
project-folder/
│── main.py
│── image5.jpg   # Your input image


Place the image you want to process inside the project folder.

▶️ How It Works

The program loads the Haar Cascade face detection model

Reads the input image

Converts the image to grayscale (required for detection)

Detects faces in the image

Draws rectangles around detected faces

Displays the result

🚀 Running the Program

Update the image filename inside main.py if needed:

img = cv2.imread('image5.jpg')


Then run:

python main.py

🧠 Code Explanation

CascadeClassifier → Loads the pre-trained face detector

imread() → Reads the image

cvtColor() → Converts image to grayscale

detectMultiScale() → Detects faces

rectangle() → Draws bounding boxes

imshow() → Displays output

⚠️ Notes

Works best with clear, front-facing images

Detection accuracy depends on lighting and image quality

If no faces are detected, try a different image

📖 Learning Purpose

This project is ideal for beginners learning:

OpenCV basics

Computer vision concepts

Image processing in Python
