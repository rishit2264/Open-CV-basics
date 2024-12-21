import cv2 as cv

#reading images:

#img = cv.imread(r"C:\Users\rishi\Pictures\Screenshot 2024-12-09 191159.png")   #it reads the image by path

#cv.imshow('me',img)  #it opens the image in a new window by the name me

#cv.waitKey(0)

#reading videos:

capture = cv.VideoCapture(r"C:\Users\rishi\Videos\Screen Recording 2024-09-22 032109.mp4")  #captures the video

while True:
    isTrue ,frame = capture.read()    #returns a boolean whether video is  captured successfully or not and the frame
    cv.imshow("video",frame)  #it opens the video under name of window video

    if cv.waitKey(20) & 0xFF == ord('d'):   #breaks the loop after some amount of time/ basically when d is pressed break out of loop
        break

capture.release()  
cv.destroyAllWindows()
