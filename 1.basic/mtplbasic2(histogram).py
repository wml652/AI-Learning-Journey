import matplotlib.pyplot as plt

import numpy as np 

list = [10,20,50,68,10,30,50]

myarray = np.array(list)

plt.hist(myarray)

plt.xlabel("x label values")

plt.ylabel("y label values")

plt.show()