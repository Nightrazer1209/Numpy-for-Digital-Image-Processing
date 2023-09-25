# -*- coding: utf-8 -*-
"""
Created on Mon Sep 25 10:10:03 2023

@author: Eddy
"""
import numpy as np
import cv2
word1 = cv2.imread('word1.bmp',1)
word2 = cv2.imread('word2.bmp',1)
word3 = cv2.imread('word3.bmp',1)

word1_f64 = word1.astype(np.float64)
word2_f64 = word2.astype(np.float64)
word3_f64 = word3.astype(np.float64)

sunway = word1_f64 + word2_f64 + word3_f64
cv2.waitKey()
max_value = sunway.max()
scl_sunway = (sunway / max_value)*255
scl_sunway = scl_sunway.astype(np.uint8)
cv2.imshow('Scl. sunway Uint8', scl_sunway)


cv2.waitKey()
cv2.destroyAllWindows()

