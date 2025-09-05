import numpy as np

n,m = map(int, input().split())
val = np.array([list(map(int, input().split())) for i in range(n)])

print(np.prod(np.sum(val, axis=0)))