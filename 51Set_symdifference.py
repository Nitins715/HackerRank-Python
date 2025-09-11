int(input())
A = set(map(int,input().split()))
int(input())
B = set(map(int,input().split()))

print(len(A.symmetric_difference(B)))
