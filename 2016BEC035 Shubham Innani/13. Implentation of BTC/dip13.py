import numpy as np
import cv2
from matplotlib import pyplot as plt

img= cv2.imread('lena.png',0)
plt.imshow(img,cmap='gray')
cv2.imwrite('lena.png',img)
bs=8
A=np.array(np.zeros([bs,bs]))
w=int(512/bs)
B=np.array(np.zeros([w*bs,w*bs]))

for i in range(0,w):
    for j in range(0,w):
        q=0
        patch_img = img[i*bs:i*bs+bs, j*bs:j*bs+bs]
        mean = np.mean(patch_img)
        sd = np.std(patch_img)
        for m in range(bs):
            for n in range(bs):
                if(patch_img[m][n]>mean):
                    A[m][n] = 1
                    q=q+1
                else:
                    A[m][n] = 0
        if(q==0):
            a = mean
            b = mean
        else:
            a = mean - (sd*(np.sqrt(q/((bs**2)-q))))
            b = mean + (sd*(np.sqrt(((bs**2)-q)/q)))
        for m in range(bs):
            for n in range(bs):
                if(A[m][n]==0):
                    B[i*bs+m, j*bs+n] = a                 
                else:
                    B[i*bs+m, j*bs+n] = b                               
plt.imshow(B, cmap='gray')
plt.title('BTC with Block Size=4')
plt.xlabel('Pixel')
plt.ylabel('Pixel')
cv2.imwrite('ob_8.png',B)
