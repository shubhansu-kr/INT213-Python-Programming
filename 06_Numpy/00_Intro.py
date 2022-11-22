import numpy as np

# numpy is used to create different types of array 

# mathematical operations can be used on arrays created using numpy 
# A numpy array is easy to manage memory. Allows memory adjustment 

# 1. Convert existing data structure into numpy array - eg. dictionary, list, etc
# 2. We can use predefined functions to create numpy arrays. 
# 3. We can convert any file into numpy array - eg. csv, txt, excel.

# 1. Exitsting data structure 
list1 = [12, 14, 15, 16, 26]
list2 = [32, 43, 23, 66, 44]

myNumpyArray1 = np.array(list1)
myNumpyArray2 = np.array(list2)


print (list1) # prints with ','
print (myNumpyArray1) # prints without ','
print (myNumpyArray2) # prints without ','

# Access each element of numpy array : Using index
print(myNumpyArray2[0], myNumpyArray1[1])

# dtype: Prints the type of data in array
# The memory size it is storing is as int32.
print(myNumpyArray1.dtype)

# size: Prints the size of array in numpy
print(myNumpyArray1.size)

# shape: Prints the shape of array
# Displays the rows and column of array
print(myNumpyArray1.shape)

# prints the dimensions of array, here it is 1 representing 1d
print(myNumpyArray1.ndim)

strlist = ['lets', 'learn', 'numpy']
strArray = np.array(strlist)

print()
print(strArray.dtype)
print(strArray.size)
print(strArray.ndim)
print(strArray.shape)

