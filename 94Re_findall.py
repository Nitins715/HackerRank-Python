import re

pattern = r'(?=[^aeiouAEIOU]([aeiouAEIOU]{2,})[^aeiouAEIOU])'
s = input()
matches = re.findall(pattern, s)

if matches:
    for match in matches:
        print(match)
else:
    print(-1)
