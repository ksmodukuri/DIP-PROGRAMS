# -*- coding: utf-8 -*-
"""
Created on Wed Oct  9 22:42:35 2019

@author: Neha Kala
"""


#Prime or not
x = int(input("Enter a number: "))
def prime(x):
    if x>1:
        for i in range(2,x):
            if x % i == 0:
                print("Number is not a prime")
                break
        else:
                print("number is a prime")
    else:
        print("Number is not a prime")
prime(x)    


#even/odd
x=int(input("enter a number:-  "))
def Check_Number(x):
    if (x%2==0):
        print("number is even")
    else:
         print("number is odd")
Check_Number(x)



x = int(input("Enter the number :-  "))
def stars(x):
    for i in range(1,x+1):
        print("*"*i)       
stars(x)



#Factorial
y=int(input("enter a no:-  "))
def factorial(y):
    f=1    
    if y<1:
        print("factorial doesn't exist")
    elif y==0:
        print("factorial is zero")   
    else:
        for i in range(1,y+1):
            f=f*i
        print("factorial is", f)
factorial(y) 



#positive/negative
x=int(input("enter a number:-  "))
def check(x):
    if (x>0):
        print("number is positive")
    elif (x==0):
        print("number is zero")
    else:
        print("number is negative")
check(x)


#transpose of matrix
import numpy as np
x=np.array([[1,2,3],[4,5,6],[3,6,8]])
print("x=",x)
y=np.array([[0,0,0],[0,0,0],[0,0,0]])

for i in range(len(x)):
    for j in range(len(x)):
        y[i][j]=x[j][i]
        
for r in y:
    print("transpose=",r)
      

#matrix multiplication
import numpy as np
x = np.array([[1,2,3], [4,5,6]])
print("x",x)
y = np.array([[1,2,3], [4,5,6]])
print("y",y)
z=x*y
print("z",z)


#upper triangular matrix
import numpy as np  
M = [[1, 2, 3],[8, 6, 4],[4, 5, 6]];  
   
rows = len(M);  
cols = len(M[0]);  
   
N=np.zeros((3,3),int) 
print("Upper triangular matrix: ");  
for i in range(0, rows):  
    for j in range(0, cols):  
        if(i > j):  
            N[i][j]=0  
        else:  
            N[i][j]=M[i][j] 
   
print(N) 


#sum of elements of matrix
import numpy as np  
M =np.array([[1, 2, 3],[8, 6, 4],[4, 5, 6]]);  
sum=0
for i in range(len(M)):
    for j in range(len(M[0])):
        sum +=M[i][j]
print("sum of elements of matrix: = ",sum)


#Recursion function
def recursion_fun(x):
    if x == 1:
        return 1
    else:
        return (x * recursion_fun(x-1))

N = int(input("enter a number: "))
print("The factorial of", N, "is", recursion_fun(N))


#multiplication table
import numpy as np
num = np.array([1,2,3,4,5,6,7,8,9,10])

for i in range(1, 11):
   print(num*i)