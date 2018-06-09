# -*- coding: utf-8 -*-
"""
Created on Fri Jun  8 23:01:31 2018

@author: kmy07
"""

import cv2 
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread(r'E:\Programming!\Image processing\images\3.jpg')
image = cv2.resize(image , None , fx =0.25 ,fy =0.25 ,interpolation = cv2.INTER_CUBIC)
cv2.imshow("Original Image " , image)

"""Type 1: filter 2d method """
#determine the kernel to perform convolution
#blurring is a effect of convolution

kernel_7x7 = np.ones((7,7), np.float32) / 49
#kernel_3x3 = np.ones((3,3), np.float32) / 9 --> other choices

blurredImage = cv2.filter2D(image , -1 , kernel_7x7)
cv2.imshow("Blurred Image " , blurredImage )

"""Type 2 : normal Blur method """
blurImage = cv2.blur(image , (9,9))
cv2.imshow("Normal Blur Image " , blurImage )

"""Type 3 : gaussian Blur method """
blurImage = cv2.GaussianBlur(image , (9,9) , 0)
cv2.imshow("Gaussian Blur Image " , blurImage )

"""Type 4 : normal Blur method """
blurImage = cv2.medianBlur(image , 7)
cv2.imshow("Median Blur Image " , blurImage )

"""Type 5 : Bilateral Blur method """
blurImage = cv2.bilateralFilter(image , 9 , 75 , 75)
cv2.imshow("Bilateral Blur Image " , blurImage )

cv2.waitKey()
cv2.destroyAllWindows()