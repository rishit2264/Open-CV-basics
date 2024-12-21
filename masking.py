import cv2 as cv
import numpy as np

img = cv.imread(r"C:\Users\rishi\Pictures\Screenshot 2024-12-09 191159.png")   #it reads the image by path

cv.imshow('me',img)  #it opens the image in a new window by the name me

blank = np.zeros(img.shape[:2],dtype="uint8")

mask = cv.circle(blank,(img.shape[1]//2,img.shape[0]//2),100,255,-1)

masked = cv.bitwise_and(img,img,mask=mask)
cv.imshow("masked img",masked)

cv.waitKey(0)