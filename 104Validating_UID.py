import re

n = int(input())

regPat = r'^(?=(?:.*[A-Z]){2,})(?=(?:.*\d){3,})(?!.*(.).*\1)[a-zA-Z0-9]{10}$'

for _ in range(n):
    s = input().strip()
    if re.fullmatch(regPat, s):
        print("Valid")
    else:
        print("Invalid")
