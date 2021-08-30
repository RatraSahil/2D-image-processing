import cv2 as cv
import numpy as np

img=cv.imread('messi.png')

#read the template and convert it into grayscale at the same time
template=cv.imread('template.png', cv.IMREAD_GRAYSCALE)

#convert the image into grayscale
img_gray=cv.cvtColor(img, cv.COLOR_BGR2GRAY)

#now, there are different methods to do template matching, here we will see one that generally works best
result=cv.matchTemplate(img_gray, template, cv.TM_CCOEFF_NORMED)

#now we need to locate the place where our template matches with the image
#threshold ranges from 0-1, with 1 indicating brightest spot
loc=np.where(result >=0.88)

w, h=template.shape[::-1] #-1 is just reversing the order coz w=columns and h=rows

for pt in zip(*loc[::-1]):
    cv.rectangle(img, pt, (pt[0]+w, pt[1]+w), (0,255,0),1)

cv.imshow("img",img)
cv.imshow("Result",result)
cv.waitKey(0)
cv.destroyAllWindows()