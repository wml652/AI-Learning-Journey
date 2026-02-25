import numpy as np 

import pandas as pd 


list = [1,2,3]

array1 = np.array(list)

sorting = ['a','b','c']

series1 = pd.Series(array1,index = sorting)

print(series1)


print(series1[2])