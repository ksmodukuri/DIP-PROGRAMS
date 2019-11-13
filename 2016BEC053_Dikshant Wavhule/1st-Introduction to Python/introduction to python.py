
#No. is Positive or Negative
num = float(input("Enter a number: "))
if num > 0:
   print("Positive number")
else:
   print("Negative number")

#No. is Even or Odd   
num1 = int(input("Enter a number: "))
if (num1 % 2) == 0:
   print("no. is Even")
else:
   print("no. is Odd")

#Prime No.   
num2 = int(input("Enter a number: "))
if num2 > 1:
   for i in range(2,num2):
       if (num2 % i) == 0:
           print(num2,"is not a prime number")
           break
       else:
           print(num2,"is a prime number")
           break

#Factorial Of a No.       
num3 = int(input("Enter a number: ")) 
factorial = 1      
for i in range(1,num3 + 1):
    factorial = factorial*i
    
print("The factorial of",num3,"is",factorial)

#Star Sequence
for i in range (0, 4):
    for j in range(0, i + 1):
        print("*", end=' ')
    print()

#Transpose of a Matrix
import numpy as np
X =np.array(([32,1],[43 ,75],[9 ,5]))

result =np.array(([0,0,0],[0,0,0]))


for i in range(len(X)):
   
   for j in range(len(X[0])):
       result[j][i] = X[i][j]
print("transpose is")
for r in result:
   print(r) 

#Addition Of a Matrix
X1 =np.array(([12,7,3],[4 ,5,6],[7 ,8,9]))
Y = np.array(([5,8,1],[6,7,3],[4,5,9]))
result =np.array(([0,0,0],[0,0,0],[0,0,0]))

for i in range(len(X)):
   
   for j in range(len(X[0])):
       result[i][j] = X[i][j] + Y[i][j]
print("addition of matrix")
for r in result:
   print(r)  

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
   
   
#Multiplication of a Matrix
X =np.array(([2,7,3],[4 ,5,6],[7,8,9]))
Y =np.array(([5,8,1],[6,7,3],[4,5,9]))
result = np.array(([0,0,0],[0,0,0],[0,0,0]))

for i in range(len(X)):
   for j in range(len(Y[0])):
       for k in range(len(Y)):
           result[i][j] += X[i][k] * Y[k][j]
print("multiplication of matrix is")
for r in result:
   print(r)

#Multiplication Tables
for i in range(1,11):
    for j in range(1,11):
        x=i*j
        print(x,end="\t")
    print()