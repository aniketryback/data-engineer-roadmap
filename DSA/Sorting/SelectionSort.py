def selsort(arr):
    for i in range(len(arr) - 1):
        temp = i
        for j in range(i + 1, len(arr)):
            if arr[temp] > arr[j] : 
                temp = j
        arr[i], arr[temp] = arr[temp], arr[i]        
    return arr

print(selsort([2,3,1,4,6,3]))

