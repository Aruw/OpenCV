import numpy as np
import cv2

img = cv2.imread('img.jpg', cv2.IMREAD_GRAYSCALE)

cv2.imshow('Minha foto', img)
cv2.waitKey(0)
cv2.imwrite('newImg.jpg', img) #salva a imagem no diretorio corrente
cv2.destroyAllWindows()
