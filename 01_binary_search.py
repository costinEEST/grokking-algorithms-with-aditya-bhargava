# %% 

def binary_search(arr, item):
  low = 0
  high = len(arr) - 1

  while low <= high:
    mid = (low + high) // 2
    guess = arr[mid]
    if guess == item:
      return mid
    elif guess > item:
      high = mid - 1
    else:
      low = mid + 1
  return None

my_list = [1, 3, 5, 7, 9]

print(binary_search(my_list, 3)) # => 1
print(binary_search(my_list, -1)) # => None
# %%
