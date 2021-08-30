import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt
img = cv.imread('img1.png',0)
edges = cv.Canny(img,100,200)
plt.subplot(121),plt.imshow(img,cmap = 'gray')
plt.title('Original Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(edges,cmap = 'gray')
plt.title('Edge Image'), plt.xticks([]), plt.yticks([])
plt.show()

ddepth = cv.CV_16S
kernel_size = 3
window_name = "Laplace edge detection"
    # [variables]
    # [load]
src = cv.imread('img1.png', cv.IMREAD_COLOR) # Load an image
    # Check if image is loaded fine
if src is None:
    print ('Error opening image')
    print ('Program Arguments: [image_name -- default lena.jpg]')
    # [load]
    # [reduce_noise]
    # Remove noise by blurring with a Gaussian filter
src = cv.GaussianBlur(src, (3, 3), 0)
    # [reduce_noise]
    # [convert_to_gray]
    # Convert the image to grayscale
src_gray = cv.cvtColor(src, cv.COLOR_BGR2GRAY)
    # [convert_to_gray]
    # Create Window
cv.namedWindow(window_name, cv.WINDOW_AUTOSIZE)
    # [laplacian]
    # Apply Laplace function
dst = cv.Laplacian(src_gray, ddepth, ksize=kernel_size)
    # [laplacian]
    # [convert]
    # converting back to uint8
abs_dst = cv.convertScaleAbs(dst)
    # [convert]
    # [display]
cv.imshow(window_name, abs_dst)
cv.waitKey(0)