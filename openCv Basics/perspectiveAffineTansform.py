# -*- coding: utf-8 -*-
"""
Created on Sat Jun  9 09:22:05 2018

@author: yatheen!
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt

from IPython import get_ipython # the plot is shown as a seperate screen
get_ipython().run_line_magic('matplotlib', 'qt')

image = cv2.imread(r'E:\Programming!\Image processing\images\5.jpg')
#image = cv2.resize(image , None , fx =0.25 ,fy =0.25 ,interpolation = cv2.INTER_CUBIC)
cv2.imshow("Original Image " , image)
rows, cols , ch = image.shape

point_A= np.float32([[320,15],[700,215],[85,610],[530,780]])
point_B= np.float32([[0,0],[420,0],[0,594],[420,594]])

pMatrix = cv2.getPerspectiveTransform(point_A,point_B)

alteredImage = cv2.warpPerspective(image , pMatrix , (420,594))

cv2.imshow("Altered Image " , alteredImage)
cv2.waitKey()
cv2.destroyAllWindows()