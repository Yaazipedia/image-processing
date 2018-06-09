# -*- coding: utf-8 -*-
"""
Created on Fri Jun  8 21:24:32 2018

@author: yatheen!
"""
import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread(r'E:\Programming!\Image processing\images\2.jpg')

brightnessMatrix = np.ones(image.shape , dtype = "uint8" ) * 100

"""To increase the brightness add the brightness matrix"""
alteredImage = cv2.add(image , brightnessMatrix)
cv2.imshow("Image Brighteness increased" , alteredImage)

"""To decrease the brightness subtract the brightness matrix"""
alteredImage = cv2.subtract(image , brightnessMatrix)
cv2.imshow("Image Brighteness decreased" , alteredImage)

cv2.waitKey()
cv2.destroyAllWindows()