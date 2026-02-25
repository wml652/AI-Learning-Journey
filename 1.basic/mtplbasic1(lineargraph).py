import matplotlib.pyplot as plt 
import numpy as np 

myarray = np.array([44,52,78,25,65,44,100])

print (myarray)


plt.plot(myarray)

plt.xlabel("x label values")

plt.ylabel("y label values")

plt.show()