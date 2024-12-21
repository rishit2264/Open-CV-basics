import cv2 as cv
import numpy as np

blank = np.zeros((500,500,3),dtype = 'uint8')
cv.imshow('Blank',blank)

#1.paint the image a certain colour:
#blank[200:300 , 300:400] = 0,255,0  #to change colour of image to green, to change to red we use 0,0,255
#cv.imshow('Green',blank)

#2.Draw a rectangle:
#cv.rectangle(blank,(0,0),(250,250),(0,255,0),thickness=cv.FILLED)  #draws a rectangle of green filled colours according to position
#cv.imshow("Rectangle",blank)

#3.draw a circle:
#cv.circle(blank,(blank.shape[1]//2,blank.shape[0]//2),40,(0,0,255),thickness =-1)     #the long bracket specifiesss center ,40 is radius
#cv.imshow("Circle",blank)

#4.draw a line:
#cv.line(blank,(100,250),(300,400),(255,255,0),thickness=3)
#cv.imshow("line",blank)

#5.writing text on an image
cv.putText(blank,"hello rishit",(255,255),cv.FONT_HERSHEY_TRIPLEX,1.0,(0,255,0),2)
cv.imshow("text",blank)




cv.waitKey(0)