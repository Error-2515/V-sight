import cv2
import os

# Load the pre-trained face detection model
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# OpenCV font settings
font = cv2.FONT_HERSHEY_SIMPLEX
font_scale = 1
font_thickness = 2

class Camera:
    def __init__(self):
        self.vid = cv2.VideoCapture(0)

    def get_frame(self):
        ret, frame = self.vid.read()
        return frame

    def release_camera(self):
        self.vid.release()
        
    # Function to load labels from a folder
    def load_labels_from_folder(self, folder_path):
        labels = []
        for label in os.listdir(folder_path):
            labels.append(os.path.splitext(label)[0])
        return labels

    # Function for facial recognition with labels
    def recognize_faces(self, image, labels):
        if len(image.shape) == 2:  # If image is grayscale, convert to BGR
            image = cv2.cvtColor(image, cv2.COLOR_GRAY2BGR)
        image=cv2.flip(image,1)
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5, minSize=(30, 30))

        for i, (x, y, w, h) in enumerate(faces):
            face_roi = gray[y:y + h, x:x + w]

            # Draw rectangle around the face
            cv2.rectangle(image, (x, y), (x + w, y + h), (255, 0, 0), 2)

            # Add label to the detected face
            if i < len(labels):
                label = labels[i]
                cv2.putText(image, label, (x, y - 10), font, font_scale, (255, 0, 0), font_thickness)

        return image
