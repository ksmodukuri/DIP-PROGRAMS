import cv2
import numpy as np
import matplotlib.pyplot as plt

img1 = cv2.imread(r"D:\Btech practicals\DIP\2_gray.jpg",0)
plt.imshow(img1,cmap='gray')
plt.title('Original Image with Magnitude and Phase')

f1 = np.fft.fft2(img1)
fshift1 = np.fft.fftshift(f1)
fshift1.imag = 0

ishift1 = np.fft.ifftshift(fshift1)
img11 = np.fft.ifft2(ishift1)
img11 = np.abs(img11)

plt.title('Without Phase')
plt.imshow(img11,cmap='gray')


img2 = cv2.imread(r"D:\Btech practicals\DIP\2_gray.jpg",0)
f2 = np.fft.fft2(img2)
fshift2 = np.fft.fftshift(f2)

fshift2.real = 0

ishift2 = np.fft.ifftshift(fshift2)
img22 = np.fft.ifft2(ishift2)
img22 = np.abs(img22)

plt.title('Without Magnitude')
plt.imshow(img22,cmap='gray')
