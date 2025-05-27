# Insertion Sort Algorithm in Python

def insertion_sort(arr):
    """
    Sorts the input list using the Insertion Sort algorithm.

    Args:
    arr (list): List of integers to be sorted

    Returns:
    list: Sorted list in ascending order
    """
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1

        # Shift elements that are greater than key to one position ahead
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        
        arr[j + 1] = key  # Place key at the correct position
    
    return arr


# Example usage
if __name__ == "__main__":
    sample_list = [3, 2, 1, 4, 6, 3]
    sorted_list = insertion_sort(sample_list)
    print("Sorted list:", sorted_list)
