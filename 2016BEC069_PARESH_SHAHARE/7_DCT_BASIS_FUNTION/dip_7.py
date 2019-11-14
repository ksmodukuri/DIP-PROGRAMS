import cv2
import numpy as np
from matplotlib import pyplot as plt
N=4
a=1
ak=np.sqrt(2/N)
al=np.sqrt(2/N)
F=np.zeros([4,4,4,4])
for k in range (N):
    for l in range(N):
        for m in range (N):
            for n in range (N):
                F[k][l][m][n]=np.cos(((2*m+1)*3.14*k)/2*N)*np.cos(((2*n+1)*3.14*l)/2*N)       
for k in range(N):
    for l in range(N):
        plt.subplot(N,N,a)
        plt.imshow(F[k][l])
        a+=1
