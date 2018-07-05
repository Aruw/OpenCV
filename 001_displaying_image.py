import numpy as np
import cv2

img = cv2.imread('img.jpg', cv2.IMREAD_GRAYSCALE)

cv2.imshow('Image', img)
cv2.waitKey(0) #waits for specified milliseconds for any keyboard event. If you press any key in that time, the program continues.
cv2.destroyAllWindows() #simply destroys all the windows we created. If you want to destroy any specific window, use the function cv2.destroyWindow() where you pass the exact window name as the argument.
