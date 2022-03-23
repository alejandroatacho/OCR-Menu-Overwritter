import cv2
from PIL import Image
import pytesseract
from pdf2image import convert_from_path

# converts PDF to PNG


def convert_pdf(pdf_path, save_dir, res=400):
    pages = convert_from_path(pdf_path, res)

    name_with_extension = pdf_path.rsplit('/')[-1]
    name = name_with_extension.rsplit('.')[0]

    for idx, page in enumerate(pages):
        page.save(f'{save_dir}/{name}_{idx}.png', 'PNG')


convert_pdf(
    'data/template1.pdf', 'temp')
