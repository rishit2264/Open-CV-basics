import cv2 as cv
import numpy as np

img = cv.imread(r"C:\Users\rishi\Pictures\Screenshot 2024-12-09 191159.png")   #it reads the image by path

cv.imshow('me',img)  #it opens the image in a new window by the name me

#translation
def translate(img,x,y):
    transMat = np.float32([[1,0,x],[0,1,y]])   #it is a translation matrix where x and y are the pixels
    dimensions = (img.shape[1],img.shape[0])
    return cv.warpAffine(img,transMat,dimensions)

#-x --> shift left
#-y --> shift up
#x --> shift right
#y --> shift down
translated = translate(img,100,100)
cv.imshow("translated",translated)



#rotation:
def rotation(img,angle,rotPoint = None):
    (height,width) = img.shape[:2]

    if rotPoint is None:
        rotPoint =(width//2,height//2)
    
    rotMat = cv.getRotationMatrix2D(rotPoint,angle,1.0)
    dimensions = (width,height)

    return cv.warpAffine(img,rotMat,dimensions)

rotated = rotation(img,45)
cv.imshow("rotated",rotated)



#flip:
flip = cv.flip(img,0)
cv.imshow("flip",flip)


cv.waitKey(0)