def binsearch(arr, target):
    left = 0
    right = len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] < target:
            left = mid + 1
        elif arr[mid] > target:
            right = mid - 1
        else:
            return mid  # Found the target
    return -1  # Target not found

# Test cases
print(binsearch([1, 2, 3, 4, 5, 6], 4))  # Output: 3
print(binsearch([1, 2, 3, 4, 5, 6], 7))  # Output: -1
