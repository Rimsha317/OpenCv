##import numpy as np
##import scipy.ndimage as sp
##import os
##
###setting directory
##
##os.chdir(path=r"C:\Users\user\Desktop\images")
##
##
##print(os.getcwd())
##
###Read Butterfly Image
##butterfly = sp.imread(fname='download.jpg', flatten=True)
##print('B&W Butterfly image shape is: ',butterfly.shape)
##print(butterfly)



import cv2


image=cv2.imread("download.jpg",0)


cv2.imshow("....",image);

cv2.waitKey(0);
cv2.destroyAllWindows();

print(".....")
