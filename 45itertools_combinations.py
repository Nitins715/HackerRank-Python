from itertools import combinations
string,size=input().split()
string=sorted(string)
size=int(size)
for i in range(1,size+1):
    for j in list(combinations(string,i)):
        print(''.join(j))
