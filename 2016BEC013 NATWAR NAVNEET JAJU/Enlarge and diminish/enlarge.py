import numpy as np
import cv2
import matplotlib.pyplot as plt

img = cv2.imread(r"C:\Users\itsna\Desktop\ops\lena_256.jpg",0)
zoomed_img = np.zeros([1024,1024])
small_img = np.zeros([len(img)//2,len(img)//2])

l=0
for i in range(0,len(img),2):
    m=0
    for j in range(0,len(img),2):
        small_img[l][m] = img[i][j]
        m+=1
    l+=1


plt.subplot(221)
plt.title("original image")
plt.imshow(img,cmap='gray')
plt.subplot(222)
plt.title("diminished image")
plt.imshow(small_img,cmap='gray')

img = cv2.imread(r"C:\Users\itsna\Desktop\ops\lena_64.jpg",0)
l=0
m=0
counter = 0
k = 0
increase = np.zeros(1024)

for j in range(len(img)):
    for i in range(len(increase)):
        increase[i] = img[l][m]
        counter+=1
        if(counter==(1024//len(img))):
            m+=1
            counter = 0
        if(m==len(img)):
            for b in range(1024//len(img)):
                zoomed_img[k+b] = increase
            increase = np.zeros(1024)
            l+=1
            m=0
            k+=1024//len(img)
plt.subplot(223)
plt.title("original image")
plt.imshow(img,cmap='gray')
plt.subplot(224)
plt.title("enlarged image")
plt.imshow(zoomed_img,cmap='gray')