import numpy as np 

import pandas as pd 

list = [[1,2,3,4],[3,7,5,20]]

print(list)


myarray = np.array(list)

print(myarray)

rowname = ['a','b']

columnname = ['one','two','three','four']


mydataframe = pd.DataFrame(myarray, index = rowname , columns=columnname)

print(mydataframe)

print(mydataframe.two)

print(mydataframe['two']['a'])
