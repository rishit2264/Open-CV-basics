import cv2 as cv

img = cv.imread(r"C:\Users\rishi\Pictures\Screenshot 2024-12-09 191159.png")   #it reads the image by path
cv.imshow('me',img) 


#rescaling the frame fxn:

def rescale(frame,scale= 0.75):   #our function takes in the image frame and resizes its dimensions
    # works on photos,videos and live videos
    width = int(frame.shape[1]*scale)
    height = int(frame.shape[0]*scale)

    dimensions = (width,height)  #creates a tuple of width and length

    return cv.resize(frame,dimensions,interpolation=cv.INTER_AREA)  #resizes the frame



def changeRes(width,height):
    # works only on live videos
    capture.set(3,width)
    capture.set(4,height)




rescaled_img = rescale(img)

cv.imshow('me2',rescaled_img)  #it opens the image in a new window by the name me2 with rescaled image



#reading videos:

capture = cv.VideoCapture(r"C:\Users\rishi\Videos\Screen Recording 2024-09-22 032109.mp4")  #captures the video

while True:
    isTrue ,frame = capture.read()    #returns a boolean whether video is  captured successfully or not and the frame

    frame_resized = rescale(frame)

    cv.imshow("video",frame)  #it opens the video under name of window video
    cv.imshow("resized_video",frame_resized)  #shows a resized video

    if cv.waitKey(20) & 0xFF == ord('d'):   #breaks the loop after some amount of time/ basically whend is pred=ssed break out of loop
        break

capture.release()  
cv.destroyAllWindows()