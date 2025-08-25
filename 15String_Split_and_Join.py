def split_and_join(line):
    record = line.split(" ")
    result = "-".join(record)
    return result

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)