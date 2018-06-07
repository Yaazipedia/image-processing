# -*- coding: utf-8 -*-
"""
Created on Thu Jun  7 10:29:24 2018

@author: yatheen!
"""
"""Step 1: Import the neccessary Packages """
import cv2  #OpenCv to handle and process the images
import numpy as np #Images are stores as numpy arrays
import matplotlib.pyplot as plt # to plot the image we have to use matplotlib

#----------------------------------------------------------------------------------------------#

""" To display the result in a seperate Screen, use the following code (Optional) """
from IPython import get_ipython # the plot is shown as a seperate screen
get_ipython().run_line_magic('matplotlib', 'qt') # use Ipython package to make the run_line_magic function 

print("All packages Imported succesfully!") #jus a check

#----------------------------------------------------------------------------------------------#

"""Step 3: Read the image input """

image = cv2.imread(r"E:\Image processing\Edge detection\vp.jpg",0) # get the image as input

"""
The second argument in the image determines how the input is readed
0 ---> the image is read as grayscale image
1 ---> the image is read as color image """

#image = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY) if color image is read as input , change it to grayscale

#----------------------------------------------------------------------------------------------#

"""Step 4 : Detect the egdes using Canny Shape Descriptor """

edges = cv2.Canny(image , 300,200) #Canny shape descriptor is used to identify the edges.

#----------------------------------------------------------------------------------------------#

"""Step 5: Plot the result """

plt.subplot(121) #121 is the index of the plot of the original image 
plt.imshow(image,cmap = 'gray')
plt.title('Original Image')
plt.xticks([])
plt.yticks([])

plt.subplot(122)
plt.imshow(edges ,cmap = 'gray')
plt.title('Image with edges detected')
plt.xticks([]) #Get or set the x-limits of the current tick locations and labels.
plt.yticks([]) #Get or set the y-limits of the current tick locations and labels.

plt.show() # Display the plot

#----------------------------------------------------------------------------------------------#