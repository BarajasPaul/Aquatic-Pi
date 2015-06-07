import cv2
import time
def diffImg(t0, t1, t2):
  d1 = cv2.absdiff(t2, t1)
  d2 = cv2.absdiff(t1, t0)
  return cv2.bitwise_and(d1, d2)

cam = cv2.VideoCapture(1)

winName = "Movement Indicator"
cv2.namedWindow(winName, cv2.CV_WINDOW_AUTOSIZE)

# Read three images first:
t_minus = cv2.cvtColor(cam.read()[1], cv2.COLOR_RGB2GRAY)
t = cv2.cvtColor(cam.read()[1], cv2.COLOR_RGB2GRAY)
t_plus = cv2.cvtColor(cam.read()[1], cv2.COLOR_RGB2GRAY)
iterador=0
while True:
    # Read next image
    t_minus = t
    t = t_plus
    t_pluscolor=cam.read()[1]
    t_plus = cv2.cvtColor(t_pluscolor, cv2.COLOR_RGB2GRAY)
    result=diffImg(t_minus, t, t_plus)

    #result=cv2.bitwise_and(result,t_pluscolor)
    ret,thresh1 = cv2.threshold(result,10,255,cv2.THRESH_BINARY)
    #cv2.imshow( winName, thresh1)
    thresh2=cv2.pyrDown(cv2.pyrDown(cv2.pyrDown(thresh1)))
    y= thresh2.shape[0]
    x= thresh2.shape[1]
    ix=0
    iy=0
    contadorpixwhite=0
    while iy<y:
        ix=0
        while ix<x:
            #print str(ix)+" "+str(x)+"x"+" "+str(iy)+" "+str(y)+"y"
            pixel= thresh1[iy,ix]
            #print "pixel"+str(pixel)
            if pixel != 0:
                contadorpixwhite=contadorpixwhite+1
            ix=ix+1
            #time.sleep(.01)
        iy=iy+1

    print "pixeles = "+str(contadorpixwhite)
    if contadorpixwhite>300:
        cv2.imwrite("movimiento"+str(iterador)+".png",t_pluscolor) 
        iterador=iterador+1
    cv2.imshow( winName, thresh2)
    key = cv2.waitKey(10)
    if key == 27:
        cv2.destroyWindow(winName)
        break
print "Goodbye"

