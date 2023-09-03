# Numpy 1D Arrays
import numpy as np

#  Create a numpy array
np_array = np.array ([1,2,3,4,5])

# Print the type
print (type (np_array)) # <class 'numpy.ndarray'>

# Print the values
print (np_array) # [1 2 3 4 5]

# The values in np_array are same type so We can use dtype method
print (np_array.dtype) # int32

# size. Check how many items in the array
print (np_array.size) # 5

# ndim.
print (np_array.ndim) # 1

# shape. The attribute "shape” is a tuple of integers indicating the size of the array in each dimension.
print (np_array.shape) # (5,)

### Create a NumPy float array
np_array_float = np.array ([11.5,2.0,23.87,4.132,509.232,3454.232])
print (type(np_array_float)) # <class 'numpy.ndarray'>
print (np_array_float.dtype) # float64
print (np_array_float) # [1.150000e+01 2.000000e+00 2.387000e+01 4.132000e+00 5.092320e+02 3.454232e+03]

# slice 
print (np_array_float[0:3]) # [11.5   2.   23.87]
print (np_array_float[::2]) # [ 11.5    23.87  509.232]
