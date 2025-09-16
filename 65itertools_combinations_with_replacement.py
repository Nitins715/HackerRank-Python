from itertools import combinations_with_replacement
s,n = input().split()

for combo in combinations_with_replacement(sorted(list(s)),int(n)):
    print(("").join(combo))