import re
pattern=r"^[789]{1}\d{9}$"
for _ in range(int(input())):
    if re.match(pattern,input()):
        print("YES")
    else:
        print("NO")