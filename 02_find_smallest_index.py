def find_smallest_index(arr):
    if not arr:
        raise ValueError("Cannot find smallest in empty array")
    
    smallest = arr[0]
    smallest_idx = 0
    
    for i in range(1, len(arr)): 
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_idx = i

    return smallest_idx

print(find_smallest_index([4, 8, 0, 5])) # => 2

