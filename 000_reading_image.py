import numpy as np
import cv2

#Load an color image in grayscale
img = cv2.imread('img.jpg', cv2.IMREAD_GRAYSCALE)

#cv2.IMREAD_COLOR : Loads a color image. Any transparency of image will be neglected. It is the default flag.
#cv2.IMREAD_GRAYSCALE : Loads image in grayscale mode
#cv2.IMREAD_UNCHANGED : Loads image as such including alpha channel
#Instead of these three flags, you can simply pass integers 1, 0 or -1 respectively.

if img == None:
    print('Invalid path...')
