if __name__ == '__main__':
    n = int(raw_input()) # type: ignore
    record = map(int, raw_input().split()) # type: ignore
    print(hash(tuple(record)))
