cube = lambda x:x**3

def fibonacci(n):
    val = []
    a = 0
    b = 1
    for _ in range(n):
        val.append(a)
        # print(a,end = " ")
        temp = a
        a = b
        b = temp+b
    return val
    

if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))