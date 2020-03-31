import numpy as np
import cv2

img = cv2.imread('C:/Users/user/Desktop/images/images.png')
imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(imgray, 127, 255,0)
contours, hierarchy  = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
print("Number of Contours  = " + str(len(contours)))
print(contours[0])

cv2.drawContours(img,contours,-1, (225,205,45), 3)

cv2.imshow('image',img)
cv2.imshow('Image GRAY', imgray)
cv2.waitKey(0)
cv2.destroyAllWindows()
