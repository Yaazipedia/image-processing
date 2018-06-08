# -*- coding: utf-8 -*-
"""
Created on Fri Jun  8 13:30:12 2018

@author: yatheen!
"""
import cv2 
import numpy as np

image = cv2.imread('D:\Pictures\Camera Roll\WIN_20180503_11_52_56_Pro.jpg',0)

cv2.imshow('First Image' , image)

cv2.waitKey(0)
cv2.destroyAllWindows()
