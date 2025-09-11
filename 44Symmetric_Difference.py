_ = input()
m = set(map(int, input().split()))
_ = input()
n = set(map(int, input().split()))

for num in sorted(list((m.difference(n).union(n.difference(m))))):
    print(num)