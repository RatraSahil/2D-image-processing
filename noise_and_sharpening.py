import cv2
import random
import numpy as np

#Salt and pepper noise can only be applied to greyscale images
img = cv2.imread('lena.png', cv2.IMREAD_GRAYSCALE)

def add_noise(img):
  
    # Getting the dimensions of the image
    row , col = np.shape(img)
      
    # Randomly pick some pixels in the image for coloring them white
    # Pick a random number between 300 and 10000
    number_of_pixels = random.randint(300, 10000)
    for i in range(number_of_pixels):
        
        # Pick a random y coordinate
        y_coord=random.randint(0, row - 1)
          
        # Pick a random x coordinate
        x_coord=random.randint(0, col - 1)
          
        # Color that pixel to white
        img[y_coord][x_coord] = 255
          
    # Randomly pick some pixels in
    # the image for coloring them black
    # Pick a random number between 300 and 10000
    number_of_pixels = random.randint(300 , 10000)
    for i in range(number_of_pixels):
        
        # Pick a random y coordinate
        y_coord=random.randint(0, row - 1)
          
        # Pick a random x coordinate
        x_coord=random.randint(0, col - 1)
          
        # Color that pixel to black
        img[y_coord][x_coord] = 0
          
    return img
  

#Storing the image
cv2.imwrite('salt-and-pepper-lena.png', add_noise(img))

#Apply smoothing to the image
avging = cv2.blur(img,(7,7))
cv2.imshow('Image with noise',img)   
cv2.imshow('Averaging',avging)
# Gaussian Blurring
# Again, you can change the kernel size
gausBlur = cv2.GaussianBlur(img, (7,7),0) 
medBlur = cv2.medianBlur(img,5)

cv2.imshow('Median Blurring', medBlur)
cv2.imshow('Gaussian Blurring', gausBlur)
cv2.waitKey(0)
cv2.destroyAllWindows()