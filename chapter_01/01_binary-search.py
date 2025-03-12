def binary_search(list, item):
    """
    Perform a binary search on a sorted list to find the index of a specified item.
    Args:
        list (list): A sorted list of elements to search through.
        item: The element to search for in the list.
    Returns:
        int: The index of the item if found, otherwise None.
    """

    low = 0  # Pointer
    high = len(list) - 1  # Pointer

    while low <= high:
        mid = (low + high) // 2
        guess = list[mid]
        if guess == item:
            return mid
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None


my_list = [1, 3, 5, 7, 9]

print(binary_search(my_list, 3))  # Position 1
print(binary_search(my_list, -1))  # None
