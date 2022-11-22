import matplotlib.pyplot as plt
import numpy as np 

x = np.array([3, 5, 6, 7, 23, 64])

# here both x and y axis is same ie x
plt.bar(x, height=1)
plt.show()

y = np.array([46, 72, 50, 14, 10, 21])
plt.xlabel ('x-axis')
plt.ylabel ('y-axis')

# specifies the x as well as y coordinate of each 
plt.bar(x, y)
plt.show()