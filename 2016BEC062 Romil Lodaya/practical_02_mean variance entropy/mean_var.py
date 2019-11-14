import cv2
import numpy as np

def mean(img):
    #mean = np.mean(img)
    summ = 0
    counter = 0
    for i in img:
        for j in i:
            for k in j:
                summ += k
                counter += 1
    return summ/counter
        
def var(img,mean):
    #var = np.var(img)
    summ = 0
    counter = 0
    for i in img:
        for j in i:
            for k in j:
                summ += ((k-mean))**2
                counter += 1
    
    return summ/counter

def energy(img):
    summ = 0
    for i in img:
        for j in i:
            for k in j:
                summ += k*k
    return summ
        
def entropy(img):
    intensity = np.zeros(256) 
    t1 = img[:,:,0]
    for i in t1:
        for j in i:
            intensity[j] += 1       
    
    for i in range(len(intensity)):
        intensity[i] = intensity[i]/(512*512)
    
    for i in range(len(intensity)):
        if intensity[i] == 0:
            i+=1
        else:
            intensity[i] = intensity[i]*(np.log2(intensity[i]))

    return -np.sum(intensity)    
    
img = cv2.imread('/home/romil/Downloads/lena.png')
mean = mean(img)
var = var(img,mean)
energy = energy(img)
ent = entropy(img) 
print("Mean = ",mean)
print("Var = ",var)
print("Energy = ",energy)
print("Entropy = ",ent)
    
