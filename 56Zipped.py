N,X = map(int,input().split())

subject_data = [list(map(float,input().split())) for _ in range(X)]
for stud_data in zip(*subject_data):
    print(round(sum(stud_data)/X,1))
