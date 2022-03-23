import cv2
from PIL import Image
from cv2 import BORDER_CONSTANT
import pytesseract
from matplotlib import pyplot as plt
from pdf2image import convert_from_path
import numpy as np

image_file = "data/pdf/template1.jpg"

img = Image.open(image_file)
img_read = cv2.imread(image_file)

# https://stackoverflow.com/questions/28816046/
# displaying-different-images-with-actual-size-in-matplotlib-subplot


def display(im_path):
    dpi = 80
    im_data = plt.imread(im_path)

    height, width = im_data.shape[:2]

    # What size does the figure need to be in inches to fit the image?
    figsize = width / float(dpi), height / float(dpi)

    # Create a figure of the right size with one axes that takes up the full figure
    fig = plt.figure(figsize=figsize)
    ax = fig.add_axes([0, 0, 1, 1])

    # Hide spines, ticks, etc.
    ax.axis('off')

    # Display the image.
    ax.imshow(im_data, cmap='gray')

    plt.show()


def convert_pdf(pdf_path, save_dir, res=400):
    pages = convert_from_path(pdf_path, res)

    name_with_extension = pdf_path.rsplit('/')[-1]
    name = name_with_extension.rsplit('.')[0]

    for idx, page in enumerate(pages):
        page.save(f'{save_dir}/{name}_{idx}.png', 'PNG')


convert_pdf(
    'data/template1.pdf', 'temp')

# image rotation function


def image_rotation(img):
    Q1 = input(
        "Hello do you want to rotate the image by 45, 90, 180, 270 or 360 degrees?: ")
    if Q1 == "90":
        img.rotate(90).show()
        img.rotate(90).save(r'temp/rotated_image90fix.jpg')
    elif Q1 == "45":
        img.rotate(45).show()
        img.rotate(45).save(r'temp/rotated_image45fix.jpg')
    elif Q1 == "180":
        img.rotate(180).show()
        img.rotate(180).save(r'temp/rotated_image180fix.jpg')
    elif Q1 == "270":
        img.rotate(270).show()
        img.rotate(270).save(r'temp/rotated_image270fix.jpg')
    elif Q1 == "360":
        img.rotate(360).show()
        img.rotate(360).save(r'temp/rotated_image360fix.jpg')
    else:
        print("no, this was not an option!")

# inverts RGB of images


def invert(img_read):
    inverted_image = cv2.bitwise_not(img_read)
    cv2.imwrite("temp/inverted.jpg", inverted_image)

# grayscale effect


def grayscale(img_read):
    return cv2.cvtColor(img_read, cv2.COLOR_BGR2GRAY)


gray_image = grayscale(img_read)
cv2.imwrite("temp/original_image.jpg", gray_image)

# binary changer for grayscale
thresh, im_bw = cv2.threshold(gray_image, 127, 230, cv2.THRESH_BINARY)
cv2.imwrite("temp/bw_image.jpg", im_bw)
# ______

# noise removing removes uneeded pixels


def noise_removal(img_read):
    kernel = np.ones((1, 1), np.uint8)
    image = cv2.dilate(img_read, kernel, iterations=1)
    kernel = np.ones((1, 1), np.uint8)
    image = cv2.erode(image, kernel, iterations=1)
    image = cv2.morphologyEx(image, cv2.MORPH_CLOSE, kernel)
    image = cv2.medianBlur(image, 3)
    return (image)


no_noise = noise_removal(im_bw)
cv2.imwrite("temp/no_noise.jpg", no_noise)
# _____ end of noise removal (pixel remover)

# dilation and erosion (for text with thick fonts)


def thin_font(img_read):
    image = cv2.bitwise_not(img_read)
    kernel = np.ones((2, 2), np.uint8)
    image = cv2.erode(image, kernel, iterations=1)
    image = cv2.bitwise_not(image)
    return (image)


eroded_image = thin_font(no_noise)
cv2.imwrite("temp/eroded_image.jpg", eroded_image)
# __________

# make fonts thicker


def thick_font(img_read):
    image = cv2.bitwise_not(img_read)
    kernel = np.ones((2, 2), np.uint8)
    image = cv2.dilate(image, kernel, iterations=1)
    image = cv2.bitwise_not(image)
    return (image)


dilated_image = thick_font(no_noise)
cv2.imwrite("temp/dilated_image.jpg", dilated_image)
# __________

# remove unneeded borders around the pdf file/image


def remove_borders(img_read):
    contours, heiarchy = cv2.findContours(
        img_read, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cntsSorted = sorted(contours, key=lambda x: cv2.contourArea(x))
    cnt = cntsSorted[-1]
    x, y, w, h = cv2.boundingRect(cnt)
    crop = img_read[y:y+h, x:x+w]
    return (crop)


no_borders = remove_borders(no_noise)
cv2.imwrite("temp/no_border.jpg", no_borders)
# __________________________________


def add_borders(img_read):
    Q2 = input("What kind of border color do you want? ".lower())
    if Q2 == "white":
        color = [255, 255, 255]
    elif Q2 == "black":
        color = [0, 0, 0]
    elif Q2 == "grey":
        color = [211, 211, 211]
    else:
        print("Sorry your color is not available")
    top, bottom, left, right = [150]*4
    image_with_border = cv2.copyMakeBorder(
        no_borders, top, bottom, left, right, cv2.BORDER_CONSTANT, value=color)
    cv2.imwrite("temp/image_with_border_{}.jpg".format(Q2), image_with_border)


# add_borders(img_read)
# display("temp/image_with_border.jpg")

# print(img) #shows image meta-data
grayscale(img_read)
# display("temp/dilated_image.jpg")
# image_rotation(img)
