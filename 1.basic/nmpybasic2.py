import numpy as np 


##basic opeartions on numpy arrays 



mylist = [[1,2,3],[44,52,78]]
mylist2 = [[1,2,3],[44,52,78]]

print(mylist)

myarray = np.array(mylist)
 
print(myarray)

print(myarray.shape)


print("Tthe first row = %s" %myarray[0])
print("The last row = %s" %myarray[1])

print ("Specific column : %s " %myarray[:,1])



#basic arithematics on numpy 


myarray= np.array(mylist)
myarray2 = np.array(mylist2)

print(myarray)
print(myarray2)


print("Addition : %s"  %(myarray+myarray2))

print("Multiplication : %s" %(myarray*myarray2))


