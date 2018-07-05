import numpy as np
import cv2

img = cv2.imread('img2.jpg',cv2.IMREAD_GRAYSCALE)
cv2.imshow('Janela de opcoes', img)
key = cv2.waitKey(0)

#If you are using a 64-bit machine, you will have to modify k = cv2.waitKey(0) line as follows : k = cv2.waitKey(0) & 0xFF
if key == 27:   #Wait for key 27 (ESC) to exit
    cv2.destroyAllWindows()
elif key == ord('s'):   #Wait for 's' key to save and exit
    cv2.imwrite('newImg.jpg', img)
    cv2.destroyAllWindows()
