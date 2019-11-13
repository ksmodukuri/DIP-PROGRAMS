import numpy as np
import cv2
import matplotlib.pyplot as plt

a = cv2.imread('lena.png',0)
i0 = np.int32(np.array(np.zeros([512,512])))
b = np.int32(np.array(np.zeros([512,512])))

for i in range(512):
    for j in range(512):
        b[i][j] = np.binary_repr(a[i][j])

for k in range(8):
    for i in range(512):
        for j in range(512):
            i0[i][j] = b[i][j]%10
            b[i][j] = np.int32(b[i][j] / 10)
    plt.subplot(2,4,k+1)
    plt.imshow(i0,cmap='gray')
    plt.title(str(k) +' bit plane')
    plt.xlabel('Pixel')
    plt.ylabel('Pixel')