import numpy as np

n,m,p = map(int,input().split())
ar1 = np.array([input().split() for i in range(n)], int)
ar2 = np.array([input().split() for i in range(m)], int)

print(np.concatenate((ar1,ar2), axis=0))