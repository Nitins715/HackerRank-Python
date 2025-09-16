from itertools import product
K,M = map(int,input().split())
K_lists_squared=[[int(x)**2 for x in input().split()[1:]] for _ in range(K)]
max_val = max([(sum(t)%M) for t in product(*K_lists_squared)])
print(max_val)