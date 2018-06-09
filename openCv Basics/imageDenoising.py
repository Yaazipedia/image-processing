# -*- coding: utf-8 -*-
"""
Created on Sat Jun  9 08:43:47 2018

@author: kmy07
"""

import cv2 
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread(r'E:\Programming!\Image processing\images\4.png')
cv2.imshow("Original Image " , image)

image = cv2.fastNlMeansDenoisingColored( image , None , 10,10,7,21)
cv2.imshow("Altered Image " , image)

cv2.waitKey()
cv2.destroyAllWindows()