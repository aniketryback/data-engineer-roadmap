def rotate(arr, d):
    n = len(arr)
    d = d % n  # handle cases where d > n
    return arr[-d:] + arr[:-d]

arr = [1, 2, 3, 4, 5, 6]
d = 1
print(rotate(arr, d))
