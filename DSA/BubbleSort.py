# cook your dish here
def binsort(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(i + 1,  n):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
    return arr 

print(BinSearch([3,2,1,4,6,3]))
             