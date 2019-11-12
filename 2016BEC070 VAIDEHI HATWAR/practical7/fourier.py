# -*- coding: utf-8 -*-
"""
Created on Sun Oct  6 23:42:58 2019

@author: Mypc
"""

 
 

import numpy as np
from matplotlib import pyplot as plt
N=4
d=np.zeros((4,4))
c=0
for k in range(4):
    for l in range(4):
        for m in range(4):
            for n in range(4):
                N=4
                if k == 0:
                    if l == 0:
                        ak = (1/N)**0.5;
                        al = (1/N)**0.5;
                        d[m][n]=ak*al*np.cos(((2*m+1)*3.14*k)/(2*N))*np.cos(((2*n+1)*3.14*l)/(2*N))
                    else:
                        ak = (1/N)**0.5
                        al = (2/N)**0.5
                        d[m][n]=ak*al*np.cos(((2*m+1)*3.14*k)/(2*N))*np.cos(((2*n+1)*3.14*l)/(2*N))
                else:
                    ak = (2/N)**0.5
                    al = (2/N)**0.5
                    d[m][n]=ak*al*np.cos(((2*m+1)*3.14*k)/(2*N))*np.cos(((2*n+1)*3.14*l)/(2*N))
        if (m==3 and n==3):
             c = c + 1
             plt.subplot(4,4,c)
             plt.imshow(d,cmap = 'gray')
             plt.axis("off")
 

        

