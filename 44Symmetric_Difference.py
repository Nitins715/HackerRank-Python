_ = input()
m = set(map(int, input().split()))
_ = input()
n = set(map(int, input().split()))

for num in sorted(list(m.symmetric_difference(n))):
    print(num)