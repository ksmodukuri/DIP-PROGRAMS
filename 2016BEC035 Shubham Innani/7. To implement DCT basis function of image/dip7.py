## Program to find DCT basis function
import cv2
import numpy as np
from matplotlib import pyplot as plt
from scipy.fftpack import dct, idct
from math import cos

img = cv2.imread('lena.png',0)
cv2.imwrite('input.png',img)
plt.imshow(img, cmap='gray')
plt.title('Input Image')
a = np.zeros([512,512])


N = 4
def alp(n):
    if n  == 0:
        return np.sqrt(1/N)
    else:
        return np.sqrt(2/N)
    
    
F = np.zeros([N,N,N,N])

for k in range(N):
    for l in range(N):
        for m in range(N):
            for n in range(N):
                F[k][l][m][n] = np.sum(alp(k)*alp(l)*(cos(((2*m+1)*3.14*k)/(2*N)))*(cos(((2*n+1)*3.14*l)/(2*N))))
                
count=1          
for k in range(N):
    for l in range(N):
        plt.subplot(N,N,count)
        plt.imshow(F[k][l], cmap ='gray')
        count = count + 1


for i in range(64):
    for j in range(64):
        patch_img = img[i*8:i*8+8, j*8:j*8+8]
        patch_dct = dct(dct(patch_img.T, norm = 'ortho').T, norm = 'ortho')
        
        patch_dct2 = np.zeros([8, 8])
        patch_dct2 = patch_dct
        for m in range(8):
            for n in range(8):
                if m>= 4 or n>=4:
                    patch_dct2[m][n] = 0
                
        patch_idct = idct(idct(patch_dct2.T, norm = 'ortho').T, norm = 'ortho')
        
        a[i*8:i*8+8, j*8:j*8+8] = patch_idct
         
cv2.imwrite('output.png',a)
plt.imshow(a,cmap='gray')

psnr =10*np.log10((255*255)) - 10*np.log10((1/(512*512))*(np.sum((img-a)**2)))
