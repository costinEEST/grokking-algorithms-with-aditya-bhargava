# Find smallest index 

```python
# Original code (performance and naming issues)
def findSmallest(arr):
    smallest = arr[0]
    smallest_index = 0
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index

# ✅ OPTION 1: Built-in optimized (FASTEST for most cases)
def find_smallest_index(arr):
    """Find index of smallest element using built-in min() function."""
    return min(range(len(arr)), key=arr.__getitem__)

# ✅ OPTION 2: Using enumerate (more readable, good performance)
def find_smallest_index_enum(arr):
    """Find index of smallest element using enumerate."""
    return min(enumerate(arr), key=lambda x: x[1])[0]

# ✅ OPTION 3: NumPy version (FASTEST for large arrays)
import numpy as np

def find_smallest_index_numpy(arr):
    """Find index of smallest element using NumPy (best for large arrays)."""
    return np.argmin(arr)

# ✅ OPTION 4: Optimized manual loop (if you must avoid built-ins)
def find_smallest_index_manual(arr):
    """Optimized manual implementation with error handling."""
    if not arr:
        raise ValueError("Cannot find smallest in empty array")
    
    smallest_value = arr[0]
    smallest_idx = 0
    
    # Use enumerate to avoid range(len()) pattern
    for idx, value in enumerate(arr[1:], 1):
        if value < smallest_value:
            smallest_value = value
            smallest_idx = idx
    
    return smallest_idx

# ✅ OPTION 5: 2025 Type-annotated version with modern features
from typing import Sequence, TypeVar
from collections.abc import Iterable

T = TypeVar('T', bound=object)  # Support any comparable type

def find_smallest_index_typed(arr: Sequence[T]) -> int:
    """
    Find index of smallest element with full type safety.
    
    Args:
        arr: Sequence of comparable elements
        
    Returns:
        Index of the smallest element
        
    Raises:
        ValueError: If array is empty
    """
    if not arr:
        raise ValueError("Cannot find smallest in empty sequence")
    
    return min(range(len(arr)), key=arr.__getitem__)

# 🧪 Performance comparison and testing
if __name__ == "__main__":
    import timeit
    import random
    
    # Test data
    small_array = [4, 8, 0, 5]
    large_array = [random.randint(0, 1000) for _ in range(10000)]
    
    print("=== FUNCTIONALITY TESTS ===")
    print("Original:", findSmallest(small_array))
    print("Built-in:", find_smallest_index(small_array))
    print("Enumerate:", find_smallest_index_enum(small_array))
    print("NumPy:", find_smallest_index_numpy(small_array))
    print("Manual:", find_smallest_index_manual(small_array))
    print("Typed:", find_smallest_index_typed(small_array))
    
    print("\n=== PERFORMANCE TESTS (10,000 elements) ===")
    
    # Original approach
    time_original = timeit.timeit(
        lambda: findSmallest(large_array), number=1000
    )
    print(f"Original approach: {time_original:.4f}s")
    
    # Built-in approach  
    time_builtin = timeit.timeit(
        lambda: find_smallest_index(large_array), number=1000
    )
    print(f"Built-in approach: {time_builtin:.4f}s")
    
    # NumPy approach
    np_array = np.array(large_array)
    time_numpy = timeit.timeit(
        lambda: find_smallest_index_numpy(np_array), number=1000
    )
    print(f"NumPy approach: {time_numpy:.4f}s")
    
    print(f"\nSpeedup vs original:")
    print(f"Built-in: {time_original/time_builtin:.1f}x faster")
    print(f"NumPy: {time_original/time_numpy:.1f}x faster")

# 🎯 NAMING CONVENTION FIXES:

# ❌ NOT PYTHONIC (your original)
# - findSmallest: camelCase (should be snake_case)
# - Missing type hints
# - No docstring
# - No error handling

# ✅ PYTHONIC 2025 STYLE:
# - snake_case function names
# - Type hints with modern typing
# - Comprehensive docstrings
# - Error handling
# - Use built-ins when possible
```

# Selection sort

