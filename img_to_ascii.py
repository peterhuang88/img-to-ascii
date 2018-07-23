"""
@author: Peter Huang
"""

import numpy as np
from PIL import Image

gscale1 = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. "

gscale2 = "@%#*+=-:. "

def open_image(fileName, cols, scale):
    # open image and convert to greyscale
    image = Image.open(fileName).convert("L")
    
    # get image dimensions
    width, height = image.size[0], image.size[1]
    
    # compute tile width
    tile_width = width / float(cols)
    
    # compute tile height based on aspect ratio and scale of font
    tile_height = tile_width / scale
    
    rows = int(height / tile_height)
    
    return [image, width, height, tile_width, tile_height, rows]

def getAverageL(image):
    # convert image to np array
    img = np.array(image)
    
    # get dimensions of np array
    w,h = img.shape
    
    # flatten image and take average
    return np.average(im.reshape(w * h))

def generateASCII(image, rows, cols, tile_width, tile_height, height, width, level):
    aimg = []
    gsval = 0
    for j in range(rows):
        # calculate start and end points for y
        y1 = int(j * tile_height)
        y2 = int((j + 1) * tile_height)
        if j == rows - 1: # correct last tile if necessary
            y2 = height
        
        aimg.append("")
        
        for i in range(cols):
            # calculate start and end points for x
            x1 = int(i * tile_width)
            x2 = int((i + 1) * tile_width)
            if i == cols - 1:
                x2 = width
                
            # crop out image to extract tile into new image object
            img = image.crop((x1, y1, x2, y2))
            
            avg = int(getAverageL(img))
            
            # convert the tile to an ASCII character depending on how many levels
            if level == True:
                gsval = gscale1[int((avg * 69) / 255)]
            else:
                gsval = gscale2[int((avg * 9) / 255)]
            
            aimg[j] += gsval

def convert(fileName, cols, scale):
    # open image and get properties
    data = open_image(fileName, cols, scale)
    image = data[0]
    width, height = data[1], data[2]
    tile_width, tile_height = data[3], data[4]
    rows = data[5]
    
    # calculate average greyscale value
    average = getAverageL(image)


    