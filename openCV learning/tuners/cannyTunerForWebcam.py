import cv2
import numpy as np

def nothing(x):
    pass
# Create a window
cv2.namedWindow('image')

# Create trackbars for color change
# Hue is from 0-179 for Opencv
cv2.createTrackbar('lower', 'image', 0, 200, nothing)
cv2.createTrackbar('upper', 'image', 0, 200, nothing)
cv2.createTrackbar('aperture', 'image', 3, 7, nothing)


# as well as MIN trackbars
cv2.setTrackbarPos('lower', 'image', 50)
cv2.setTrackbarPos('upper', 'image', 150)
cv2.setTrackbarPos('aperture', 'image', 3)


vid_capture = cv2.VideoCapture(0, cv2.CAP_DSHOW)


while(vid_capture.isOpened()):
  # vCapture.read() methods returns a tuple, first element is a bool 
  # and the second is frame
 
  ret, frame = vid_capture.read()
  if ret == True:
    #cv2.imshow('Frame',frame)
    # convert to hsv colorspace
    # Load image
    image = frame
    # Get current positions of all trackbars
    lower = cv2.getTrackbarPos('lower', 'image')
    upper = cv2.getTrackbarPos('upper', 'image')
    aperture = cv2.getTrackbarPos('aperture', 'image')
    


   

   

    
    image = cv2.Canny(frame,lower,upper, apertureSize=aperture)
    # Display result image
    cv2.imshow('image', frame)
    cv2.imshow('result',image)
    
    k = cv2.waitKey(100)
    # 113 is ASCII code for q key
    if k == 113:
      break
  else:
    break

# Release the objects
vid_capture.release()
cv2.destroyAllWindows()




