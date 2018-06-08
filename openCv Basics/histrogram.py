# -*- coding: utf-8 -*-
"""
Created on Fri Jun  8 13:44:09 2018

@author: yatheen!
"""
import cv2 
import numpy as np
import matplotlib.pyplot as plt
from IPython import get_ipython # the plot is shown as a seperate screen
get_ipython().run_line_magic('matplotlib', 'qt')

image = cv2.imread(r'E:\Programming!\Image processing\images\1.jpg')

color = ('b','g','r')

for i,col in enumerate(color):
    histogram = cv2.calcHist([image], [i] ,None, [256] , [0,256])
    plt.plot(histogram,color=col)
    plt.xlim([0,1256])
    
plt.show()

