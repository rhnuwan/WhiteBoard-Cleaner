import cv2
import numpy as np

def get_sobel(img):
	gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	sobelX = cv2.Sobel(gray, cv2.CV_64F,1,0)
	sobelY = cv2.Sobel(gray,cv2.CV_64F,0,1)

	sobelX =np.uint8(np.absolute(sobelX))
	sobelY = np.uint8(np.absolute(sobelY))

	sob = cv2.bitwise_and(sobelX,sobelY)

	cv2.imshow('X',sobelX)
	cv2.imshow('Y',sobelY)
	cv2.imshow('Res',sob)
	return sob

def get_laplacian(img):
	gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	lap = cv2.Laplacian(gray,cv2.CV_64F)
	lap = np.uint8(np.absolute(lap))
	cv2.imshow('Image',lap)
	return lap

def get_canny(img):
	gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	blurred = cv2.GaussianBlur(img, (5,5),0)
	canny = cv2.Canny(blurred,30,150)
	cv2.imshow('Canny',canny)
	return canny

def get_contours(img):
	gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	canny = get_canny(img)
	_,cnt,_ = cv2.findContours(canny.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
	print("i count {} coins in this image".format(len(cnt)))

	coins = img.copy()
	# cv2.drawContours(coins,cnt, -1,(0,255,0),1)

	cv2.drawContours(coins,cnt, 0,(0,255,0),1)
	cv2.drawContours(coins,cnt, 1,(0,255,0),1)
	cv2.drawContours(coins,cnt, 2,(0,255,0),1)

	for(i,c) in enumerate(cnt):
		(x,y,w,h) = cv2.boundingRect(c)
		print("Coins #{}".format(i+1))
		coin = img[y:y+h, x:x+w]
		cv2.imshow('Coin',coin)
		mask = np.zeros(img.shape[:2],dtype = "uint8")
		((centerX, centerY), radius) = cv2.minEnclosingCircle(c)
		
		cv2.circle(mask,(int(centerX),int(centerY)),int(radius),255,-1)
		mask = mask[y:y+h, x:x+w]
		cv2.imshow('Mask Coin',cv2.bitwise_and(coin,coin,mask=mask))

	cv2.imshow('Coins',coins)
	return cnt, coins

def get_object(img): # Uncompleted
	lower = np.array([10,40,100])
	upper = np.array([170,255,255])

	blue = cv2.inRange(img, lower,upper)
	blue = cv2.GaussianBlur(blue,(5,5),0)
	canny = get_canny(img)
	cn = cv2.bitwise_and(blue,blue) #error
	_,cnts,_ = cv2.findContours(cn.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
	print(cnts)
	if len(cnts) > 0 :
		cnt = sorted(cnts,key=cv2.contourArea,reverse = True)[0]
		rect = np.int32(cv2.boxPoints(cv2.minAreaRect(cnt)))
		cv2.drawContours(img,cnts,-1,(0,255,0),1)
		cv2.imshow('I',img)
		cv2.imshow('B',cn)

img = cv2.imread('ed.jpg')
get_object(img)
cv2.waitKey(0)