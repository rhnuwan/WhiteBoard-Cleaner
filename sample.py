import cv2
import numpy as np
import Take_Image as t
import color as col

# img = t.take_image()
img = cv2.imread('image01_r.jpg')

gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)	#Gray

edges = cv2.Canny(gray,50,150,apertureSize = 3)	#Edges

mask,res = col.setColor(img,'red')

img_mask = cv2.bitwise_and(gray, gray, mask = mask) # Gray with Mask
ret, thresh = cv2.threshold(img_mask, 60, 255, cv2.THRESH_TOZERO)
im2, contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
cv2.drawContours(img, contours, -1, (0,255,255), 1)

cv2.imshow('Image',img)
cv2.waitKey(0)

