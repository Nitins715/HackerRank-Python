if __name__ == '__main__':
    data = []
    marks = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        data.append([name,score])
        marks.append(score) 
    res = sorted(set(marks))[1]
    final_data = []
    for name,score in data:
        if(score == res):
            final_data.append(name)
    final_data.sort()        
    for i in final_data:
        print(i)       
