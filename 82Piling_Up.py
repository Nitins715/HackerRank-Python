from collections import deque
Test_cases =  int(input())
for _ in range(Test_cases):
    n = int(input())
    cube = deque(map(int,input().split()))
    ans = True
    last = max(cube)
    
    while cube:
        if cube[0] >= cube[-1]:
            current = cube.popleft()
        else:
            current = cube.pop()
                
        if last is None or current <= last:
            last = current
        else:
            ans = False
            break
    print("Yes" if ans else "No")   
