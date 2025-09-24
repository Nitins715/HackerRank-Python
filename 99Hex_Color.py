import re
for _ in range(int(input())):
    line = input()
    pattern = re.compile(r'(?<=[\s:])#(?:[a-fA-F0-9]{6}|[a-fA-F0-9]{3})')
    for m in pattern.findall(line):
        print(m)