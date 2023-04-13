import cv2
import numpy as np

image = cv2.imread('data/car.jpg')
cv2.imshow('Original Image', image)

h,w,c = image.shape
print("Original Height and Width:", h, "x", w)
print("channels: ",c)
down_width = 300
down_height = 200
down_factor = 0.5
down_points = (int(w * down_factor), int(h * down_factor))
resized_down = cv2.resize(image, down_points, interpolation= cv2.INTER_LINEAR)


up_width = 600
up_height = 400
up_factor = 1.5
up_points = (int(w * up_factor), int(h * up_factor))
resized_up = cv2.resize(image, up_points, interpolation= cv2.INTER_LINEAR)


cv2.imshow('Resized Down by defining height and width', resized_down)
cv2.waitKey()
cv2.imshow('Resized Up image by defining height and width', resized_up)
cv2.waitKey()

cv2.destroyAllWindows()

