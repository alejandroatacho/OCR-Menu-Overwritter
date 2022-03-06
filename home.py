from pdf2image import convert_from_path
import pytesseract as tess
import cv2
from PIL import Image


tess.pytesseract.tesseract_cmd = 'C:\\Users\\alex_\\AppData\\Local\\Programs\\Tesseract-OCR\\tesseract.exe'

img = cv2.imread('data/1.png')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
print(tess.image_to_string(img))
cv2.imshow('Result', img)
cv2.waitKey(0)
