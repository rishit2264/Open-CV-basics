import cv2 as cv

img = cv.imread(r"C:\Users\rishi\Pictures\Screenshot 2024-12-09 191159.png")   #it reads the image by path
cv.imshow('me',img) 

gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow("gray me",gray)

haar_cascade = cv.CascadeClassifier(r'C:\Users\rishi\Desktop\opencv\haar_face.xml')

faces_rect = haar_cascade.detectMultiScale(gray,scaleFactor=1.1,minNeighbors=3)  #here faces rect is the list of rectangle detected cordinates.

print(f" no of faces = {len(faces_rect)}")

for (x,y,w,h) in faces_rect:
    cv.rectangle(img,(x,y),(x+w,y+h),(0,255,0),thickness= 3)

cv.imshow("haar faces",img)

cv.waitKey(0)