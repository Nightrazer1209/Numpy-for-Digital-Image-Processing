# -*- coding: utf-8 -*-
"""
Created on Mon Sep 25 10:10:03 2023

@author: Eddy
"""
import numpy as np
import cv2 as cv
ufo = cv.imread('Lab3_images/ufo.bmp',cv.IMREAD_GRAYSCALE)
    
ufo_c=ufo*15
cv.imwrite('Lab3_images/baboon.bmp',ufo_c)
cv.imshow('baboon',ufo_c)


cv.waitKey(0)
cv.destroyAllWindows()

