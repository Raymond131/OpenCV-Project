import cv2

webCam = cv2.VideoCapture(1,cv2.CAP_DSHOW)
laptopCam = cv2.VideoCapture(0, cv2.CAP_DSHOW)

while(laptopCam.isOpened() and webCam.isOpened()):
    ret, frame = laptopCam.read()
    _,   webFrame = webCam.read()
    if ret == True:
        cv2.imshow('laptop',frame)
        cv2.imshow('webCam', webFrame)
        k = cv2.waitKey(1)
        # 113 is ASCII code for q key
        if k == 113:
            break
    else:
        break

# Release the objects
laptopCam.release()
cv2.destroyAllWindows()