import matplotlib.pyplot as plt
import numpy as np 

x = np.array([3, 5, 6, 7, 23, 64])


# plot is used to create a iine graph, takes a numpy array or list as 
# input args and marker specifies the type of point and linestyle 
# specifies the type of line eg. solid or dotted. 

# here both x and y axis is same ie x
plt.plot(x, marker = '.', linestyle = 'dotted')
plt.show()

y = np.array([46, 72, 50, 14, 10, 21])
plt.xlabel ('x-axis')
plt.ylabel ('y-axis')

# specifies the x as well as y coordinate of each 
plt.plot(x, y)
plt.show()