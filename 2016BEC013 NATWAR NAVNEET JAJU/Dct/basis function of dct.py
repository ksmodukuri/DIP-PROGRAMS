# -*- coding: utf-8 -*-

import numpy as np

import matplotlib.pyplot as plt

F = np.zeros((4,4))

counter = 0
for k in range(4):
    for l in range(4):
        for i in range(4):
            for j in range(4):
                if k == 0:
                    if l == 0:
                        alpha_k = (1/4)**0.5
                        alpha_l = (1/4)**0.5
                        F[i][j] = alpha_k * alpha_l * np.cos(((2*i+1)*3.14*k)/(2*4)) * np.cos(((2*j+1)*3.14*l)/(2*4))
                       
                    else:
                        alpha_k = (1/4)**0.5
                        alpha_l = (2/4)**0.5
                        F[i][j] = alpha_k * alpha_l * np.cos(((2*i+1)*3.14*k)/(2*4)) * np.cos(((2*j+1)*3.14*l)/(2*4))
                        
                else:
                    alpha_k = (2/4)**0.5
                    alpha_l = (2/4)**0.5
                    F[i][j] = alpha_k * alpha_l * np.cos(((2*i+1)*3.14*k)/(2*4)) * np.cos(((2*j+1)*3.14*l)/(2*4))
                    
                if i == 3 and j == 3:
                    counter = counter + 1
                    plt.subplot(4,4,counter)
                    plt.imshow(F,cmap = 'gray')
                    