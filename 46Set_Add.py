n = int(input())
stamps = [input() for country in range(n)]
print(len(set(stamps)))
