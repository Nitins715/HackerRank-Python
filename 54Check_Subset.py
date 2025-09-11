test_cases = int(input())
for i in range(test_cases):
    n = int(input())
    A = set(map(int,input().split()))
    m = int(input())
    B = set(map(int,input().split()))
    print(A.issubset(B))
