# -*- coding: utf-8 -*-
"""
Created on Fri Jun  8 14:00:29 2018

@author: kmy07
"""

import cv2 
import matplotlib.pyplot as plt
import numpy as np

blackScreen = np.zeros((512,1000,3) , dtype = np.uint8 )

cv2.line(blackScreen , pt1 = (10,0) , pt2 = (150,64) , color = (255,127,0) , thickness = 5 )

cv2.rectangle(blackScreen , pt1 = (130,0) , pt2 = (150,64) , color = (255,120,0) , thickness = 5 )

cv2.rectangle(blackScreen , pt1 = (120,20) , pt2 = (150,64) , color = (255,227,0) , thickness = 5 )


cv2.imshow("Blue Line" , blackScreen )

cv2.waitKey()
cv2.destroyAllWindows()