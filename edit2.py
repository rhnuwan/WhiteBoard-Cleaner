import cv2
import numpy as np

img = cv2.imread('image01_r.jpg')

gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

blurred = cv2.GaussianBlur(gray, (5,5),0)

t, thresh = cv2.threshold(blurred,127,255,cv2.THRESH_BINARY)
# cv2.imshow('Threshold', thresh)

T, threshInc = cv2.threshold(blurred, 127,255, cv2.THRESH_BINARY_INV)
# cv2.imshow('Inver', threshInc)

mask = cv2.bitwise_not(gray,thresh)
thre = cv2.adaptiveThreshold(blurred,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY_INV,11,4)
cv2.imshow('sad',thre)
rt,th = cv2.threshold(mask,127,255,cv2.THRESH_BINARY)
im2, contours, hierarchy = cv2.findContours(thre, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(mask, contours, -1, (0,255,255), 1)
cv2.imshow('New',mask)



cv2.waitKey(0)