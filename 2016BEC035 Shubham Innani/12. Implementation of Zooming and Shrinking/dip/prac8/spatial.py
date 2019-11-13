import cv2
import numpy as np
from matplotlib import pyplot as plt
import random
from scipy.signal import medfilt as mf

## Program for median filtering 
img = cv2.imread('C:/Users/CoE_28/Desktop/dip/lena.png',0)
def sp_noise(image,prob):
    output = np.zeros(image.shape,np.uint8)
    thres = 1 - prob 
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            rdn = random.random()
            if rdn < prob:
                output[i][j] = 0
            elif rdn > thres:
                output[i][j] = 255
            else:
                output[i][j] = image[i][j]
    return output

noise_img = sp_noise(img,0.05)
amf= mf(noise_img,3)
plt.subplot(1,3,1)
plt.imshow(img,cmap='gray')
plt.title('Original Image')
plt.subplot(1,3,2)
plt.imshow(noise_img, cmap='gray')
plt.title('Noisy Image')
plt.subplot(1,3,3)
plt.imshow(amf,cmap='gray')
plt.title('Using Function')
plt.subplots_adjust(hspace=0.25, wspace=0.35)

img1 = np.pad(noise_img,1,mode='constant')
a1=np.zeros([512,512])
a2=np.zeros([512,512])
a3=np.zeros([512,512])

for i in range(514):
    for j in range(514):
        patch_img = img1[i:i+3, j:j+3]
        med = np.median(patch_img)
        a1[i:i+1, j:j+1] = med
for i in range(514):
    for j in range(514):
        patch_img = img1[i:i+5, j:j+5]
        med = np.median(patch_img)
        a2[i:i+1, j:j+1] = med
for i in range(514):
    for j in range(514):
        patch_img = img1[i:i+7, j:j+7]
        med = np.median(patch_img)
        a3[i:i+1, j:j+1] = med      
plt.subplot(2,2,1)
plt.imshow(img1,cmap='gray')
plt.title('Noisy Image')
plt.subplot(2,2,2)
plt.imshow(a1,cmap='gray')
plt.title('Median Filtering with k=3')
plt.subplot(2,2,3)
plt.imshow(a2,cmap='gray')
plt.title('Median Filtering with k=5')
plt.subplot(2,2,4)
plt.imshow(a3,cmap='gray')
plt.title('Median Filtering with k=7')
plt.subplots_adjust(hspace=0.5,wspace=0.35)
psnr =10*np.log10((255*255)) - 10*np.log10((1/(512*512))*(np.sum((noise_img-a3)**2)))
## Program for Average filtering
img = cv2.imread('C:/Users/CoE_28/Desktop/dip/lena.png',0)
img1 = np.pad(img,1,mode='constant')
blur1 = cv2.blur(img1,(3,3))
blur2 = cv2.blur(img1,(5,5))
blur3 = cv2.blur(img1,(7,7))

plt.subplot(2,2,1)
plt.imshow(img1,cmap='gray')
plt.title('Original Image')
plt.subplot(2,2,2)
plt.imshow(blur1,cmap='gray')
plt.title('Average Blurr with k=3')
plt.subplot(2,2,3)
plt.imshow(blur2,cmap='gray')
plt.title('Average Blurr with k=5')
plt.subplot(2,2,4)
plt.imshow(blur3,cmap='gray')
plt.title('Average Blurr with k=7')
plt.subplots_adjust(hspace=0.5,wspace=0.35)
psnr =10*np.log10((255*255)) - 10*np.log10((1/(512*512))*(np.sum((img1-blur2)**2)))

a1=np.zeros([513,513])
for i in range(512):
    for j in range(512):
        patch_img = img1[i:i+3, j:j+3]
        avg = np.average(patch_img)
        a1[i:i+1, j:j+1] = np.round(avg)
a2=np.zeros([513,513])
for i in range(512):
    for j in range(512):
        patch_img = img1[i:i+5, j:j+5]
        avg = np.average(patch_img)
        a2[i:i+1, j:j+1] = np.round(avg)
a3=np.zeros([513,513])
for i in range(512):
    for j in range(512):
        patch_img = img1[i:i+7, j:j+7]
        avg = np.average(patch_img)
        a3[i:i+1, j:j+1] = np.round(avg)
