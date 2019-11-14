import cv2
import numpy as np
from matplotlib import pyplot as plt

def romil_hist(path,channel):
    im = cv2.imread(path)
    img = im[:,:,channel]
    z = np.zeros(256)
    for i in img:
        for j in i:
                z[j] = z[j] + 1           
    plt.plot(z)


#romil_hist('C:/Users/DSPLAB_USER/Downloads/lena.png',1)
#romil_hist('C:/Users/DSPLAB_USER/Downloads/buildLensBadGrid.jpg',1)
#imgg = cv2.imread('C:/Users/DSPLAB_USER/Downloads/buildLensBadGrid.jpg')
#
#for i in range(512):
#    for j in range(512):
#        if i <= 256:
#            imgg[:,:,0][i][j]  =  0
#        else: 
#            imgg[:,:,0][i][j] = 255
#
#imgg[:,:,1] = imgg[:,:,0]
#imgg[:,:,2] = imgg[:,:,0]
#
#plt.imshow(imgg)
path = 'C:/Users/DSPLAB_USER/Downloads/lena.png'
im = cv2.imread(path)
img = im[:,:,0]
z = np.zeros(256)
for i in img:
    for j in i:
            z[j] = z[j] + 1   

for i in range(256):
    z[i] = z[i]/(512*512)

for i in range(256):
    z[i] = z[i] + z[i-1]
    
plt.plot(z)

#z1 = cv2.calcHist([img],[0],None,[256],[0,256])
#plt.plot(z1)

