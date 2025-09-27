import re

n,m = map(int,input().rstrip().split())

matrix = [input() for _ in range(n)]
    
result = "".join(row[no] for no in range(m) for row in matrix)

result = re.sub(r'(?<=[A-Za-z0-9])[^A-Za-z0-9]+(?=[A-Za-z0-9])',' ',result)
print(result)