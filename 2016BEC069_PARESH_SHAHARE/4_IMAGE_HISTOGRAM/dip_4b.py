import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("lena5.jpg")
intensity = np.zeros(256) 
t1 = img[:,:,0]
for i in t1:
    for j in i:
        intensity[j] += 1
plt.subplot(121)       
plt.plot(intensity)

for i in range(len(intensity)):
    intensity[i] = intensity[i]/(512*512)
cdf = []
a = 0
for i in intensity:
    a += i
    cdf.append(a)
plt.subplot(122)       
plt.plot(cdf)