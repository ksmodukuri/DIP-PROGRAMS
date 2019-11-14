# -*- coding: utf-8 -*-
"""
Created on Sat Jul 27 01:45:35 2019

@author: Paresh Shahare   
"""

n=int(input('Enter a number'))

def positive(n):
    print('-'*25)
    print('The input number is : {}',format(n))
    if n>0:
        print('positive')
    elif n<0:
        print('negative')
    else:
        print('zero')

def even(n):
    print('-'*25)
#    print('The input number is :::::')
    if n==0:
        print('Neither even nor odd')
    elif n%2==0:
        print('even')
    else:
        print('odd')
    
def prime(n):
    print('-'*25)
    count=0
    for i in range(2,n-1,1):
        if n%i==0:
            count+=1
    if n==0:
        print('Neither prime nor composite')
    elif n==1:
        print('Neither prime nor composite')
    elif count>0:
        print('composite number')
    else:
        print('prime number')

def factorial(n):
    print('-'*25)
    fact=1
    for i in range(2,n+1,1):
        fact=fact*i
    print('factorial = {}'.format(fact))

def pattern():
    print('-'*25)
    print('pattern')
    i=1
    for i in range(7):
        for j in range(i):
            print('*',end='')
        print('  ')
    print('-'*25)
positive(n)
even(n)
prime(n)
factorial(n)
pattern()
print(':'*40)       
import numpy as np
a=np.array([(1,2,3),(4,5,6),(7,8,9)])
b=np.array([(10,11,12),(13,14,15),(16,17,18)])
c=np.add(a,b)
d=np.subtract(b,a)
e=np.multiply(a,b)
f=np.divide(b,a)
g=np.sqrt(e)
print('Array a : ')
print(a)
print('Array b : ')
print(b)
print('Addition :')
print(c)
print('Substraction :')
print(d)
print('Multiplication :')
print(e)
print('Divide :')
print(f)
print('SquareRoot of b :')
print(g)        