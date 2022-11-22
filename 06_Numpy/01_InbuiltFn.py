# Creating default numpy arrays 

import numpy as np 

# Zeroes : Create a numpy array of m, n shape with all zeroes 
z = np.zeros((2, 5)) 
print (z)

# Ones: Create a numpy array of m, n shape with all ones 
z = np.ones((4, 4))
print(z)

# Full : Create a numpy array of m, n shape with all values equal to x
z = np.full((3, 4), 21)
print(z)

# Arange : Creates an array with elements 0 to x where x is excluded. 
z = np.arange(15)
print(z)

# Linspace: Creates an array within range [a, b] both inclusive with x 
# equal partition
z = np.linspace(1, 5, 12)

# Identity : Create an identity matriz of size x
z = np.identity(4)
print(z)

x = [[1,2,3], [4,5,6], [7,8,9]]
z = np.array(x)

print(z)

# axis zero gives column sum 
s1 = z.sum(axis=0)
print(s1)

# axis one gives row sum
s2 = z.sum(axis=1)
print(s2)

