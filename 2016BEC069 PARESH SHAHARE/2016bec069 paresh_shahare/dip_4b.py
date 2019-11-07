#import cv2
#import matplotlib.pyplot as plt
#
#img = cv2.imread('lena5.jpg')
#img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
#h=[]
#for i in range(256):
#    h.append(0)
#p=[]
#for i in range(256):
#    p.append(0)
#c=[]
#for i in range(256):
#    c.append(0)
#for i in range(512):
#    for j in range(512):
#        k=img[i][j]
#        h[k]=h[k]+1
#num=sum(h)
#for i in range(256):
#    p[i]=h[i]/num
#print(sum(p))  
#plt.subplot(131)
#plt.hist(img.ravel(),256,[0,256])
#plt.subplot(132)
#plt.hist(p,256,[0,256])
#plt.show()

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
    
#hist1 = cv2.calcHist([img],[0],None,[256],[0,256])
#plt.subplot(322)
#plt.plot(hist1)
#
#intensity = np.zeros(256)
#t2 = img[:,:,1]
#for i in t2:
#    for j in i:
#        intensity[j] += 1
#plt.subplot(323)       
#plt.plot(intensity)
#
#hist1 = cv2.calcHist([img],[1],None,[256],[0,256])
#plt.subplot(324)
#plt.plot(hist1)
#
#intensity = np.zeros(256)
#t3 = img[:,:,2]
#for i in t3:
#    for j in i:
#        intensity[j] += 1
#plt.subplot(325)       
##plt.plot(intensity)
#
#hist1 = cv2.calcHist([img],[2],None,[256],[0,256])
#plt.subplot(326)
#plt.plot(cdf)

print("hjsdjf");print("sdfgh")