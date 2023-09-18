# -*- coding: utf-8 -*-
"""
Created on Mon Sep 18 10:48:20 2023

@author: Eddy
"""

import numpy as np
array4x4a = np.array([[1,2,3,4],[5,6,7,8]])
array4x4b = np.array([[9,10,11,12],[13,14,15,16]])
array1x4 = np.array([[2,0,1,4]])


conct_arr = np.concatenate((array4x4a,array1x4,array4x4b),0)
print(conct_arr)