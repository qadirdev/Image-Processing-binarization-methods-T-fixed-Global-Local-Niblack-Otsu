import numpy as np
import cv2
###  Read  Image ###
img1=cv2.imread('Assets/image1.png')
img2=cv2.imread('Assets/image2.jpg')
img3=cv2.imread('Assets/image3.png')
### convert 2 gray ###
im_gray1=cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY)
im_gray2=cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)
im_gray3=cv2.cvtColor(img3,cv2.COLOR_BGR2GRAY)
### Global iterative Function ###
def local_iterative(title,image,n,constant=2):
    row, column = image.shape[:]
    newImage = image[:,:]
    binary = np.zeros((row, column), dtype=np.uint8)
    for i in range(row):
        for j in range(column):
            block = image[max(i-n//2, 0):min(i+n//2+1, row), max(j-n//2, 0):min(j+n//2+1, column)]
            t = np.mean(block) - constant
            if image[i, j] > t:
                newImage[i, j] = 255
    cv2.imshow(title, newImage)
    cv2.waitKey(0)
### Run ###
local_iterative('image 1',im_gray1 , 25)    
local_iterative('image 2',im_gray2 , 25)   
local_iterative('image 3',im_gray3 , 25)   
local_iterative('image 1',im_gray1 , 35)   
local_iterative('image 2',im_gray2 , 35)
local_iterative('image 3',im_gray3 , 35)
local_iterative('image 1',im_gray1 , 45)
local_iterative('image 2',im_gray2 , 45)
local_iterative('image 3',im_gray3 , 45)