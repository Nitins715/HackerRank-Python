# Shorter version
# def swap_case(s):
#     return s.swapcase()
def swap_case(s: str) -> str:
    return "".join(
        ch.upper() if ch.islower() else ch.lower() if ch.isupper() else ch
        for ch in s
        )
        
if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)