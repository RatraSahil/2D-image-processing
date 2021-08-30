import cv2
import numpy as np

img = cv2.imread('lena.png')
   
# make sure that you have saved it in the same folder
# Averaging
# You can change the kernel size as you want
avging = cv2.blur(img,(7,7))
cv2.imshow('Original image',img)   
cv2.imshow('Averaging',avging)
# Gaussian Blurring
# Again, you can change the kernel size
gausBlur = cv2.GaussianBlur(img, (7,7),0) 
medBlur = cv2.medianBlur(img,5)
#Sharpening the image
sharp=cv2.addWeighted(gausBlur, 1.85, img, -0.70, 0, img)
cv2.imshow('Median Blurring', medBlur)
cv2.imshow('Gaussian Blurring', gausBlur)
cv2.imshow('Sharpened image', sharp)
cv2.waitKey(0)
cv2.destroyAllWindows()