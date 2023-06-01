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
### Otsu Function ###
def otsu(title,image):
    pixel_number = image.shape[0] * image.shape[1]
    mean_weigth = 1/pixel_number
    his, bins = np.histogram(image, np.array(range(0, 255)))
    final_thresh = 128
    final_value = 0
    for i in bins[:]:
        Wb = np.sum(his[:i]) * mean_weigth
        Wf = np.sum(his[i:]) * mean_weigth
        mub = np.mean(his[:i])
        muf = np.mean(his[i:])
        value = Wb * Wf * (mub - muf) ** 2
        print("Wb = ", Wb, " Wf = ", Wf)
        print("i = ", i, " value = ", value)
        if value > final_value:
            final_thresh = i
            final_value = value
    newImage = image.copy()
    print(final_thresh)
    newImage[image > final_thresh] = 255
    newImage[image < final_thresh] = 0
    cv2.imshow(title,newImage)
    cv2.waitKey(0)
### Run ###
otsu('image 1', im_gray1)    
otsu('image 2', im_gray2)  
otsu('image 3', im_gray3)  