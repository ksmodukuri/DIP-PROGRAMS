import cv2
import matplotlib.pyplot as plt
import numpy as np
img1=cv2.imread(r"D:\Btech practicals\DIP\blackbox_2.jpg",0)
plt.subplot(341)
plt.imshow(img1, cmap = 'gray')
f1 = np.fft.fft2(img1)
fshift1 = np.fft.fftshift(f1)
magnitude1 = 20*np.log(1+np.abs(fshift1))
plt.subplot(342)
plt.imshow(magnitude1, cmap = 'gray')

ishift1 = np.fft.ifftshift(fshift1)
img11 = np.fft.ifft2(ishift1)
img11 = np.abs(img11)

phase1=np.angle(fshift1)
plt.subplot(343)
plt.imshow(phase1, cmap = 'gray')

plt.subplot(344)
plt.imshow(img11, cmap = 'gray')

img2=cv2.imread(r"D:\Btech practicals\DIP\whitebox_2.jpg",0)
plt.subplot(345)
plt.imshow(img2, cmap = 'gray')
f2 = np.fft.fft2(img2)
fshift2 = np.fft.fftshift(f2)
magnitude2 = 20*np.log(1+np.abs(fshift2))
plt.subplot(346)
plt.imshow(magnitude2, cmap = 'gray')

ishift2 = np.fft.ifftshift(fshift2)
img_2 = np.fft.ifft2(ishift2)
img_2 = np.abs(img_2)

phase2=np.angle(fshift2)
plt.subplot(347)
plt.imshow(phase2, cmap = 'gray')

plt.subplot(348)
plt.imshow(img_2, cmap = 'gray')

img3 = cv2.imread(r"D:\Btech practicals\DIP\whitebox_rotate.jpg",0)
plt.subplot(349)
plt.imshow(img3, cmap = 'gray')
f3 = np.fft.fft2(img3)
fshift3 = np.fft.fftshift(f3)
magnitude3 = 20*np.log(1+np.abs(fshift3))
plt.subplot(3,4,10)
plt.imshow(magnitude3, cmap = 'gray')

ishift3 = np.fft.ifftshift(fshift3)
img_3 = np.fft.ifft2(ishift3)
img_3 = np.abs(img_3)

phase3 = np.angle(fshift3)
plt.subplot(3,4,11)
plt.imshow(phase3, cmap = 'gray')

plt.subplot(3,4,12)
plt.imshow(img_3, cmap = 'gray')

