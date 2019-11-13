import cv2
from matplotlib import pyplot as plt
 
img = cv2.imread('lena.png')
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))   

for j in range(0,512):
    for k in range(0,512) :
        if img[:,:,0][j][k] >=0 and img[:,:,0][j][k]<64:
            img[:,:,0][j][k] = 0
        elif img[:,:,0][j][k] >=64 and img[:,:,0][j][k]<128:
             img[:,:,0][j][k] = 80
        elif img[:,:,0][j][k] >=128 and img[:,:,0][j][k]<192:
             img[:,:,0][j][k] = 160               
        elif img[:,:,0][j][k] >=192 and img[:,:,0][j][k]<256:
             img[:,:,0][j][k] = 255
 
 
img1 = img[:,:,1]
for j in range(0,512):
    for k in range(0,512) :
         if img1[j][k] >=0 and img1[j][k]<64:
             img1[j][k] = 0
         elif img1[j][k] >=64 and img1[j][k]<128:
             img1[j][k] = 80
         elif img1[j][k] >=128 and img1[j][k]<192:
             img1[j][k] = 160               
         elif img1[j][k] >=192 and img1[j][k]<256:
             img1[j][k] = 255
 
img[:,:,2] = img[:,:,1]
img[:,:,0] = img[:,:,1]
plt.imshow(img)


img2 = img[:,:,1]
for j in range(0,512):
    for k in range(0,512) :
        if img2[j][k] >=0 and img2[j][k]<127:
            img2[j][k] = 0
        elif img2[j][k] >=128 and img2[j][k]<256:
            img2[j][k] = 255
            
img[:,:,2] = img[:,:,1]
img[:,:,0] = img[:,:,1]
plt.imshow(img)

 
img = cv2.imread('pout.jpg')
plt.imshow(img)


imgp = img[:,:,0]
for j in range(0,247):
    for k in range(0,204) :
        if imgp[j][k] >=0 and imgp[j][k]<100:
            imgp[j][k] = imgp[j][k]*0.5 
        elif imgp[j][k] >=100 and imgp[j][k]<200:
            imgp[j][k] = imgp[j][k]*1.5 -100
        elif imgp[j][k] >=200 and imgp[j][k]<255:
            imgp[j][k] = imgp[j][k]
plt.imshow(img[:,:,0] , cmap = 'gray')
cv2.imwrite('pout1.png' , img[:,:,0])


 


