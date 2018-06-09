# -*- coding: utf-8 -*-
"""
Created on Sat Jun  9 15:03:36 2018

@author: yatheen!
"""

import cv2 
import numpy as np
import matplotlib.pyplot as plt
import os
import time

image =cv2.imread(r"E:\Programming!\Image processing\images\8.jpg")

image = cv2.fastNlMeansDenoisingColored( image , None , 10,10,7,21)

ret , threshold =cv2.threshold(image , 127 ,255 , 0)

alteredImage, contours, hierarchy = cv2.findContours(threshold,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

cv2.imshow("Original Image" , image)
path = r"E:/Programming!/Image processing/images/Blades Images/"

image2 = cv2.drawContours(image , contours , -1 , (0,255,0), 6)
#cv2.imwrite(os.path.join(path+'Blade '+str(i)+".jpg"),image2)

cv2.imshow("Altered Image" , image2)
print("Area of the detected contour is : " , cv2.contourArea(contours[1]))
print("Arc of detected contour is : " ,cv2.arcLength(contours[1],True))


cv2.waitKey(0)
cv2.destroyAllWindows()