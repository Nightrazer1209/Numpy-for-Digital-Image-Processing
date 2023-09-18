# -*- coding: utf-8 -*-
"""
Created on Mon Sep 18 18:02:48 2023

@author: Eddy
"""

import numpy as np

array = np.zeros([200,200])
#start from cols and rows all = 100
array[0:,0:] = 100

#alternative
array.fill(100)