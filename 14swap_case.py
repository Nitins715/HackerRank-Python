# Shorter version
# def swap_case(s):
#     return s.swapcase()
def swap_case(s):
    swapped = ""
    for ch in s:
        if ch.islower():
            swapped += ch.upper()
        elif ch.isupper():
            swapped += ch.lower() 
        else:
            swapped += ch       
    return swapped

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)