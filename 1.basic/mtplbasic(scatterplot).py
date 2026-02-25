import matplotlib.pyplot as plt 

import numpy as np 

list = [10,40,70,44,77,33,66,88]

list2 = [12,55,70,32,21,43,43,21]


x = np.array(list)

y = np.array(list2)
 
plt.scatter(x,y)

plt.xlabel("x label values")

plt.ylabel("y label values")

plt.show()