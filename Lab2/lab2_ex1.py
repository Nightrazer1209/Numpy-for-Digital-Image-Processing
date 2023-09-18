# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy

array1D_int = numpy.array([[1,2]])
array2D_int = numpy.array([[1,2,3],[4,5,6],[7,8,9]])
array1D_float = numpy.array([[1.2,3.4,5.6]])
#Create a 1x2 array
#Create a 3x3 array
#Create a 1x3 array

print (array1D_int)
print (array2D_int)
print (array1D_float)

array4x4 = numpy.array([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]])
array5x4 = numpy.array([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16],[17,18,19,20]])
array4x1 = numpy.array([[1],[2],[3],[4]])

print(array4x4.dtype)

array1D_uint8 = numpy.array([[255,256,257]],dtype=numpy.uint8)
