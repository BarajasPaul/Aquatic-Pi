import numpy as np
import cv2

print cv2.__version__
cap = cv2.VideoCapture(0)
print "CAp Saved" 

fourcc = cv2.cv.CV_FOURCC('M','J','P','G')
# Define the codec and create VideoWriter object
out = cv2.VideoWriter('output.avi',fourcc, 20.0,(640,480))
while(cap.isOpened()):
    ret, frame = cap.read()
    if ret==True:
        out.write(frame)
        a = raw_input()

        if a == 'a' :
            break
    else:
        break
cap.release()
out.release()
