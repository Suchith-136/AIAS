def sort_list(data):
    # Filter only integers for sorting
    int_items = [item for item in data if isinstance(item, int)]
    str_items = [item for item in data if isinstance(item, str)]
    # Sort each type separately and concatenate
    return sorted(int_items) + sorted(str_items)

items = [3, "apple", 1, "banana", 2]
print(sort_list(items))
