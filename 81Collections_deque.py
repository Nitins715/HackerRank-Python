from collections import deque
    
d = deque()    
n = int(input())

for _ in range(n):
    op, *args = input().split()
    getattr(d, op)(*args)

print(*d)
