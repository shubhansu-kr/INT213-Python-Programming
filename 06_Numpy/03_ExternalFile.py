import numpy as np

f = open("dummy.txt")
str = f.read()
print(str)

# arr = np.loadtxt(f, delimeter = " ", dtype = "int")

# print(arr)
f.close()