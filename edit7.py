import numpy as np
import cv2 

img = cv2.imread('image01_r.jpg', cv2.IMREAD_UNCHANGED)

ret, threshed_img = cv2.threshold(cv2.cvtColor(img, cv2.COLOR_BGR2GRAY),110, 255, cv2.THRESH_BINARY_INV)

imag, contours, hier = cv2.findContours(threshed_img, cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)


# cv2.drawContours(img,contours,0,(0,255,0),1)
# cnt = contours[0]
# area = cv2.contourArea(cnt)
# perimeter = cv2.arcLength(cnt,True)
# print(area)
# print(perimeter)
# epsilon = 0.1*cv2.arcLength(cnt,True)
# approx = cv2.approxPolyDP(cnt,epsilon,True)
# hull = cv2.convexHull(cnt)
# print(approx)
# print(hull)
# for each contour
for cnt in contours:
    # calculate epsilon base on contour's perimeter
    # contour's perimeter is returned by cv2.arcLength
    epsilon = 0.01 * cv2.arcLength(cnt, True)
    # get approx polygons
    approx = cv2.approxPolyDP(cnt, epsilon, True)
    print(approx)
    # draw approx polygons
    cv2.drawContours(img, [approx], -1, (0, 255, 0), 1)
 


 
cv2.imshow("contours", img)


cv2.imshow('s',img)
cv2.waitKey(0)
