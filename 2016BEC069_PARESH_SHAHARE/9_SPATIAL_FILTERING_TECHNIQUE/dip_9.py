import cv2
import numpy as np

image = cv2.imread('lena5.jpg',0)
kernel = np.ones((3,3),np.float32)/9
processed_image = cv2.filter2D(image,-1,kernel)
blur = cv2.GaussianBlur(img,(5,5),0)
median = cv2.medianBlur(img,5)
cv2.imshow('original image', image)
cv2.imshow('Guassian blur', blur)
cv2.imshow('median blur', median)
cv2.imshow('Mean Filter Processing', processed_image)
cv2.waitKey(0)
