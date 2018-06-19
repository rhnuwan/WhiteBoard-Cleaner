import numpy as np
import cv2 
 
# read and downscale image
img = cv2.imread('im.jpg', cv2.IMREAD_UNCHANGED)
# threshold image
# this step is neccessary when you work with contours
ret, threshed_img = cv2.threshold(cv2.cvtColor(img, cv2.COLOR_BGR2GRAY),127, 255, cv2.THRESH_BINARY_INV)
# find contours in image
imag, contours, hier = cv2.findContours(threshed_img, cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)

x=[]
y=[]
xM =[]
yM=[]
for indx,i in enumerate(contours):
    x.append([])
    y.append([])     
    xM.append([])     
    yM.append([])     
    for j in i:
        x[indx].append(j[0][0])
        y[indx].append(j[0][1])



# cv2.imshow('i',img)
# cv2.waitKey()
# cv2.destroyAllWindows()