import cv2
import numpy as np
from matplotlib import pyplot as plt
img = cv2.imread('/gdrive/My Drive/python/lena.png')

for j in range(0,512):
    for k in range(0,512) :
        imgg = img[:,:,1][j][k]
        
        if imgg >=0 and imgg<64:
            imgg = 0
        elif imgg >=64 and imgg<128:
            imgg = 80
        elif imgg >=128 and imgg<192:
            imgg = 160               
        elif imgg >=192 and imgg<256:
            imgg = 255
img[:,:,2] = img[:,:,1]
img[:,:,0] = img[:,:,1]

cv2.imwrite('/gdrive/My Drive/python/lena2.png',img)
