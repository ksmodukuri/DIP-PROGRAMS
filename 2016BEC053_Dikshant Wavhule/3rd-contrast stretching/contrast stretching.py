import numpy as np
import cv2
from matplotlib import pyplot as plt
img = cv2.imread('lena.png')
plt.imshow(img)
im = img[:,:,2]
for j in range(0,512):
    for k in range(0,512):
        if im[j][k]>=0 and im[j][k]<63:
            im[j][k]=0
        elif im[j][k]>=64 and im[j][k]<127:
            im[j][k]=80
        elif im[j][k]>=128 and im[j][k]<191:
            im[j][k]=160
        elif im[j][k]>=128 and im[j][k]<255:
                im[j][k]=255
    
img[:,:,0] = img[:,:,2]
img[:,:,1] = img[:,:,2]
plt.imshow(img)
print(img[:,:,2])
cv2.imwrite('lena1.png',img)


img2 = cv2.imread('pout.png')
plt.imshow(img2)
im2 = img2[:,:,1]
for j in range(0,291):
    for k in range(0,240):
        if im2[j][k]>=0 and im2[j][k]<100:
            im2[j][k] = 0.5*im2[j][k]
        elif im2[j][k]>=100 and im2[j][k]<200:
            im2[j][k] = 1.5*im2[j][k]-100
        elif im2[j][k]>=200 and im2[j][k]<255:
            im2[j][k] = im2[j][k]
img2[:,:,2] = img2[:,:,1]
img2[:,:,0] = img2[:,:,1]
plt.imshow(img2)

