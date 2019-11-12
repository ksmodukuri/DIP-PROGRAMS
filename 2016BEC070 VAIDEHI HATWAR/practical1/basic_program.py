# -*- coding: utf-8 -*-
"""
Created on Fri Oct  4 22:36:14 2019

@author: Mypc
"""
# check whether number is positive or neagative 
x=int(input("enter a number"))
if x>0:
    print(x,"is positive number")
elif x<0:
    print(x,"is negative number")
else:
        print("zero")

        
        
# check whether number is even or odd
x=int(input("enter a number"))
if (x%2==0):
    print(x,"is even number")
else:
    print(x,"is odd number")

# check whether number is even or odd using function       
x=int(input("Enter a number"))
def even_odd(x): #function definition
    if (x%2==0):
        print(x, "is a even number")
    else:
        print(x, "is a odd number")
even_odd(x)#call the function


# check whether number is prime or not
x=int(input("enter a number"))
for i in range(2,x):
    if(x%i==0):
     print(x,"is not prime number")
     break
else:
    print(x,"is prime number")


#factorial   
x=int(input("enter a number"))
result=1
for i in range(1,x+1):
    result=result*i
print("factorial of",x,"is",result)

#factorial using function
x=int(input("enter a number"))
def factorial(n):#function definition
    fact=1
    for i in range(1, n+1):
        fact=fact*i
    return fact    #return factorial 
result=factorial(x)#function call 
print("The factorial is",result)


#pattern
x=int(input("enter a number rows"))
for i in range(1,x+1):
    for j in range(1,i+1):
        print("*",end="")
    print()


#transpose a matrix  
x=[[1 ,4],
    [5 ,7]]
result=[[0,0],
         [0,0]]
for i in range(len(x)):   
   for j in range(len(x[0])):
       result[j][i] = x[i][j]
for r in result:
   print(r)

#multiplication of two matrix
x=[[2 ,1],
    [3,2]]

y=[[3,2],
    [0,1]]
result=[[0,0],
         [0,0]]
for i in range(len(x)):
   for j in range(len(y[0])):
       for k in range(len(y)):
           result[i][j] += x[i][k]*y[k][j]
for r in result:
   print(r)
    
   
#table  
for j in range(1,11):
    for k in range(1,11):
        print(j*k,end="\t")
    print("\n")


#factorial using recursion
def fact(n):
    if n==0:
        return 1
    else:
        return n*fact(n-1)
n=int(input("enter a number"))
result=fact(n)
print("factorial of",n,"is",result)


 

#Upper triangular matrix
import numpy as np
b=np.random.randint(1,4,[3,3])       #multidimensional array
print(b)
for i in range(0,3):  
        for j in range(0, 3):  
            if(i < j):  
                print("0")
            else:  
               print(b[i][j])  
        print(" ")


#Summation of all elements in matrix
arr = [[14, 17, 44],    
       [15, 6, 27],   
       [23, 2, 54]]   
print("\nSum of arr : ", np.sum(arr))

