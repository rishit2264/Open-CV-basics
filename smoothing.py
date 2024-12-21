import cv2 as cv

img = cv.imread(r"C:\Users\rishi\Pictures\Screenshot 2024-12-09 191159.png")   #it reads the image by path

cv.imshow('me',img)  #it opens the image in a new window by the name me

#averaging:
average = cv.blur(img,(3,3))
cv.imshow("blurrede by avg",average)  #takes in the kernel size ,makes a kernel each pixel  and takes the average intensity of all pixel intensity and thus we get intensity for each  pixel 

#gaussian blur:
gauss = cv.GaussianBlur(img,(3,3),0)  # same as average blur but weights are given to pixels for intensity
cv.imshow("gaussian blur",gauss)

#median blur:
median = cv.medianBlur(img,3)  #takes the median of pixels rather than average of  the intensity
cv.imshow("median blur",median) 

#bilateral blur:
bilateral = cv.bilateralFilter(img, 5 ,15,15)  #here it keeps in check the edges of the image ,5 is the radius and 15's are basically the sigma colour(as value increases no of colors influincing increases) and sigmaSpace(value increase = no of pixels influencing increases)

cv.waitKey(0)