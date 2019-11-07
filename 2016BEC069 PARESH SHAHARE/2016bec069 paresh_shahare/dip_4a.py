import cv2
import matplotlib.pyplot as plt

img = cv2.imread('lena5.png')
im=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
h=[]
for i in range(256):
    h.append(0)
for i in range(256):
    for j in range(256):
        k=im[i][j]
        h[k]=h[k]+1
plt.hist(im.ravel(),256,[0,256])
plt.show()