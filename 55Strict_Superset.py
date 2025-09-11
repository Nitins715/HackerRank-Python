A = set(map(int,input().split()))
n = int(input())
res = True
for _ in range(n):
    temp = set(map(int,input().split()))
    if not(A > temp):
        res = False
        break 
print(res)    
