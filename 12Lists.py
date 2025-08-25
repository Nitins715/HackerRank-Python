if __name__ == '__main__':
    N = int(input())
    records = []
    for i in range(N):
        data = input().split()
        if "print" in data[0]:
            print(records)
        elif "insert" in data[0]:
            records.insert(int(data[1]),int(data[2]))
        elif "remove" in data[0]:
            records.remove(int(data[1]))
        elif "append" in data[0]:
            records.append(int(data[1]))
        elif "sort" in data[0]:
            records.sort()
        elif "pop" in data[0]:
            records.pop() 
        elif "reverse" in data[0]:
            records.reverse()       
        else:
            print("some error")    