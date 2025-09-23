import re
s = input()
k = input()

pattern = fr"(?=({k}))"
matches = re.finditer(pattern, s)
matches_list = list(matches)
if matches_list:
    for m in matches_list:
        print((m.start(1), m.end(1)-1))
else:
    print((-1, -1))