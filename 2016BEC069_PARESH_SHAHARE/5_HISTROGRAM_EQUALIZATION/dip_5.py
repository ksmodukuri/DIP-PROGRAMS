import cv2
import numpy as np
from matplotlib import pyplot as plt
img = cv2.imread('pout.jfif',0)
cv2.imshow('orignal image',img)
z = np.zeros(256)
c = np.zeros(256)
z = cv2.calcHist([img], [0], None,[256], [0,256]) 
for i in range (256): 
    c[i] = z[i]/(img.shape[0]*img.shape[1])   
for i in range (255):
    c[i] = c[i] + c[i-1]
plt.subplot(2,1,2)
plt.plot(c)
plt.title('CDF')
plt.show()
c = c*255
c = np.round_(c)
c=c.astype(np.uint8) # converted to int
for i in range(img.shape[0]):
    for j in range(img.shape[1]):
        g=img[i,j]
        img[i,j]=c[g]
cv2.imshow('HistogramEqua',img)
eq=cv2.equalizeHist(img)
cv2.imshow('With command Histogram Equa',eq)
cv2.waitKey()
