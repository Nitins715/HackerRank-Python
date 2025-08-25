if __name__ == '__main__':
    n = int(raw_input()) 
    record = map(int, raw_input().split()) 
    print(hash(tuple(record)))
    # Use python 2
