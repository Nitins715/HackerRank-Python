from itertools import permutations
s = list(input().split(" "))
 
a = list((permutations(s[0],int(s[1]))))
a.sort()
print(*map(''.join,a),sep='\n')