```python
# ❌ ORIGINAL CODE (O(n³) due to pop() overhead!)
def selectionSort(arr):                      
    newArr = []
    copiedArr = list(arr)  # copy array before mutating
    for i in range(len(copiedArr)):
        smallest = findSmallest(copiedArr)     
        newArr.append(copiedArr.pop(smallest))  # ← O(n) operation in O(n²) loop!
    return newArr

def findSmallest(arr):
    smallest = arr[0]
    smallest_index = 0
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index

# ✅ REFACTOR 1: Proper O(n²) In-Place Selection Sort
from typing import List, TypeVar

T = TypeVar('T')

def selection_sort_inplace(arr: List[T]) -> List[T]:
    """
    Optimized in-place selection sort - O(n²) time, O(1) space.
    
    Args:
        arr: List to sort (will be modified in-place)
        
    Returns:
        The same list, now sorted
    """
    n = len(arr)
    
    for i in range(n - 1):  # Only need n-1 passes
        # Find index of minimum element in remaining unsorted portion
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        
        # Swap minimum element with first element of unsorted portion
        if min_idx != i:  # Only swap if necessary
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
    
    return arr

# ✅ REFACTOR 2: Non-Mutating Version (Creates Copy)
def selection_sort_copy(arr: List[T]) -> List[T]:
    """
    Selection sort without mutating original array.
    
    Args:
        arr: Original list to sort
        
    Returns:
        New sorted list
    """
    if not arr:
        return []
    
    # Create copy to avoid mutating original
    result = arr.copy()
    return selection_sort_inplace(result)

# ✅ REFACTOR 3: Generator Version (Memory Efficient)
def selection_sort_generator(arr: List[T]):
    """
    Memory-efficient generator version of selection sort.
    Yields elements in sorted order without creating full result list.
    """
    if not arr:
        return
    
    # Work with indices to avoid mutating original array
    remaining_indices = list(range(len(arr)))
    
    while remaining_indices:
        # Find index of minimum element among remaining indices
        min_pos = 0
        for i in range(1, len(remaining_indices)):
            if arr[remaining_indices[i]] < arr[remaining_indices[min_pos]]:
                min_pos = i
        
        # Yield the minimum element and remove its index
        min_idx = remaining_indices.pop(min_pos)
        yield arr[min_idx]

# ✅ REFACTOR 4: Using Modern Python Features (2025)
def selection_sort_modern(arr: List[T]) -> List[T]:
    """
    Modern selection sort using Python 3.8+ features and optimizations.
    """
    if not arr:
        return []
    
    result = arr.copy()
    n = len(result)
    
    for i in range(n - 1):
        # Use min() with key function for cleaner code
        min_idx = min(range(i, n), key=result.__getitem__)
        
        # Swap using tuple unpacking (already optimal)
        if min_idx != i:
            result[i], result[min_idx] = result[min_idx], result[i]
    
    return result

# ✅ REFACTOR 5: Practical 2025 Solution
def sort_array(arr: List[T]) -> List[T]:
    """
    Practical sorting function - uses built-in Timsort (O(n log n)).
    For production code, this is almost always the right choice.
    """
    return sorted(arr)

# 🧪 PERFORMANCE & CORRECTNESS TESTS
import timeit
import random

def run_comprehensive_tests():
    """Test all implementations for correctness and performance."""
    
    # Test data
    test_cases = [
        [5, 3, 6, 2, 10],
        [1],
        [],
        [3, 3, 3, 3],
        [5, 4, 3, 2, 1],  # Reverse sorted (worst case)
        [1, 2, 3, 4, 5],  # Already sorted (best case)
    ]
    
    print("=== CORRECTNESS TESTS ===")
    for i, test_arr in enumerate(test_cases):
        print(f"\nTest {i+1}: {test_arr}")
        
        # Test all implementations
        original_result = selectionSort(test_arr.copy()) if test_arr else []
        inplace_result = selection_sort_copy(test_arr)
        modern_result = selection_sort_modern(test_arr)
        generator_result = list(selection_sort_generator(test_arr))
        builtin_result = sort_array(test_arr)
        
        results = [original_result, inplace_result, modern_result, generator_result, builtin_result]
        all_same = len(set(str(r) for r in results)) == 1
        
        print(f"Original:  {original_result}")
        print(f"In-place:  {inplace_result}")
        print(f"Modern:    {modern_result}")
        print(f"Generator: {generator_result}")
        print(f"Built-in:  {builtin_result}")
        print(f"✅ All correct: {all_same}")
    
    # Performance comparison
    print("\n=== PERFORMANCE COMPARISON ===")
    
    # Small array (100 elements)
    small_arr = [random.randint(0, 1000) for _ in range(100)]
    print(f"\n📊 Small Array (100 elements):")
    
    time_original = timeit.timeit(lambda: selectionSort(small_arr.copy()), number=100)
    time_inplace = timeit.timeit(lambda: selection_sort_copy(small_arr), number=100)
    time_modern = timeit.timeit(lambda: selection_sort_modern(small_arr), number=100)
    time_builtin = timeit.timeit(lambda: sort_array(small_arr), number=100)
    
    print(f"Original (O(n³)):  {time_original:.4f}s")
    print(f"In-place (O(n²)):  {time_inplace:.4f}s ({time_original/time_inplace:.1f}x faster)")
    print(f"Modern (O(n²)):    {time_modern:.4f}s ({time_original/time_modern:.1f}x faster)")
    print(f"Built-in Timsort:  {time_builtin:.4f}s ({time_original/time_builtin:.1f}x faster)")
    
    # Medium array (1000 elements) - only fast algorithms
    medium_arr = [random.randint(0, 1000) for _ in range(1000)]
    print(f"\n📊 Medium Array (1000 elements):")
    
    time_inplace = timeit.timeit(lambda: selection_sort_copy(medium_arr), number=10)
    time_modern = timeit.timeit(lambda: selection_sort_modern(medium_arr), number=10)
    time_builtin = timeit.timeit(lambda: sort_array(medium_arr), number=10)
    
    print(f"In-place (O(n²)):  {time_inplace:.4f}s")
    print(f"Modern (O(n²)):    {time_modern:.4f}s")
    print(f"Built-in Timsort:  {time_builtin:.4f}s ({time_inplace/time_builtin:.1f}x faster)")

# 📋 COMPLEXITY ANALYSIS
def complexity_analysis():
    print("\n=== COMPLEXITY ANALYSIS ===")
    print("""
🔍 ORIGINAL CODE ISSUES:
   Time Complexity: O(n³) ❌
   - Outer loop: O(n)
   - findSmallest: O(n)  
   - list.pop(index): O(n) ← This kills performance!
   
   Space Complexity: O(n) for copied array

✅ OPTIMIZED VERSIONS:
   In-place Selection Sort: O(n²) time, O(1) space
   Modern Selection Sort: O(n²) time, O(n) space  
   Built-in sorted(): O(n log n) time, O(n) space
   
🚀 PERFORMANCE IMPROVEMENTS:
   - Eliminated O(n) pop() operations
   - Reduced from O(n³) to O(n²)
   - Used efficient swapping instead of array mutations
   - Added type hints and proper error handling
   
🎯 2025 BEST PRACTICES:
   - Use sorted() for production code (fastest, most reliable)
   - Use proper selection sort for educational purposes
   - Always include type hints and docstrings
   - Use snake_case naming convention
""")

if __name__ == "__main__":
    run_comprehensive_tests()
    complexity_analysis()
    
    print("\n=== 2025 RECOMMENDATIONS ===")
    print("""
🏆 FOR PRODUCTION: Use `sorted(arr)` 
   - O(n log n) Timsort algorithm
   - Highly optimized C implementation
   - Handles edge cases perfectly
   
🎓 FOR LEARNING: Use optimized selection sort
   - Proper O(n²) time complexity
   - In-place swapping, no expensive pop() operations
   - Modern Python style with type hints
   
❌ AVOID: Your original approach
   - O(n³) complexity due to pop() in loop
   - Inefficient memory usage
   - Non-Pythonic naming conventions
""")
```