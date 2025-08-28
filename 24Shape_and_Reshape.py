import numpy as np

arr = input().strip().split(" ")
myarr = np.array(list(map(int,arr)))
print (np.reshape(myarr,(3,3)))