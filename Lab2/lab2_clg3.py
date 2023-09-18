# -*- coding: utf-8 -*-
"""
Created on Mon Sep 18 18:10:44 2023

@author: Eddy
"""

import numpy as np

new_array = np.zeros([7,7])
k=1
for i in range (0,7,2):
    for j in range (0,7,2):
        new_array[i,j]=k
        k+=1
    