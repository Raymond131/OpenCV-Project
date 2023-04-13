import cv2

vid_capture = cv2.VideoCapture(0, cv2.CAP_DSHOW)

while(vid_capture.isOpened()):
    ret, frame = vid_capture.read()
    if ret == True:
        cv2.imshow('Frame',frame)
        k = cv2.waitKey(1)
        # 113 is ASCII code for q key
        if k == 113:
            break
    else:
        break

# Release the objects
vid_capture.release()
cv2.destroyAllWindows()