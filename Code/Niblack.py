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
### Niblack Function ###
def niblack(title,image,n=100,k=0.2):
    row,column = image.shape[:]
    newImage = image[:,:]
    w = int((n-1) / 2)
    for i in range(w+1,row-w):
        for j in range(w+1,column-w):
            block = image[i-w:i+w,j-w:j+w]
            m = np.mean(block)
            s = np.std(block)
            t = m + k*s
            if image[i,j] > t:
                newImage[i,j] = 255
            else:
                newImage[i,j] = 0
    cv2.imshow(title,newImage)      
    cv2.waitKey(0)
### Run ###
niblack('image 1', im_gray1)  
niblack('image 2', im_gray2)  
niblack('image 3', im_gray3)             