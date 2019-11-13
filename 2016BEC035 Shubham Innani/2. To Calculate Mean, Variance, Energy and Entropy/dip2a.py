import numpy as np
import cv2 

img = cv2.imread('lena.png',0)
z=np.zeros(256)
for i in img:
    for j in i:
        z[j]=z[j]+1

for i in range(256):
    z[i]=z[i]/(512*512)

p=0
for i in range(256):
    if(z[i]!=0):
        p=p - z[i]*np.log(z[i])
print('Entropy of image is '+str(p))
