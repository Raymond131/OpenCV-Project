import cv2
import numpy as np

# lower bound and upper bound for Green color
lower_bound = np.array([22, 25, 74])	 
upper_bound = np.array([87, 130, 255])

#define kernel size  
kernelOpen = np.ones((11,11),np.uint8)
kernelClose = np.ones((2,2),np.uint8)

vid_capture = cv2.VideoCapture(0, cv2.CAP_DSHOW)
# Obtain frame size information using get() method
frame_width = int(vid_capture.get(3))
frame_height = int(vid_capture.get(4))
# print("frame_width", frame_width, "frame_height", frame_height)
frame_size = (frame_width,frame_height)
fps = 20

while(vid_capture.isOpened()):
  # vCapture.read() methods returns a tuple, first element is a bool 
  # and the second is frame
 
  ret, frame = vid_capture.read()
  if ret == True:
    
   
    
    height, width = frame.shape[:2]
    maxRadius = int(1.5*(height/7)/2)
    minRadius = int(0.75*(height/7)/2)

    # Convert to grayscale.
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
     # convert to hsv colorspace
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, lower_bound, upper_bound)
    mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernelClose)
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernelOpen)
    # cv2.imshow("mask", mask)
    frame = mask
    # Read image.
    # Blur using 3 * 3 kernel.
    gray_blurred = cv2.blur(gray, (3, 3))

    # Apply Hough transform on the blurred image.
    detected_circles = cv2.HoughCircles(gray_blurred,
            cv2.HOUGH_GRADIENT, 1, 20, param1 = 50,
          param2 = 30, minRadius = minRadius, maxRadius = maxRadius)

    # Draw circles that are detected.
    if detected_circles is not None:

      # Convert the circle parameters a, b and r to integers.
      detected_circles = np.uint16(np.around(detected_circles))

      for pt in detected_circles[0, :]:
        a, b, r = pt[0], pt[1], pt[2]

        # Draw the circumference of the circle.
        cv2.circle(frame, (a, b), r, (0, 255, 0), 2)

        # Draw a small circle (of radius 1) to show the center.
        cv2.circle(frame, (a, b), 1, (0, 0, 255), 3)
        print('(',a,',',b,')', sep='')
        # cv2.imshow("Detected Circle", img)
        # cv2.waitKey(0)
      # cv2.imshow("Detected Circle", frame)
      # cv2.waitKey(0)

    cv2.circle(frame, (maxRadius, maxRadius ), maxRadius, (0, 0, 255), 3)
    cv2.circle(frame, (minRadius, maxRadius*2 + minRadius), minRadius, (0, 0, 255), 3)
    cv2.imshow('Frame',frame)
    
    k = cv2.waitKey(200)
    # 113 is ASCII code for q key
    if k == 113:
      break
      
  else:
    break

# Release the objects
vid_capture.release()
cv2.destroyAllWindows()