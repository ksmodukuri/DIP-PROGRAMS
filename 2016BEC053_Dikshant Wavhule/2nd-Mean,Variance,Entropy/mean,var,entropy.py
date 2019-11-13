import cv2
import numpy as np
from matplotlib import pyplot as plt
img= cv2.imread('lena.png',0)
plt.imshow(img,cmap='gray')

def img_mean(img):
    sum=0
    for i in img:
        for j in i:	
            for k in j:
                sum=sum + k
    return sum/(512*512*3)
img_mean(img)

def img_var(img):
    sum=0
    m = img_mean(img)
    for i in img:
        for j in i:
            for k in j:
                d = k - m 
                sum =sum + d*d
    return sum/(512*512*3)
img_var(img)

def img_en(img):
    sum=0
    for i in img:
        for j in i:
            for k in j:
                sum=sum + k*k
    return sum
img_en(img)


def entropy(img):
    intensity = np.zeros(256) 
    t1 = img[:,:,0]
    for i in t1:
        for j in i:
            intensity[j] += 1       
    
    for i in range(len(intensity)):
        intensity[i] = intensity[i]/(512*512)
    
    for i in range(len(intensity)):
        if intensity[i] == 0:
            i+=1
        else:
            intensity[i] = intensity[i]*(np.log2(intensity[i]))

    return -np.sum(intensity)       
entropy(img)