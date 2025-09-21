from collections import namedtuple
n, marks = int(input()), namedtuple("marks",input().split())
print(round(sum([int(marks(*input().split()).MARKS) for _ in range(n)])/n,2))
