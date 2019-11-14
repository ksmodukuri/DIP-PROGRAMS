DIP


import cv2
import numpy as np
from matplotlib import pyplot as plt
from scipy.fftpack import dct
import math

img = cv2.imread(r'C:\Users\DSPLAB_USER\Downloads/lena.png',0)

dct_img = dct(img)


def alpha(num,N):
    if num == 0:
        return np.sqrt(1/N)
    else:
        return np.sqrt(2/N)

N = 4
x = np.zeros([N,N,N,N])
for k in range(N):
    for l in range(N):
        for m in range(N):
            for n in range(N):
                x[k][l][m][n] =  x[k][l][m][n] + alpha(k,N)*alpha(l,N)*math.cos(((2*m+1)*3.142*k)/(2*N))*math.cos(((2*n+1)*3.142*l)/(2*N))
                
count = 1                
for i in range(N):
    for j in range(N):
        plt.subplot(N,N,count)
        plt.imshow(x[i][j],cmap = 'gray')
        count = count + 1

#%%


import cv2
import numpy as np
from matplotlib import pyplot as plt
from scipy.fftpack import dct,idct
import math

img = cv2.imread(r'C:\Users\DSPLAB_USER\Downloads/lena.png',0)


#patch_hor = []
#patch_ver = []
#dct_img = dct(img)
z = np.zeros([512,512])

for i in range(64):
    for j in range(64):
        crop_img = img[i*8:i*8+8, j*8:j*8+8]
        patch_dct = dct(crop_img)
        patch_dct1 = np.transpose(patch_dct)
        patch_dct2 = dct(patch_dct1)
        
        for m in range(8):
            for n in range(8):
                if m >= 2 or n >=2:
                    patch_dct2[m][n] = 0
        
        patch_idct = idct(patch_dct2)
        patch_idct1 = np.transpose(patch_idct)
        patch_idct2 = np.round(idct(patch_idct1)/256)
        
        z[i*8:i*8+8, j*8:j*8+8] = patch_idct2
        
#        patch_hor = np.append(patch_hor,patch_idct2,axis = 0)
#    patch_ver = np.append(patch_ver,patch_hor,axis = 1)        
#        

cv2.imwrite(r'C:\Users\DSPLAB_USER\Downloads/lena4.png',z)
cv2.imwrite(r'C:\Users\DSPLAB_USER\Downloads/lena3.png',img)

psnr = 10*np.log10((255*255)/(1/(512*512)*np.sum(z-img)*np.sum(z-img)))


