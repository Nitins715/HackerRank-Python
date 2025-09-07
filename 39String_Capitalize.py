def solve(s):
    splitted_s = s.split(" ")
    return (" ".join(i.capitalize() for i in splitted_s))
    
if __name__ == '__main__':
    s = input()
    result = solve(s)
    print(result)