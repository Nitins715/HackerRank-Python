int(input())
A = set(map(int,input().split()))
n = int(input())
for _ in range(n):
    key, value = input().split()
    temp = set(map(int,input().split()))
    # if key == "intersection_update":
    #     A.intersection_update(temp)
    # elif key == "update": 
    #     A.update(temp)
    # elif key == "symmetric_difference_update":
    #     A.symmetric_difference_update(temp) 
    # elif key == "difference_update":
    #     A.difference_update(temp)
    getattr(A, key)(temp)    
        
print(sum(A))
