def sort_list(data):
    # Separate numbers and strings
    numbers = [x for x in data if isinstance(x, (int, float))]
    strings = [x for x in data if isinstance(x, str)]
    
    # Sort each type separately
    numbers.sort()
    strings.sort()
    
    # Combine sorted results
    return numbers + strings

# Test with mixed data types
items = [3, "apple", 1, "banana", 2]
print("Original list:", items)
print("Sorted list:", sort_list(items))

# Test with more mixed data
items2 = [10, "zebra", 5.5, "cat", 2, "dog", 7]
print("\nOriginal list:", items2)
print("Sorted list:", sort_list(items2))
