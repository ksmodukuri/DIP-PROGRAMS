 
import cv2
import matplotlib.pyplot as plt
img1 = cv2.imread("black.png",0)
img2 = cv2.imread("white.png",0)
plt.subplot(341)
plt.imshow(img1,cmap='gray') ;plt.title("img1")
plt.subplot(342)
plt.imshow(img2,cmap='gray') ;plt.title("img2")

ADD = cv2.add(img1,img2) 
plt.subplot(343)
plt.imshow(ADD,cmap='gray') ;plt.title("addition")
SUB= cv2.subtract(img1,img2)
plt.subplot(344)
plt.imshow(SUB,cmap='gray');plt.title("subtraction")
MUL = img1*img2
plt.subplot(345)
plt.imshow(MUL,cmap='gray');plt.title("multiplication")
div = img1/img2
plt.subplot(346)
plt.imshow(div,cmap='gray');plt.title("division")

OR = cv2.bitwise_or(img1,img2)
plt.subplot(347)
plt.imshow(OR,cmap='gray')
plt.title("bitwise or")
AND = cv2.bitwise_and(img1,img2)
plt.subplot(348)
plt.imshow(AND,cmap='gray')
plt.title("bitwise and")
XOR = cv2.bitwise_xor(img1,img2)
plt.subplot(349)
plt.imshow(XOR,cmap='gray')
plt.title("bitwise xor")
NOT = cv2.bitwise_not(img1,img2)
plt.subplot(3,4,10)
plt.imshow(NOT,cmap='gray')
plt.title("bitwise not")

 