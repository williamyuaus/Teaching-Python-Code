import sys, random, argparse
import numpy as np
import math

from PIL import Image

gscale1 = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. "
gscale2 = '@%#*+=-:. '

def getAverageL(image):
    im = np.array(image)
    w,h = im.shape
    return np.average(im.reshape(w*h))

def convertImageToAscii(fileName, cols, scale, moreLevels):
    global gscale1, gscale2
    image = Image.open(fileName).convert('L')
    W, H = image.size[0], image.size[1]
    print("input image dims: %d x %d" % (W, H))

    w = W/cols
    h = w/scale
    rows = int(H/h)
    
