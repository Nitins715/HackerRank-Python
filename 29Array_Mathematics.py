import numpy as np

n,m = map(int,input().split())
A = [list(map(int, input().split())) for _ in range(n)]
B = [list(map(int, input().split())) for _ in range(n)]
a = np.array(A) 
b = np.array(B)

print(a+b,a-b,a*b,a//b,a%b,a**b,sep="\n")