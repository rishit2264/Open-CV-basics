import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread(r"C:\Users\rishi\Pictures\Screenshot 2024-12-09 191159.png")   #it reads the image by path
cv.imshow("me",img)

blank = np.zeros(img.shape[:2],dtype = "uint8")

# gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
# cv.imshow("gray",gray)

# circle = cv.circle(blank,(blank.shape[1]//2,blank.shape[0]//2),400,(0,0,255),thickness =-1)  

# mask = cv.bitwise_and(gray,gray,mask=circle)
# cv.imshow("masked img",mask)

#grayscale histogram:
# gray_hist = cv.calcHist([gray],[0],mask,[256],[0,256])  #here gray is inlist form because hist expects a list of images ,0 is no of computation and None is the mask.[0,256] is the pixel intensity(ig)

# plt.figure()
# plt.title("grayscale histogram")
# plt.xlabel("no of bins")
# plt.ylabel("no of pixels")
# plt.plot(gray_hist)
# plt.xlim([0,256])
# plt.show()


#color histograms:

plt.figure()
plt.title("grayscale histogram")
plt.xlabel("no of bins")
plt.ylabel("no of pixels")
colors = ('b','g','r')
for i,col in enumerate(colors):
    hist = cv.calcHist([img],[i],None,[256],[0,256])
    plt.plot(hist,color = col)
    plt.xlim([0,256])
plt.show()

cv.imshow('me',img) 

