if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    print(sorted(set(arr))[-2])

# Without sorting the whole list (faster for large inputs):
# n = int(input())
# arr = set(map(int, input().split()))

# first = max(arr)
# arr.remove(first)
# second = max(arr)
# print(second)    