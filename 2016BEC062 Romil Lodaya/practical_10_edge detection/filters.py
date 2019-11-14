from skimage import io
import numpy as np
import matplotlib.pyplot as plt
import cv2

imgg = io.imread('/home/romil/Pictures/house.jpeg')
img = imgg[:,:,0]
plt.subplot(3,3,1)
plt.imshow(imgg)
plt.title('original img')

window = np.array([[-1,-1,-1],[0,0,0],[1,1,1]])
img = np.pad(img,1,'constant')
new_img = np.zeros([554,554])

for i in range(554):
    for j in range(554):
        val = img[i:i+3,j:j+3]*window
        new_img[i][j] = abs(np.sum(val))
plt.subplot(3,3,2)
plt.imshow(np.uint8(new_img),cmap = 'gray')
plt.title('Prewitt horizontal mask')



imgg = io.imread('/home/romil/Pictures/house.jpeg')
img = imgg[:,:,0]
window = np.array([[1,0,-1],[1,0,-1],[1,0,-1]])
img = np.pad(img,1,'constant')
new_img = np.zeros([554,554])

for i in range(554):
    for j in range(554):
        val = img[i:i+3,j:j+3]*window
        new_img[i][j] = int(abs(np.sum(val)))
plt.subplot(3,3,3)
plt.imshow(np.uint8(new_img),cmap = 'gray')
plt.title('Prewitt Vertical mask')


window = np.array([[1,0],[0,-1]])
img = np.pad(img,1,'constant')
new_img = np.zeros([554,554])

for i in range(554):
    for j in range(554):
        val = img[i:i+2,j:j+2]*window
        new_img[i][j] = int(abs(np.sum(val)))
plt.subplot(3,3,4)
plt.imshow(np.uint8(new_img),cmap = 'gray')
plt.title('Roberts Vertical mask')


window = np.array([[0,1],[-1,0]])
img = np.pad(img,1,'constant')
new_img = np.zeros([554,554])

for i in range(554):
    for j in range(554):
        val = img[i:i+2,j:j+2]*window
        new_img[i][j] = int(abs(np.sum(val)))
plt.subplot(3,3,5)
plt.imshow(np.uint8(new_img),cmap = 'gray')
plt.title('Roberts horizontal mask')


window = np.array([[-1,0,1],[-2,0,2],[-1,0,1]])
img = np.pad(img,1,'constant')
new_img = np.zeros([554,554])

for i in range(554):
    for j in range(554):
        val = img[i:i+3,j:j+3]*window
        new_img[i][j] = int(abs(np.sum(val)))
plt.subplot(3,3,6)
plt.imshow(np.uint8(new_img),cmap = 'gray')
plt.title('Sobel vertical mask')

window = np.array([[-1,-2,-1],[0,0,0],[1,2,1]])
img = np.pad(img,1,'constant')
new_img = np.zeros([554,554])

for i in range(554):
    for j in range(554):
        val = img[i:i+3,j:j+3]*window
        new_img[i][j] = int(abs(np.sum(val)))
plt.subplot(3,3,7)
plt.imshow(np.uint8(new_img),cmap = 'gray')
plt.title('Sobel horizontal mask')

