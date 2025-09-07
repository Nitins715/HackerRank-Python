import numpy as np

poly = list(map(float,input().split()))
x = float(input())

print(np.polyval(poly,x))