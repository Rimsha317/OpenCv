import cv2
image=cv2.imread("opencv example/flower.jpg",1)
image = cv2.arrowedLine(image,(0,25),(55,120),(147,96,54), 4) 
image = cv2.rectangle(image,(0,40),(80,80),(0,0,255),5)
image = cv2.circle(image,(191,63),(63),(0,255,0),-1)
image = cv2.line(image,(0,0),(255,255),(147,96,54), 5)
font = cv2.FONT_HERSHEY_SIMPLEX
image = cv2.putText(image,'rimsha',(65,45),font,2,(0,0,255),10,cv2.LINE_AA)
cv2.imshow("....",image)
cv2.waitKey(0)
cv2.destroyAllWindows()
