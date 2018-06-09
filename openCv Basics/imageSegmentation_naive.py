# -*- coding: utf-8 -*-
"""
Created on Sat Jun  9 16:31:50 2018

@author: kmy07
"""

import cv2 
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread(r'E:\Programming!\Image processing\images\4.png')
cv2.imshow("Original Image " , image)

"""Step 2 : Convert the input image into grapyscale image
                This makes the processing faster """
image = cv2.cvtColor(image , cv2.COLOR_BGR2GRAY)
    
"""Step 3 : Gaussian blur to improvise and remove noise further """
    
image = cv2.GaussianBlur(image , (5,5) , 0)

"""Step 4 : Edge Detection """
    
alteredImage = cv2.Canny(image,10,70)
    
"""Step 5 : Invert and Binarise the Image """
    
ret , mask = cv2.threshold(alteredImage , 100 ,255 , cv2.THRESH_BINARY_INV)


cv2.imshow("Altered Image " , mask)

result = cv2.subtract(image , mask)

print(result.shape)

cv2.imshow("Result" , result)

cv2.waitKey()
cv2.destroyAllWindows()