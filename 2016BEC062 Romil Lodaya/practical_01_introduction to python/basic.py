print('Hello World')
import numpy as np
a =np.array([[1,2,3],[3,2,1]])
print(type(a))
print(a.shape)

###Conditional loop
b=-10
if b>0:
    print('Positive Number!')
else:
    print('Negative Number!')

##Defining Function
def number(b):
    if b>0:
        print('Positive Number!')
    else:
        print('Negative Number!')
number(2)

x=np.array([[1,2,3],[3,2,1]])
y=np.array([[4,5,6],[6,5,4]])
z=np.array([1,4,9])
z1=np.add(x,y)
z2=np.subtract(x,y)
z3=np.multiply(x,y)
z4=np.divide(x,y)
z5=np.sqrt(z)
z6=np.dot(x,np.transpose(y))
z7=np.sum(x)
z8=np.sum(z,axis=0)
z9=np.zeros(4)
z10=np.ones(4)

import cv2
from matplotlib import pyplot as plt
img=cv2.imread('Desktop/lena.png')
print(img[100,100])
r,c,d=img.shape[0:3]
size=img.shape
dtype=img.dtype
cv2.imshow('image',img)
plt.imshow(img)
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
 
#+ve/-ve
def positive_negative(number):
    if number > 0:
        return "positive"
    elif number < 0 :
        return "negative"
    elif number == 0:
        return "neither positive nor negative"
print(positive_negative(5))


#even/odd
def odd_even(number):
    if number % 2 == 0:
        return "even"
    elif number % 2 == 1 :
        return "odd"
number = int(input("Enter a Number to check:-"))
print(odd_even(number))

#prime/not
number = int(input("Enter a Number to check:-  "))
def prime(number):
    for i in range(2,number):
        if number % i == 0:
            return "not prime"
            break
        else :
            return "prime"
print(prime(number))

#factorial
def factorial(number):
    x = 1
    for i in range(1,number+1):
        x = x*i
    return x
print(factorial(5))    

#star pattern
def star(number):
    for i in range(number+1):
        print('*'*i)
star(number)

#matrix transpose
X = [[12,7],[4 ,5],[3 ,8]]
result = [[0,0,0],[0,0,0]]
for i in range(len(X)):
   for j in range(len(X[0])):
       result[j][i] = X[i][j]
for r in result:
   print(r)
   
#sum of matrix
X = [[1,2,3], [4 ,5,6], [7 ,8,9]] 
Y = [[9,8,7], [6,5,4], [3,2,1]] 
result = [[0,0,0], [0,0,0], [0,0,0]] 
for i in range(len(X)):     
    for j in range(len(X[0])): 
        result[i][j] = X[i][j] + Y[i][j] 
for r in result: 
    print(r) 

#multiplication of matrix
# Program to multiply two matrices using nested loops 
A = [[12, 7, 3], [4, 5, 6], [7, 8, 9]]   
B = [[5, 8, 1, 2], [6, 7, 3, 0], [4, 5, 9, 1]]      
result = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]] 
for i in range(len(A)):   
    for j in range(len(B[0])): 
        for k in range(len(B)): 
            result[i][j] += A[i][k] * B[k][j] 
for r in result: 
    print(r) 

for i in range(1,11):
    for j in range(1,11):
        print(str(i*j).zfill(2),end= " ")
    print(" ")

#program for upper traingular matrix 
def upper(matrix, row, col): 
    for i in range(0, row): 
        for j in range(0, col): 
            if (i > j): 
                print("0", end = " "); 
            else: 
                print(matrix[i][j],  
                       end = " " ); 
        print(" "); 
    
upper(matrix = [[1, 2, 3],[4, 5, 6],[7, 8, 9]],row=3,col=3) 

#program for recursive factorial
def factorial(n):
    if(n <= 1):
        return 1
    else:
        return(n*factorial(n-1))
n = int(input("Enter number:"))
print("Factorial:",factorial(n))
