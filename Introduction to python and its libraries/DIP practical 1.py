# -*- coding: utf-8 -*-
"""
Created on Thu Jul 25 23:47:03 2019

@author: KARTIK
"""
# =============================================================================
# To identify positive numbers
n = 12
if n > 0:
    print("the entered number {} is positive".format(n))
elif n == 0:
    print("the entered number is neither negative nor postive".format(n))
else:
    print("the entered number {} is negative".format(n))
# =============================================================================

# =============================================================================
# To identify even and odd numbers
n = int(input()) #integer
if n%2 == 0:
    print("the entered number {} is even".format(n))
else:
    print("the entered number {} is odd".format(n))
# =============================================================================

# =============================================================================
# Printing a specific * pattern
n = int(input())
for i in range(n):
    for j in range(i+1):
        print("*", end = " ")
    print("\n")
# =============================================================================

# =============================================================================
# Calculating factorial of a number using recursion
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n*factorial(n-1)
if __name__ == "__main__":
    n = int(input())
    result = factorial(n)
    print("factorial of the entered number is {}".format(result))        
            
# =============================================================================

# =============================================================================
# Calculate the facctorial of a number without recursion
n = int(input())
result = 1
if n > 0:
    while n > 0:
        result = result * n
        n -= 1

if n < 0:
    result = "inavlid"

print("Factorial of the entered number is {}".format(result))
 
# =============================================================================

# =============================================================================
# Finding Transpose of a matrix
import numpy as np
a = np.array([[1,2,3,4],[1,2,4,5],[4,5,4,7],[6,5,2,1]])
b = np.zeros((4,4))
print(a)
for i in range(len(a)):
    for j in range(len(a[0])):
        b[j][i] = a[i][j]

print("transpose of matrix a \n{}".format(b))
 
# =============================================================================

# =============================================================================
# Summatoin of elements of a matrix
import numpy as np
a = np.array([[1,2,3,4],[1,2,4,5],[4,5,4,7],[6,5,2,1]])
sum_of_matrix = 0
for i in range(len(a)):
    for j in range(len(a[0])):
        sum_of_matrix += a[i][j]

print("the Sum of elements of the matrix a is {}".format(sum_of_matrix))
# =============================================================================

# =============================================================================
# Summatoin of elements of a matrix using sum function
import numpy as np
a = np.array([[1,2,3,4],[1,2,4,5],[4,5,4,7],[6,5,2,1]])
sum_of_matrix = sum(sum(a))
print("the Sum of elements of the matrix a is {}".format(sum_of_matrix))
 
# =============================================================================
# =============================================================================
# Multiplication of a 1-D and 2-D matrices
import numpy as np
g = np.array([1,2,3,4,5])
g_1 = np.zeros(5)
for i in range(len(g)):
    g_1[i] = g[i] * g[i]

print("Multiplication of 1-D array = \n",g_1)

h = np.array([[1,2,3,4,5],[2,3,4,5,6]])
m = np.array([[2,3,4,5,6],[1,2,3,4,5]])
result = np.zeros((2,5))
for i in range(len(h)):
    for j in range(len(m[0])):
        for k in range(len(m)):
            result[i][j] += h[i][k] * m[k][j]

print("Multiplication of 2-D array = \n",result)
# =============================================================================

# =============================================================================
# Upper Triangle
import numpy as np
M = np.array([[1,3,4],[3,6,7],[7,1,5]])
N = np.zeros((3,3))
print("Upper Triangle matrix = \n")
for i in range(len(M)):
    for j in range(len(M[0])):
        if(i > j):
            N[i][j] = 0
        else:
            N[i][j] = M[i][j]
print(N)
# =============================================================================

# =============================================================================
# Multiplication table
a = []
for i in range(1,11):
    print(i,end = "\t")
    a.append(i)
print("\n")
len(a)
for j in range(2,11):
    print(j,end = "\t")
    for k in range(1,10):
        print(j*a[k],end = "\t")
    print("\n")
# =============================================================================
