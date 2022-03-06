# Useful libraries
# [0]
from pdf2image import convert_from_path
from pytesseract import image_to_string

# [1]


def convert_pdf_to_img(pdf_file):
    """
    @desc: this function converts a PDF into Image

    @params:
        - pdf_file: the file to be converted

    @returns:
        - an interable containing image format of all the pages of the PDF
    """
    return convert_from_path(pdf_file)


def convert_image_to_text(file):
    """
    @desc: this function extracts text from image

    @params:
        - file: the image file to extract the content

    @returns:
        - the textual content of single image
    """

    text = image_to_string(file)
    return text


def get_text_from_any_pdf(pdf_file):
    """
    @desc: this function is our final system combining the previous functions

    @params:
        - file: the original PDF File

    @returns:
        - the textual content of ALL the pages
    """
    images = convert_pdf_to_img(pdf_file)
    final_text = ""
    for pg, img in enumerate(images):

        final_text += convert_image_to_text(img)
        #print("Page n°{}".format(pg))
        # print(convert_image_to_text(img))

    return final_text


# [4]
path_to_pdf = 'data/#.pdf'

# [5]
print(get_text_from_any_pdf(path_to_pdf))
