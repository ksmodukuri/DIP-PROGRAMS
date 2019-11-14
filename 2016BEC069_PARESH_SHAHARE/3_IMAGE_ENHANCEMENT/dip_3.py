"""
@author: Paresh Shahare
"""
# Program 1 : Applying thresholding without using opencv function
import cv2
import matplotlib.pyplot as plt

img = cv2.imread('lena5.jpg')
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
plt.imshow(gray)
cv2.imshow("Gray_original",gray)
gray_=gray[:]
cv2.imwrite('2_gray.jpg',gray)
for i in range(512):
    for j in range(512):
        k=gray_[i][j]
        if k<128:
            gray_[i][j]=0
        elif k>127 and k<256:
            gray_[i][j]=255
cv2.imwrite('Quantized_2_gray.jpg',gray_)
cv2.imshow("Gray_histogram",gray_)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Program 2 : Applying multiple thresholding on grayscale image without using function
import cv2
import matplotlib.pyplot as plt

img1 = cv2.imread('lena5.jpg')
gray1=cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY)
plt.imshow(gray1)
cv2.imshow("Gray_original",gray1)
cv2.imwrite('gray.jpg',gray1)
gray_1=gray1[:]
for i in range(512):
    for j in range(512):
        k=gray_1[i][j]
        if k<64:
            gray_1[i][j]=0
        elif k>63 and k<128:
            gray_1[i][j]=80
        elif k>127 and k<194:
            gray_1[i][j]=160
        elif k>193 and k<256:
            gray_1[i][j]=255
cv2.imwrite('Quantized_image.jpg',gray_1)
cv2.imshow("Gray_histogram",gray_1)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Program 3 : 
import cv2
import matplotlib.pyplot as plt

img2 = cv2.imread('pout.jfif')
gray2=cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)
plt.imshow(gray2)
cv2.imshow("Gray_original",gray2)
gray_2=gray2[:]
for i in range(247):
    for j in range(204):
        k=gray_2[i][j]
        if k<101:
            gray_2[i][j]*=0.5
        elif k>100 and k<201:
            gray_2[i][j]=gray_[i][j]*1.5-100
cv2.imwrite('pout_image.jpg',gray_2)
cv2.imshow("pout_histogram",gray_2)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imshow("Gray_original_1",gray)
cv2.imshow("Gray_histogram_1",gray_)
cv2.imshow("Gray_original_2",gray1)
cv2.imshow("Gray_histogram_2",gray_1)
cv2.imshow("Gray_original_3",gray2)
cv2.imshow("pout_histogram_3",gray_2)
cv2.waitKey(0)
cv2.destroyAllWindows()
