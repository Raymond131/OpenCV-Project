# TechVidvan Object detection of similar color

import cv2
import numpy as np

# Reading the image
img = cv2.imread('tennis.jpg')

# Showing the output





# convert to hsv colorspace
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# lower bound and upper bound for Green color
lower_bound = np.array([35, 55, 0])	 
upper_bound = np.array([51, 255, 255])

# find the colors within the boundaries
mask = cv2.inRange(hsv, lower_bound, upper_bound)
cv2.imshow("before", mask)

#define kernel size  
kernel = np.ones((5,5),np.uint8)

# Remove unnecessary noise from mask

mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)
mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)

cv2.imshow("mask", mask)

cv2.waitKey(0)
cv2.destroyAllWindows()