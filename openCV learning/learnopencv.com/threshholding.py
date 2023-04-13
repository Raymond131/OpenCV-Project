import numpy as np
import cv2 as cv


image = cv.imread('data/blackHollowCircle.jpg')
th, im_th = cv.threshold(image, 200, 255, cv.THRESH_BINARY_INV)
cv.imshow('thresh',im_th)
im_floodfill = im_th.copy()
h, w = im_th.shape[:2]
mask = np.zeros((h+2, w+2), np.uint8)
cv.floodFill(im_floodfill, mask, (0,0), (255,255,255))

cv.imshow('Full Mask', im_floodfill)
cv.waitKey(0)

cv.imwrite('filled_circle_200_big.png', im_floodfill)