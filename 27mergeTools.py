def merge_the_tools(string, k):
    for i in range(0, len(string), k):
        seen = set()
        out = ''
        for c in string[i: i + k]:
            if c in seen:
                continue
            seen.add(c)
            out += c
        print(out)
        
if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)