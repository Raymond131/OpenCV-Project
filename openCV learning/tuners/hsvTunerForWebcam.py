import cv2
import numpy as np
import threading
def nothing(x):
    pass
# Create a window
cv2.namedWindow('image')

# Create trackbars for color change
# Hue is from 0-179 for Opencv
cv2.createTrackbar('HMin', 'image', 0, 179, nothing)
cv2.createTrackbar('SMin', 'image', 0, 255, nothing)
cv2.createTrackbar('VMin', 'image', 0, 255, nothing)
cv2.createTrackbar('HMax', 'image', 0, 179, nothing)
cv2.createTrackbar('SMax', 'image', 0, 255, nothing)
cv2.createTrackbar('VMax', 'image', 0, 255, nothing)

# Set default value for Max HSV trackbars
cv2.setTrackbarPos('HMax', 'image', 87)
cv2.setTrackbarPos('SMax', 'image', 255)
cv2.setTrackbarPos('VMax', 'image', 255)

# as well as MIN trackbars
cv2.setTrackbarPos('HMin', 'image', 22)
cv2.setTrackbarPos('SMin', 'image', 22)
cv2.setTrackbarPos('VMin', 'image', 74)

# Initialize HSV min/max values
hMin = sMin = vMin = hMax = sMax = vMax = 0
phMin = psMin = pvMin = phMax = psMax = pvMax = 0
#define kernel size  
kernelOpen = np.ones((5,5),np.uint8)
kernelClose = np.ones((3,3),np.uint8)

# vid_capture = cv2.VideoCapture(0, cv2.CAP_DSHOW)
vid_capture = cv2.VideoCapture("http://192.168.0.189:8080/video")




while(vid_capture.isOpened()):
  # vCapture.read() methods returns a tuple, first element is a bool 
  # and the second is frame
 
  ret, frame = vid_capture.read()
  if ret == True:
    cv2.imshow('Frame',frame)
    # convert to hsv colorspace
    # Load image
    image = frame
    # cv2.resize(frame, dim, interpolation = cv2.INTER_AREA)
    # cv2.imshow('frame',frame)
    # Get current positions of all trackbars
    hMin = cv2.getTrackbarPos('HMin', 'image')
    sMin = cv2.getTrackbarPos('SMin', 'image')
    vMin = cv2.getTrackbarPos('VMin', 'image')
    hMax = cv2.getTrackbarPos('HMax', 'image')
    sMax = cv2.getTrackbarPos('SMax', 'image')
    vMax = cv2.getTrackbarPos('VMax', 'image')

    # Set minimum and maximum HSV values to display
    lower = np.array([hMin, sMin, vMin])
    upper = np.array([hMax, sMax, vMax])

    # Convert to HSV format and color threshold
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, lower, upper)
    mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernelClose)
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernelOpen)
    result = cv2.bitwise_and(image, image, mask=mask)
    mask = cv2.blur(mask,(10,10))
    _, mask = cv2.threshold(mask,100,255,cv2.THRESH_BINARY)

    # Print if there is a change in HSV value
    if((phMin != hMin) | (psMin != sMin) | (pvMin != vMin) | (phMax != hMax) | (psMax != sMax) | (pvMax != vMax) ):
        print("(hMin = %d , sMin = %d, vMin = %d), (hMax = %d , sMax = %d, vMax = %d)" % (hMin , sMin , vMin, hMax, sMax , vMax))
        phMin = hMin
        psMin = sMin
        pvMin = vMin
        phMax = hMax
        psMax = sMax
        pvMax = vMax

    # Display result image
    
    # mask = cv2.resize(mask, dim, interpolation = cv2.INTER_AREA)
    cv2.imshow('result', mask)
    
    k = cv2.waitKey(10)
    # 113 is ASCII code for q key
    if k == 113:
      break
  else:
    break

# Release the objects
vid_capture.release()
cv2.destroyAllWindows()




