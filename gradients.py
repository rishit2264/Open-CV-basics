import cv2 as cv
import numpy as np

img = cv.imread(r"C:\Users\rishi\Pictures\Screenshot 2024-12-09 191159.png")   #it reads the image by path

cv.imshow('me',img) 

gray  = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow("gray",gray)

#laplacian :
lap = cv.Laplacian(gray,cv.CV_64F)  #here CV_64F is the d depth
lap = np.uint8(np.absolute(lap))
cv.imshow("laplacian",lap)

#sobel:(it essentialy calculates gradients in two directions)
sobelx = cv.Sobel(gray,cv.CV_64F,1,0)
sobely = cv.Sobel(gray,cv.CV_64F,0,1)
combined_sobel = cv.bitwise_or(sobelx,sobely)

cv.imshow("sobel x",sobelx)
cv.imshow("sobel y",sobely)
cv.imshow("combined img",combined_sobel)            #canny uses sobel in one of its steps/it is usually better 

cv.waitKey(0)