# -*- coding: utf-8 -*-
"""
Created on Fri Jun  8 19:33:15 2018

@author: yatheen!
"""

import cv2 
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread(r'E:\Programming!\Image processing\images\2.jpg')
cv2.imshow("Original Image " , image)
height , width = image.shape[:2]

"""Translation"""
translationMatrix = np.float32([[1,0,54],[0,1,54]])
translatedImage = cv2.warpAffine( image , translationMatrix , (width,height))
cv2.imshow("Translated Image",translatedImage)

"""Rotation"""
rotationMatrix = cv2.getRotationMatrix2D((width/2,height/2),180,1)
rotatedImage = cv2.warpAffine( image , rotationMatrix , (width,height))
cv2.imshow("Rotated Image",rotatedImage)

"""Resizing"""
resizedImage = cv2.resize(image , None , fx =2 ,fy =2 ,interpolation = cv2.INTER_CUBIC)
cv2.imshow("Resized Image" , resizedImage)

"""Usage of image pyramids"""

smaller = cv2.pyrDown(image)
larger = cv2.pyrUp(image)
cv2.imshow('Smaller Image' , smaller)
cv2.imshow('Larger Image' , larger)

"""Cropping the Image """

start_row , start_col = int(height * 0.15) , int(width * 0.15)
end_row , end_col = int(height * 0.75) , int(width * 0.75)

cropped_image = image[start_row:end_row , start_col:end_col]

cv2.imshow("Cropped Image" , cropped_image)

cv2.waitKey()
cv2.destroyAllWindows()