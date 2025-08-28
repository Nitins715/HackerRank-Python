import numpy
def arrays(arr):
    arr.reverse()
    f1 = list(map(float,arr))
    res = numpy.array(f1)
    return res
    
arr = input().strip().split(' ')
result = arrays(arr)
print(result)