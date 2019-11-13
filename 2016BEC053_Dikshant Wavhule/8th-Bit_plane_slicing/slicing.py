import numpy as np
from matplotlib import pyplot as plt
import cv2
img = cv2.imread('lena.png',0)
b = np.zeros((225,225))
c = np.zeros((225,225))
for i in range(225):
    for j in range(225):
        b[i][j] = np.binary_repr(img[i][j]) 

for k in range(8):
    for i in range(225):
        for j in range(225):
            c[i][j] = b[i][j]%10
            b[i][j] = np.int32(b[i][j]/10)
    plt.subplot(2,4,k+1)
    plt.imshow(c, cmap='gray')
    plt.title(str(k)+' bit plane')
    plt.xlabel('Pixel')
    plt.ylabel('Pixel')
