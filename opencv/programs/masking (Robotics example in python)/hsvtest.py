#See this example: https://stackoverflow.com/questions/57198052/why-does-the-color-conversion-from-rgb-to-hsv-produce-corrupt-images
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
b, g, r = cv2.split(img)
cv2.imshow("blue", b)
cv2.imshow("green", g)
cv2.imshow("red", r)
cv2.waitKey(0)