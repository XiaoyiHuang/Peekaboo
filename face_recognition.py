from cv2 import *


def grab_webcam_image():
    cam = VideoCapture(0)

    if not cam.isOpened():
        raise IOError("Cannot open webcam")

    s, img = cam.read()

    while s:
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


def main():
    grab_webcam_image()


if __name__ == "__main__":
    main()
