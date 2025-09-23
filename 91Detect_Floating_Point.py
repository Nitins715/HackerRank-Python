k = int(input())
data = []
for i in range(k):
    data.append(input())

for i in data:
    if '.' in i:
        try:
            float(i)
            print(True)
        except ValueError:
            print(False)
    else:
        print(False)
