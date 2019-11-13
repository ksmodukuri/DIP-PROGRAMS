import cv2
import numpy as np
from matplotlib import pyplot as plt
img= cv2.imread('lena.jpg')
img1=cv2.imread('lena.jpg')
img2=cv2.imread('lena.jpg')
img3=cv2.imread('lena.jpg')
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))   

def img_mean(img):
    sum=0
    for i in img:
        for j in i:
            for k in j:
                sum=sum + k
    return sum/(512*512*3)
img_mean(img)
imgmean=np.mean(img)
img_mean(img)
imgmean=np.mean(img)

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
imgvar=np.var(img)

def img_en(img):
    sum=0
    for i in img:
        for j in i:
            for k in j:
                sum=sum + k*k
    return sum
img_en(img)

r,g,b = img[:,:,0], img[:,:,1], img[:,:,2] 
z=np.zeros((512,512))
img1[:,:,1]=z
img1[:,:,2]=z
plt.imshow(img1)
￼z=np.zeros((512,512))
img2[:,:,0]=z
img2[:,:,2]=z
plt.imshow(img2)
r,g,b = img[:,:,0], img[:,:,1], img[:,:,2] 
z=np.zeros((512,512))
img3[:,:,0]=z
img3[:,:,1]=z
plt.imshow(img3)

￼ 
