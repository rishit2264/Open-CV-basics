import cv2 as cv
import numpy as np

img = cv.imread(r"C:\Users\rishi\Pictures\Screenshot 2024-12-09 191159.png")   #it reads the image by path

cv.imshow('me',img)  #it opens the image in a new window by the name me

blank = np.zeros(img.shape,dtype = 'uint8')
cv.imshow('Blank',blank)

gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow("gray",gray)

# blur = cv.GaussianBlur(img,(7,7),cv.BORDER_DEFAULT)
# cv.imshow("blurred me",blur)

# canny = cv.Canny(blur,125,175)
# cv.imshow("canny edges me",canny)

ret,thresh = cv.threshold(gray,125,255,cv.THRESH_BINARY)    #here 125 pixel value will turn black and 255 will turn to white and we are converting image to binary
cv.imshow("threshold",thresh)

contours ,hierarchies = cv.findContours(thresh,cv.RETR_LIST,cv.CHAIN_APPROX_SIMPLE)#here in this function we retr_list give all contour lines if it was retr_external it would have given only the external contours ,next chain approx none give all of the contours but chain approx simple will only give for a line the two points connection it
print(f'{len(contours)}  contours found')

cv.drawContours(blank,contours,-1,(0,0,255),1)
cv.imshow("contours drawn",blank)


cv.waitKey(0)