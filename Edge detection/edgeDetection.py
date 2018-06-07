# -*- coding: utf-8 -*-
"""
Created on Thu Jun  7 10:29:24 2018

@author: kmy07
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt
from IPython import get_ipython
get_ipython().run_line_magic('matplotlib', 'qt')

print("All packages Imported succesfully!")

image = cv2.imread(r"E:\MRV Project\Project 1\vp.jpg",0)

edges = cv2.Canny(image , 500,200)

plt.subplot(121)
plt.imshow(image,cmap = 'gray')
plt.title('Original Image')
plt.xticks([])
plt.yticks([])

plt.subplot(122)
plt.imshow(edges ,cmap = 'gray')
plt.title('Image with edges detected')
plt.xticks([])
plt.yticks([])

plt.show()
