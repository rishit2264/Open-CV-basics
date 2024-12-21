import cv2 as cv
import numpy as np

blank = np.zeros((400,400),dtype = "uint8")

rectangle = cv.rectangle(blank.copy(),(30,30),(370,370),255,-1)
circle = cv.circle(blank.copy(),(200,200),200,255,-1)

cv.imshow("rectangle",rectangle)
cv.imshow("circle",circle)

#bitwise and:  (returrns only the intersecting regions)
bitwise_and = cv.bitwise_and(rectangle,circle)
cv.imshow("bitwisw and",bitwise_and)

#bitwise or:  (returns both intersecting as well as non intersecting region)
bitwise_or = cv.bitwise_or(rectangle,circle)
cv.imshow("bitwise or",bitwise_or)

#bitwise XOR:  (returns only the non intersecting region)
bitwise_XOR = cv.bitwise_xor(rectangle,circle)
cv.imshow("bitwise or",bitwise_XOR)

#bitwise not:  (returns the opposite of the img)
bitwise_not = cv.bitwise_not(rectangle)
cv.imshow("bitwise not",bitwise_not)

cv.waitKey(0)
