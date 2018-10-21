from cv2 import *
import numpy as np


def grab_webcam_image():
    cam = VideoCapture(0)

    if not cam.isOpened():
        raise IOError("Cannot open webcam")

    s, img = cam.read()

    while s:
        img = face_recognition(img)
        if not show_webcam_img(img):
            break
        s, img = cam.read()

    cam.release()


def show_webcam_img(img):
    imshow("webcam", img)
    if waitKey(1) == 27:
        destroyAllWindows()
        return False
    else:
        return True


def face_recognition(img):
    face_cascade = CascadeClassifier('haarcascade_frontalface_default.xml')
    eye_cascade = CascadeClassifier('haarcascade_eye.xml')

    if face_cascade.empty():
        raise FileNotFoundError('Failed to locate default face classifier')

    if eye_cascade.empty():
        raise FileNotFoundError('Failed to locate default eye classifier')

    gray_scale_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray_scale_img, 1.3, 5)
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)
        roi_gray_scale = gray_scale_img[y: y + h, x: x + w]
        roi_color = img[y: y + h, x: x + w]

        eyes = eye_cascade.detectMultiScale(roi_gray_scale)
        for (ex, ey, ew, eh) in eyes:
            cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 255, 255), 2)

    return img


def main():
    grab_webcam_image()


if __name__ == "__main__":
    main()
