from itertools import combinations

length = int(input())
s = input().split()
k = int(input())
count = 0
for tup in combinations(s,k):
    if any(elem == 'a' for elem in tup):
        count += 1

print(count / len(list(combinations(s,k))))
