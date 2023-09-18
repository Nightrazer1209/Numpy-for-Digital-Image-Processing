# -*- coding: utf-8 -*-
"""
Created on Mon Sep 18 17:29:43 2023

@author: Eddy
"""

import numpy as np
#8 = stop value of an array 
my_array = np.arange(8)
#start from 1, ends at 8
my_array = np.arange(1,8)
#start from 1, ends 8 and jump 2 (odd)
my_array = np.arange(1,8,2)
#determine data type with number of bits
new_array = np.array([1,2,3],dtype=np.int8)


print(my_array)
print(type(my_array))

#2d array

#1) create two rows with arange
array_2d = np.array((np.arange(0,8,2),np.arange(1,8,2)))
print(array_2d)
print("2d shape: " ,array_2d.shape)
print("1d shape: ",my_array.shape)

#transform an array
array_2d_trans = array_2d.reshape((4,2))

#empty arrays
empty_array = np.zeros((2,2))

#eye_array: only diagonal
#k: position of diagonal
eye_array = np.eye(10,k=-1)
#change values within eye array
eye_array[eye_array == 0] = 2


#rows
eye_array[2] = 3
#first two rows
eye_array[:2] = 3
print(eye_array)

#columns
#first column
eye_array[:,0] = 4
#last column
eye_array[:,-1] = 5
#2nd column 3rd row
eye_array[2:3,3:4] = 6

#sorting arrays(from lowest to highest)
#horizontally
sorted_array_hor = np.sort(eye_array,1)
#vertically
sorted_array_ver = np.sort(eye_array,0)

#.view() = create copy that changes with ori
#.copy() = create copy tat dun affect ori
