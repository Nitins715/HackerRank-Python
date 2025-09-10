n = int(input()) 
s = set(map(int, input().split()))
m = int(input())

for i in range(m):
    cmd = input().split()
    if cmd[0] == "pop":
        try:
            s.pop()
        except KeyError:
            pass
    elif cmd[0] == "remove":
        try:
            s.remove(int(cmd[1]))
        except KeyError:
            pass
    elif cmd[0] == "discard":
        s.discard(int(cmd[1]))

print(sum(s))
