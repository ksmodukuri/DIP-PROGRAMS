Name : Sahil Gawande
2016bec006
 Title: Histogram plot.

import numpy as np
import cv2
from matplotlib import pyplot as plt
img=cv2.imread('C:/Users/COMPLAB_29/lena_color.jpg',0)
plt.subplot(431)
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.title('lena')

count=np.zeros(256)
for i in img:
    for j in i:
        count[j]=count[j]+1        
plt.subplot(432)
plt.plot(count)
plt.title('derived')

hist=cv2.calcHist([img],[0],None,[256],[0,256])
plt.subplot(433)
plt.plot(hist)
plt.title('formula')

#checker board
img2=cv2.imread('C:/Users/COMPLAB_29/board.png',0)
plt.subplot(434)
plt.imshow(cv2.cvtColor(img2, cv2.COLOR_BGR2RGB))
plt.title('board')

count1=np.zeros(256)
for i in img2:
    for j in i:
        count1[j]=count1[j]+1
plt.subplot(435)
plt.plot(count1)
plt.title('derived')

hist1=cv2.calcHist([img2],[0],None,[256],[0,256])
plt.subplot(436)
plt.plot(hist1)
plt.title('formula')

#black and white
img3=cv2.imread('C:/Users/COMPLAB_29/blackwhite.png',0)
plt.subplot(437)
plt.imshow(cv2.cvtColor(img3, cv2.COLOR_BGR2RGB))
plt.title('blackandwhite')

count2=np.zeros(256)
for i in img3:
    for j in i:
        count2[j]=count2[j]+1
plt.subplot(438)
plt.plot(count2)
plt.title('derived')

hist2=cv2.calcHist([img3],[0],None,[256],[0,256])
plt.subplot(439)
plt.plot(hist2)
plt.title('formula')

#rotate
img4 = np.rot90(img)
plt.subplot(4,3,10)
plt.imshow(cv2.cvtColor(img4, cv2.COLOR_BGR2RGB))
plt.title('lena90rot')

count3=np.zeros(256)
for i in img4:
    for j in i:
        count3[j]=count3[j]+1
plt.subplot(4,3,11)
plt.plot(count3)
plt.title('derived')

hist3=cv2.calcHist([img4],[0],None,[256],[0,256])
plt.subplot(4,3,12)
plt.plot(hist3)
plt.title('formula')