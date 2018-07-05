import numpy as np
import cv2

img = cv2.imread('img.jpg',cv2.IMREAD_GRAYSCALE)

cv2.namedWindow('image', cv2.WINDOW_NORMAL) #specify whether window is resizable or not
#By default, the flag is cv2.WINDOW_AUTOSIZE. But if you specify flag to be cv2.WINDOW_NORMAL, you can resize window.
cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
