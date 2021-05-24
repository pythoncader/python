import cv2
import numpy as np
path = "C:/users/mike/desktop/creative cloud files/coding/programming/python/opencv/files/"

img = cv2.imread(path+"skystonesmall.jpg")
cv2.imshow("Hello", img)
cv2.waitKey(0)

hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
H, S, V = cv2.split(hsv)
cv2.imshow("Hue", H)
cv2.waitKey(0)
cv2.imshow("Saturation", S)
cv2.waitKey(0)
cv2.imshow("Value", V)
cv2.waitKey(0)