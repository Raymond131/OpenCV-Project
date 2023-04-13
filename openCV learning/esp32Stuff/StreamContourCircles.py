import cv2
from cv2 import cvtColor 
import numpy as np
 #night tune:
#lower = np.array([18,45,74])
#upper = np.array([62,255,255])

#glass table snowmy morning

# lower = np.array([20, 30, 100])	 
# upper = np.array([67, 255, 255])

# dinner table facing kitchen.
lower = np.array([20,46,65])
upper = np.array([87,255,255])
cam = cv2.VideoCapture(0)

# countdown = cv2.imread('data/car.jpg')
# cv2.imshow("countdown",countdown)
# cv2.waitKey(3000)
# cv2.destroyWindow("countdown")


frames = 0
while True:
    result, image = cam.read()

    if result:
        

        
        
        
       



        hsv = cv2.cvtColor(image,cv2.COLOR_BGR2HSV)


        mask = cv2.inRange(hsv,lower,upper )
        

        # im_floodfill = mask.copy()
        # h, w = mask.shape[:2]
        # mask = np.zeros((h+2, w+2), np.uint8)
        # cv2.floodFill(im_floodfill,mask, (0,0), (255,255,255))
        gau = cv2.GaussianBlur(mask,(23,23),0)
        # blurred = cv2.blur(mask,(5,5))
        T, thresh = cv2.threshold(gau, 90, 255, cv2.THRESH_BINARY)
      
       
        contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
        img = cvtColor(thresh, cv2.COLOR_GRAY2BGR)
        for c in contours:
            # calculate moments for each contour
            M = cv2.moments(c)
            
            # calculate x,y coordinate of center
            if M["m00"] != 0:
                cX = int(M["m10"] / M["m00"])
                cY = int(M["m01"] / M["m00"])
                cv2.circle(img, (cX, cY), 5, (255, 255, 0), -1)
                cv2.putText(img, "centroid", (cX - 25, cY - 25),cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 0), 2)
            
                # set values as what you need in the situation
                
            
            # print(cX,cY)
            # display the image
        cv2.imshow("frame", image)
        cv2.imshow("Image", img)
        k = cv2.waitKey(10)
        if k==113:
            break
            
    else:
        print("error")
        break
# path = r"data/cam_Tennis.jpg"
# cv2.imwrite(path,image)
# cv2.destroyWindow("Frames")


   
# # Setting parameter values
# t_lower = 50  # Lower Threshold
# t_upper = 150  # Upper threshold
  
# # Applying the Canny Edge filter
# edge = cv2.Canny(image, t_lower, t_upper)
# # cv2.imshow('edge',edge)


# biEdge = cv2.Canny(mask, t_lower, t_upper)# modified from blurred
# color = cv2.cvtColor(biEdge,cv2.COLOR_GRAY2BGR)


# cv2.imshow('color',color)


cv2.destroyAllWindows()














