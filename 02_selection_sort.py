def selection_sort(arr):
    n = len(arr)
    
    for i in range(n - 1):
        # Find index of minimum element in remaining unsorted portion
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        
        # Swap minimum element with first element of unsorted portion
        if min_idx != i:  # Only swap if necessary
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
    
    return arr

print(selection_sort([4, 8, 0, 5])) # => [0, 4, 5, 8]

