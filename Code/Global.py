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
def global_iterative(title,image):
    row,column = image.shape[:]
    newImage = image[:,:]
    t0,t=128,128
    g1 = []
    g2 = []
    while(1):
        for i in range(row):
            for j in range(column):
                if (image[i,j] < t):
                    g1.append(image[i,j])
                else:
                    g2.append(image[i,j])
        mu1 = sum(g1) / len(g1)
        mu2 = sum(g2) / len(g2)
        t0=t
        t = ((mu1+ mu2)/2)
        delta_t = abs(t-t0)
        if(delta_t < 0.1):
           break
    print('value of T = ','\t','delta_t = ',delta_t)    
    hist_full = cv2.calcHist([image],[0],None,[256],[0,256])
    #apply thresholding
    for i in range(row):
        for j in range(column):
            if (image[i,j] < t):                
                newImage[i,j] = 0
            else:
                newImage[i,j] = 225
    cv2.imshow(title,newImage)
    cv2.waitKey(0)            
###Run###  
global_iterative('image 1', im_gray1)
global_iterative('image 2', im_gray2)
global_iterative('image 3', im_gray3)