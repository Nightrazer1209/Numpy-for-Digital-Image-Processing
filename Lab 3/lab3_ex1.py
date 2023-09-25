# -*- coding: utf-8 -*-
"""
Created on Mon Sep 25 10:10:03 2023

@author: Eddy
"""
import numpy as np
import cv2 
cman = cv2.imread('cameraman.bmp',0)
boat = cv2.imread('boat.bmp',0)

cman_f64 = cman.astype(np.float64)
boat_f64 = boat.astype(np.float64)

boatman = boat_f64 + cman_f64
cv2.imshow('Boatman Float', boatman)
cv2.waitKey()
max_value = boatman.max()
scl_boatman = (boatman / max_value)*255
scl_boatman = scl_boatman.astype(np.uint8)
cv2.imshow('Scl. Boatman Uint8', scl_boatman)


cv2.waitKey()
cv2.destroyAllWindows()

