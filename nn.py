import cv2
import numpy as np
from Take_Image import take_image
from Resize import resized,setside
from wrap_image import wrap_image
import Color as col
cap = take_image()
rimg = resized(cap,600)
img = wrap_image(rimg)

cv2.imshow('Image',img)
image = setside(img,'1')
cv2.imshow('side',image)
cv2.waitKey(0)
