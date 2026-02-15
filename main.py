import cv2
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
# Read the image and convert it to grayscale
img = cv2.imread('image5.jpg')#upload images in the file and give their name here
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#for detecting faces
faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

# for drawing rectangles
for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)

# for showing
cv2.imshow('Detected Faces', img)
cv2.waitKey(0)
cv2.destroyAllWindows()