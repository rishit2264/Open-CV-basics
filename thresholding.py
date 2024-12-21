import cv2 as cv

img = cv.imread(r"C:\Users\rishi\Pictures\Screenshot 2024-12-09 191159.png")   #it reads the image by path

cv.imshow('me',img) 

grey = cv.cvtColor(img,cv.COLOR_BGR2GRAY)

#simple thresholding
threshold,thresh = cv.threshold(grey,150,255,cv.THRESH_BINARY)
cv.imshow("thresholded img",thresh)

threshold,thresh_inv = cv.threshold(grey,150,255,cv.THRESH_BINARY_INV)
cv.imshow("thresholded_inv img",thresh_inv)

#adaptive thresholding:
adaptive_thresh = cv.adaptiveThreshold(grey,255,cv.ADAPTIVE_THRESH_MEAN_C,cv.THRESH_BINARY,11,3)  #here adaptive thresholding adapts thresholding itself in this case takes mean(can also do it by gaussian method) of surrounding pixels.11 here is kernel size.3 here is the amount we subtract from the mean.
cv.imshow("adaptive thresh",adaptive_thresh)

cv.waitKey(0)