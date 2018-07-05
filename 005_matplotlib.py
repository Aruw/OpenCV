import cv2
import numpy as np
from matplotlib import pyplot as matplotlib


img = cv2.imread('img.jpg', cv2.IMREAD_GRAYSCALE)
matplotlib.imshow(img, cmap='gray', interpolation='bicubic')
matplotlib.xticks([]), matplotlib.yticks([]) #To hide tick values on X and Y axis
matplotlib.show()
