from collections import defaultdict
m,n = input().split()
d=defaultdict(list)
for i in range(1,int(m)+1):
    a = input()
    d[a].append(i)

for _ in range (int(n)):
    b = input()
    
    if b in d:
        print(*d[b])
    else:
        print('-1')
