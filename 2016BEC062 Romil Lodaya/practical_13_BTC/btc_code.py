import numpy as np
import cv2
import matplotlib.pyplot as plt
img = cv2.imread('/home/romil/Downloads/lena.png', 0)

def a(patch,q):
    return np.mean(patch) - np.std(patch)*np.sqrt(q/(4-q))

def b(patch,q):
    if np.std(patch) == 0:
        return np.mean(patch)
    else:
        return np.mean(patch) + (np.std(patch)*np.sqrt((4-q)/q))
    
for i in range(256):
    for j in range(256):
        patch = img[i*2:i*2+2,j*2:j*2+2]
        block = patch - np.mean(patch)             
        block[block >= 0] = 1
        block[block < 0] = 0        
        q = 4 - np.count_nonzero(block)
        block[block > 0] = b(patch,q)
        block[block <= 0] = a(patch,q)
        img[i*2:i*2+2,j*2:j*2+2] = block

plt.imshow(img , cmap = 'gray')
