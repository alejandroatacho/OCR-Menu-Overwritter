from pdf2image import convert_from_path
import pytesseract as tess
import cv2
from PIL import Image


tess.pytesseract.tesseract_cmd = 'C:\\Users\\alex_\\AppData\\Local\\Programs\\Tesseract-OCR\\tesseract.exe'

img = cv2.imread('data/1.png')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
# print(tess.image_to_string(img))
# detect characters

# class for OCR index shower


def test(img):

    hImg, Wimg, _ = img.shape
    boxes = tess.image_to_boxes(img)
    for b in boxes.splitlines():
        # print(b)
        b = b.split(' ')
        # print(b)
        x, y, w, h = int(b[1]), int(b[2]), int(b[3]), int(b[4])
        cv2.rectangle(img, (x, hImg-y), (w, hImg-h), (0, 0, 255), 2)
        cv2.putText(img, b[0], (x, hImg-y+25),
                    cv2.FONT_HERSHEY_COMPLEX, 1, (50, 50, 255), 2)

    cv2.imshow('Result', img)
    cv2.waitKey(0)


def detecting_words(img):

    hImg, Wimg, _ = img.shape
    boxes = tess.image_to_data(img)
    # print(boxes)
    for x, b in enumerate(boxes.splitlines()):
        if x != 0:
            b = b.split()
            print(b)
            if len(b) == 12:
                x, y, w, h = int(b[6]), int(b[7]), int(b[8]), int(b[9])
                cv2.rectangle(img, (x, y), (w+x, h+y), (0, 0, 255), 2)
    cv2.imshow('Result', img)
    cv2.waitKey(0)

detecting_words(img)
