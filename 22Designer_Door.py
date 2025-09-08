n,m = map(int,input().split())
des = ".|."

for i in range(int((n-1)/2)):
    print(((2*i+1)*(des)).center(m,"-"))
print("WELCOME".center(m,"-"))
for i in range(int((n-1)/2),0,-1):
    print(((2*i-1)*(des)).center(m,"-"))