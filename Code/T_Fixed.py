import cv2
###  Read  Image ###
img1=cv2.imread('Assets/image1.png')
img2=cv2.imread('Assets/image2.jpg')
img3=cv2.imread('Assets/image3.png')
### convert 2 gray ###
im_gray1=cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY)
im_gray2=cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)
im_gray3=cv2.cvtColor(img3,cv2.COLOR_BGR2GRAY)
### T_Fixed Function ###
def T_Fixed(title,image):
    row,column = image.shape[:]
    for i in range(row-1):
        for j in range(column-1):
            if image[i,j] >= 128:
                image[i,j] = 255
            else:
                image[i,j] = 0   
    cv2.imshow(title,image)
    cv2.waitKey(0)
###Run###
T_Fixed('image 1', im_gray1)
T_Fixed('image 2', im_gray2)
T_Fixed('image 3', im_gray3)