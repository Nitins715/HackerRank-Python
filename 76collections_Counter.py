from collections import Counter
no_of_shoes = int(input())
size_list = map(int, input().split(" "))
total_customers = int(input())
size_dict = Counter(size_list)
earning = 0

for i in range(total_customers):
    req = list(map(int, input().split(" ")))
    if size_dict[req[0]]:
        earning += req[1]
        size_dict[req[0]] -= 1

print(earning)
