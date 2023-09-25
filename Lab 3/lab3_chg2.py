# -*- coding: utf-8 -*-
"""
Created on Mon Sep 25 10:10:03 2023

@author: Eddy
"""
import numpy as np
import cv2
ufo = cv2.imread('ufo.bmp',1)

ufo_f64 = ufo.astype(np.float64)

ufo_f64 = ufo_f64 * 15

cv2.imwrite('baboon.bmp',ufo_f64)
cv2.imshow('baboon',ufo_f64)


cv2.waitKey()
cv2.destroyAllWindows()

