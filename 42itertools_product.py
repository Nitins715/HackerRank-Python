from itertools import product

lists=[list(map(int,input().split())) for _ in range(2)]

print(*product(lists[0],lists[1]))
