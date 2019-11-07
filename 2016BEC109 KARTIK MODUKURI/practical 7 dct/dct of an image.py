import cv2
import numpy as np
from scipy.fftpack import dct,idct

img = cv2.imread(r"D:\Btech practicals\DIP\lena.png",0)

z = np.zeros([512,512])

for i in range(64):
    for j in range(64):
        small_img = img[i*8:i*8+8, j*8:j*8+8]
        small_dct = dct(small_img)
        small_dct1 = np.transpose(small_dct)
        small_dct2 = dct(small_dct1)
       
        for m in range(8):
            for n in range(8):
                if m > 4 or n > 4:
                    small_dct2[m][n] = 0
       
        small_idct = idct(small_dct2)
        small_idct1 = np.transpose(small_idct)
        small_idct2 = np.round(idct(small_idct1)/256)
       
        z[i*8:i*8+8, j*8:j*8+8] = small_idct2       

cv2.imwrite(r'D:\Btech practicals\DIP\lena_1.png',z)
cv2.imwrite(r'D:\Btech practicals\DIP\lena_2.png',img)

psnr = 10*np.log10((255*255)/(1/(512*512)*np.sum(z-img)*np.sum(z-img)))
print(psnr)