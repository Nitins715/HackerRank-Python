from collections import OrderedDict

n = int(input())
od=OrderedDict()
for _ in range(n):
    line=input().split()
    item,price=' '.join(line[:-1]),int(line[-1])
    od[item]=od.get(item, 0)+int(price)

for item,price in od.items():
    print(item,price)