import cv2 as cv

img = cv.imread(r"C:\Users\rishi\Pictures\Screenshot 2024-12-09 191159.png")   #it reads the image by path

cv.imshow('me',img)  #it opens the image in a new window by the name me

#1.converting img to grayscale
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow("gray",gray)

#2.converting img to blur
blur = cv.GaussianBlur(img,(7,7),cv.BORDER_DEFAULT)
cv.imshow("blurred me",blur)

#3.edge cascade(gives edges of img in black n white)
canny = cv.Canny(img,125,175)
cv.imshow("canny edges me",canny)

#4.dilating the image  (works on edges mostly)
dilating  = cv.dilate(canny, (7,7),iterations=3)
cv.imshow("dilated me",dilating)

#5.eroding  (gives img before dilating back basically gives cascaded img)
eroded = cv.erode(dilating,(7,7),iterations=3)
cv.imshow("eroded me",eroded)

#6.resizing
resized = cv.resize(img,(500,500))
cv.imshow("resized img",resized)

#7.cropping
cropped = img[50:200,200:400]
cv.imshow("cropped me",cropped)

cv.waitKey(0)
