# -*- coding: utf-8 -*-
"""
Created on Mon Sep 25 10:10:03 2023

@author: Eddy
"""
import numpy as np
import cv2
dice1 = cv2.imread('dice1.png',1)
dice2 = cv2.imread('dice2.png',1)

dice1_f64 = dice1.astype(np.float64)
dice2_f64 = dice2.astype(np.float64)

dice_diff = dice1_f64 - dice2_f64 
cv2.waitKey()
max_value = dice_diff.max()
scl_dice = (dice_diff / max_value)*255
scl_dice = scl_dice.astype(np.uint8)
cv2.imshow('Scl. dice Uint8', scl_dice)


cv2.waitKey()
cv2.destroyAllWindows()

