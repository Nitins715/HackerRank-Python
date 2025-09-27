def is_valid_phone(phone):
    return (len(phone) in range(10, 14) and phone[1:].isdigit())

def wrapper(f):
    def fun(l):
        if len(l) == 0 or not isinstance(l, list):
            raise ValueError("Input must be a non-empty list")
        
        invalid_numbers = [phone for phone in l if not is_valid_phone(phone)]
        if invalid_numbers:
            raise ValueError(f"Invalid phone numbers: {', '.join(invalid_numbers)}")
        
        return f(f"+91 {phone[-10:-5]} {phone[-5:]}" for phone in l)
    return fun

@wrapper
def sort_phone(l):
    print(*sorted(l), sep='\n')

if __name__ == '__main__':
    l = [input() for _ in range(int(input()))]
    sort_phone(l) 