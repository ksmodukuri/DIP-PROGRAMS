import cv2
import matplotlib.pyplot as plt
import numpy as np

path = '/home/romil/Downloads/pout.png'

def histogram_equalizer(path):
	img = cv2.imread(path,0)
	z = np.zeros(256)
	for i in img:
		for j in i:
			z[j] = z[j] + 1
	total = sum(z)
	for i in range(256):
		z[i] = z[i]/total
	for i in range(256):
		z[i] = z[i] + z[i-1]
	for i in range(256):
		z[i] = z[i]*255
		z[i] = round(z[i])
	size = np.shape(img)
	for i in range(size[0]):
		for j in range(size[1]):
			img[i][j] = z[img[i][j]]
	return img

imgg = cv2.imread(path,0)
plt.figure(1)
plt.subplot(1,2,1)
plt.imshow(imgg,cmap = 'gray')
plt.subplot(1,2,2)
plt.imshow(histogram_equalizer(path) ,cmap = 'gray')