psnr =10*np.log10((255*255)) - 10*np.log10((1/(512*512))*(np.sum((img-a1)**2)))
plt.subplot(2,2,1)
plt.imshow(img1,cmap='gray')
plt.title('Original Image')
plt.subplot(2,2,2)
plt.imshow(a1,cmap='gray')
plt.title('Average Blurr with k=3')
plt.subplot(2,2,3)
plt.imshow(a2,cmap='gray')
plt.title('Average Blurr with k=5')
plt.subplot(2,2,4)
plt.imshow(a3,cmap='gray')
plt.title('Average Blurr with k=7')
plt.subplots_adjust(hspace=0.5,wspace=0.35)

def gauss(image):
      row,col= image.shape
      mean = 0
      var = 0.1
      sigma = var**0.5
      gauss = np.random.normal(mean,sigma,(row,col))
      gauss = gauss.reshape(row,col)
      noisy = image + gauss
      return noisy

img = cv2.imread('C:/Users/CoE_28/Desktop/dip/lena.png',0)
plt.imshow(img,cmap='gray')
img1= gauss(img)
blur = cv2.GaussianBlur(img,(3,3),0)
psnr =10*np.log10((255*255)) - 10*np.log10((1/(512*512))*(np.sum((img-blur)**2)))
plt.subplot(1,3,1)
plt.imshow(img,cmap='gray')
plt.title('Original Image')
plt.subplot(1,3,2)
plt.imshow(blur, cmap='gray')
plt.title('Gaussian Blurr with function')
plt.subplot(1,3,3)
plt.imshow(img1,cmap='gray')
plt.title('Gaussian Blurr')
plt.subplots_adjust(hspace=0.55,wspace=0.65)

##Program for min and max filtering
img = cv2.imread('C:/Users/CoE_28/Desktop/dip/lena.png',0)
img1 = np.pad(img,1,mode='constant')
a1=np.zeros([512,512])
for i in range(514):
    for j in range(514):
        patch_img = img1[i:i+3, j:j+3]
        med = np.max(patch_img)
        a1[i:i+1, j:j+1] = med
a2=np.zeros([512,512])
for i in range(514):
    for j in range(514):
        patch_img = img1[i:i+5, j:j+5]
        med = np.max(patch_img)
        a2[i:i+1, j:j+1] = med
a3=np.zeros([512,512])
for i in range(514):
    for j in range(514):
        patch_img = img1[i:i+7, j:j+7]
        med = np.max(patch_img)
        a3[i:i+1, j:j+1] = med
plt.subplot(2,2,1)
plt.imshow(img,cmap='gray')
plt.title('Original Image')
plt.subplot(2,2,2)
plt.imshow(a1,cmap='gray')
plt.title('Max Filtering with k=3')
plt.subplot(2,2,3)
plt.imshow(a2,cmap='gray')
plt.title('Max Filtering with k=5')
plt.subplot(2,2,4)
plt.imshow(a3,cmap='gray')
plt.title('Max Filtering with k=7')
plt.subplots_adjust(hspace=0.5,wspace=0.35)
psnr =10*np.log10((255*255)) - 10*np.log10((1/(512*512))*(np.sum((img-a3)**2)))
img1 = np.pad(img,1,mode='constant')
a1=np.zeros([512,512])
for i in range(514):
    for j in range(514):
        patch_img = img1[i:i+3, j:j+3]
        med = np.min(patch_img)
        a1[i:i+1, j:j+1] = med
a2=np.zeros([512,512])
for i in range(514):
    for j in range(514):
        patch_img = img1[i:i+5, j:j+5]
        med = np.min(patch_img)
        a2[i:i+1, j:j+1] = med
a3=np.zeros([512,512])
for i in range(514):
    for j in range(514):
        patch_img = img1[i:i+7, j:j+7]
        med = np.min(patch_img)
        a3[i:i+1, j:j+1] = med
plt.imshow(img1,cmap='gray')
plt.subplot(2,2,1)
plt.imshow(img1,cmap='gray')
plt.title('Original Image')
plt.subplot(2,2,2)
plt.imshow(a1,cmap='gray')
plt.title('Min Filtering with k=3')
plt.subplot(2,2,3)
plt.imshow(a2,cmap='gray')
plt.title('Min Filtering with k=5')
plt.subplot(2,2,4)
plt.imshow(a3,cmap='gray')
plt.title('Min Filtering with k=7')
plt.subplots_adjust(hspace=0.5,wspace=0.35)
psnr =10*np.log10((255*255)) - 10*np.log10((1/(512*512))*(np.sum((img-a3)**2)))