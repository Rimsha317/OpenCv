
import numpy as np
import cv2 as cv

def nothing(x):
    print(x)
    

cv.namedWindow('image')
cv.createTrackbar('CP','image',5,400,nothing)
switch = 'color/gray'
cv.createTrackbar(switch,'image',0,1,nothing)

while ('i'):
    image =cv.imread("./opencv example/flower.jpg",)
   
    pos = cv.getTrackbarPos('CP','image')
    font = cv.FONT_HERSHEY_SIMPLEX
    cv.putText(image,str(pos),(50,150),font,4,(0,0,255),5)
    
    k = cv.waitKey(1) & 0xFF
   
    if k == 27:
        
        break
        
    
    g = cv.getTrackbarPos('G','image')
   
    
    if g == 0 :
        pass
    else:
        
        image = cv.imshow('image', image)
cv.destroyAllWindows()
