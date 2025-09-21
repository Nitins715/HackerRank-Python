from collections import Counter
if __name__ == '__main__':
    s = input()
    c = Counter(s).items()
    s=sorted(list(c), key=lambda item: (-item[1], item[0]))[:3]
    [print(_[0],_[1]) for _ in s]