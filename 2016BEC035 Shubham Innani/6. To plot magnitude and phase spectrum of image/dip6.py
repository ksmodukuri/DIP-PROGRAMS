### Program to plot phase and magnitude of image
import numpy as np
import cv2
from matplotlib import pyplot as plt

img = cv2.imread('image.png',0)
plt.imshow(img,cmap='gray')
f = np.fft.fft2(img)
phase = np.angle(f)
fshift = np.fft.fftshift(f)
mag = 20*(np.log(np.abs((fshift))))
plt.imshow(mag, cmap='gray')
plt.imshow(phase,cmap='gray')

ifshift = np.fft.ifftshift(fshift)
ift=np.fft.ifft2(f)
plt.imshow(np.abs(ift), cmap='gray')

### Program to interchange Phase of two images and plot it
i=np.complex(0,1)
img1=cv2.imread('lena.png',0)
img2=cv2.imread('mandrill.png',0)
plt.imshow(img1, cmap='gray')
plt.imshow(img2,cmap='gray')

f1 = np.fft.fft2(img1)
phase1 = np.angle(f1)
fshift1 = np.fft.fftshift(f1)
mag1 = 20*(np.log(np.abs((fshift1))))
plt.imshow(mag1, cmap='gray')
plt.imshow(phase1,cmap='gray')

f2 = np.fft.fft2(img2)
phase2 = np.angle(f2)
fshift2 = np.fft.fftshift(f2)
mag2 = 20*(np.log(np.abs((fshift2))))
plt.imshow(mag2, cmap='gray')
plt.imshow(phase2,cmap='gray')

imgi1=np.abs(f1)*(np.exp(i*phase2))
ift=np.fft.ifft2(imgi1)
plt.imshow(np.abs(ift), cmap='gray')

imgi2=np.abs(f2)*(np.exp(i*phase1))
ift=np.fft.ifft2(imgi2)
plt.imshow(np.abs(ift), cmap='gray')
