import cv2

class Camera:
    def __init__(self):
        self.vid = cv2.VideoCapture(0)

    def get_frame(self):
        ret, frame = self.vid.read()
        return frame

    def release_camera(self):
        self.vid.release()
