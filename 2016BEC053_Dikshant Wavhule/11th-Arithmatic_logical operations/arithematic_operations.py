import cv2
import matplotlib.pyplot as plt

img1 = cv2.imread("black1.png",0)
plt.subplot(341)
plt.imshow(img1,cmap='gray')
plt.title("1")
img2 = cv2.imread("sample.png",0)
plt.subplot(342)
plt.imshow(img2,cmap='gray')
plt.title("2")
img3 = cv2.imread("white.png",0)
plt.subplot(343)
plt.imshow(img3,cmap='gray')
plt.title("3")
add = img1+img2
plt.subplot(345)
plt.imshow(add,cmap='gray') 
plt.title("addition 1+2")

sub = img2 - img3
plt.subplot(346)
plt.imshow(sub,cmap='gray')
plt.title("subtraction 2-3")

mul = img2*img3
plt.subplot(347)
plt.imshow(mul,cmap='gray')
plt.title("multiplication 2*3")


div = img2/img3
plt.subplot(348)
plt.imshow(div,cmap='gray')
plt.title("division 2/3")

orr = cv2.bitwise_or(img1,img2)
plt.subplot(349)
plt.imshow(orr,cmap='gray')
plt.title("bitwise or 1 2")

aand = cv2.bitwise_and(img3,img2)
plt.subplot(3,4,10)
plt.imshow(aand,cmap='gray')
plt.title("bitwise and 3 2")

xor = cv2.bitwise_xor(img3,img2)
plt.subplot(3,4,11)
plt.imshow(xor,cmap='gray')
plt.title("bitwise xor 3 2")

notn = cv2.bitwise_not(img2)
plt.subplot(3,4,12)
plt.imshow(notn,cmap='gray')
plt.title("bitwise not 2")