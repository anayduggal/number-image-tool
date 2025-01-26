from PIL import Image
import numpy as np
import re

# process config.txt into colors array
def getColorsArray(config_file):
    with open(config_file, "r") as f:
        colors = np.array([i.rstrip().split(",")[1:] for i in f.readlines()]).astype(np.uint8)
        return colors


# process number.txt into string number
def readNumber(number_file, limit=None):
    with open(number_file, "r") as f:
        number = f.read()
        number = re.sub("\D", "", number)
        if limit and len(number) > limit:
            number = number[:limit]
        return number


def getImageDims(num, **kwargs):
    # get width and height arguments if entered
    width = kwargs.get("width", None)
    height = kwargs.get("height", None)

    if not(width or height):
        # neither entered, generate square
        width = height = int(np.sqrt(len(num)))
    elif width and not height:
        # find height from width and num length
        height = len(num) // width
    elif height and not width:
        # find width from height and num length
        width = len(num) // height
    
    return (width, height)


def getImageMat(width, height, number, colors):

    image_mat = []

    # assign colours to each digit, put into matrix
    for i in range(height):
        row = [colors[int(j)] for j in number[i * width : i * width + width]]
        image_mat.append(row)

    image_mat = np.array(image_mat).astype(np.uint8)

    return image_mat


def getImageFromMat(image_mat):
    return Image.fromarray(image_mat)

# function for testing
def simpleSquare():
    colors = getColorsArray("config.txt")
    number = readNumber("number.txt", 10000)
    width, height = getImageDims(number)
    image_mat = getImageMat(width, height, number, colors)
    im = getImageFromMat(image_mat)

    im.show()

