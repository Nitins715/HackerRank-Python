map(int,input().split())
n = map(int,input().split())
A = set(map(int,input().split()))
B = set(map(int,input().split()))

like = 0
for i in n:
    if i in A:
        like += 1
    elif i in B:
        like -=1

print(like)