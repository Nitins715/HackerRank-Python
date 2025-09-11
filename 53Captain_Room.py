n = int(input())
room_list = list(map(int,input().split()))
room_set = set(room_list)

captain = (n * sum(room_set) - sum(room_list)) // (n - 1)
print(captain)
