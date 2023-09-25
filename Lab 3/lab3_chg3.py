# -*- coding: utf-8 -*-
"""
Created on Mon Sep 25 19:51:30 2023

@author: Eddy
"""

import cv2 as cv
import numpy as np
cbaboon = cv.imread('Lab3_images/baboon.bmp',0)

mask = np.zeros((512,512),dtype=np.uint8)
mask[64:512-64,64:512-64] = 255

bitand_cbaboon = cv.bitwise_and(cbaboon, mask)
cv.imshow('Masked baboon', bitand_cbaboon)
cv.waitKey(0)