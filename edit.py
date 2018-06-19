import cv2
import numpy as np

img = cv2.imread('ed.jpg')

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)


edg = cv2.Canny(img,100,200)

lower = np.array([10,70,100])
upper = np.array([170,255,255])

mask = cv2.inRange(hsv,lower,upper)

#red   get the orginal image and low set 10,40,60/100,255,255

ret,thresh = cv2.threshold(gray,127,255,cv2.THRESH_BINARY_INV)

res = cv2.bitwise_and(thresh,thresh,mask=mask)

_ret, contours, hierarchy = cv2.findContours(res, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE) 
cv2.drawContours(img,contours , 0, (255,255,0), 1)

cv2.imshow('Laplacian',img)


cv2.waitKey(0)