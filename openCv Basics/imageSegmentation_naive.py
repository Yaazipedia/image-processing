# -*- coding: utf-8 -*-
"""
Created on Sat Jun  9 16:31:50 2018

@author: kmy07
"""

import cv2 
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread(r'E:\Programming!\Image processing\images\7.jpeg')
cv2.imshow("Original Image " , image)

"""Step 2 : Convert the input image into grapyscale image
                This makes the processing faster """
image = cv2.cvtColor(image , cv2.COLOR_BGR2GRAY)
    
"""Step 3 : Gaussian blur to improvise and remove noise further """
    
image = cv2.GaussianBlur(image , (5,5) , 0)

"""Step 4 : Edge Detection """
    
alteredImage = cv2.Canny(image,255,255)
    
"""Step 5 : Invert and Binarise the Image """
    
ret , mask = cv2.threshold(alteredImage , 100 ,255 , cv2.THRESH_BINARY_INV)

#mask = cv2.fastNlMeansDenoising( mask , None , 10,10,7,21)

cv2.imshow("Altered Image " , mask)

ret , threshold =cv2.threshold(mask, 127 ,255 , 0)

alteredImage, contours, hierarchy = cv2.findContours(threshold,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

image2 = cv2.drawContours(alteredImage , contours , -1 , (0,255,0), 2)
#cv2.imwrite(os.path.join(path+'Blade '+str(i)+".jpg"),image2)

cv2.imshow("Result" , image2)

print(len(contours))

for i in range(0,len(contours)):
    Area = []
    Area.append(cv2.contourArea(contours[i]))
    
print(max(Area))
#print("Area of the detected contour is : " , cv2.contourArea(contours[1]))
#print("Arc of detected contour is : " ,cv2.arcLength(contours[1],True))

cv2.waitKey()
cv2.destroyAllWindows()