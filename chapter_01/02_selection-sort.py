def find_smallest(arr):
    """
    Finds the index of the smallest element in the given list.
    Args:
        arr (list): A list of comparable elements.
    Returns:
        int: The index of the smallest element in the list.
    """

    smallest = arr[0]
    smallest_index = 0
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index


def selection_sort(arr):
    """
    Sorts an array using the selection sort algorithm.
    The function iterates over the input array, finds the smallest element,
    removes it from the original array, and appends it to a new array.
    This process is repeated until the original array is empty, resulting
    in a sorted new array.
    Args:
        arr (list): The list of elements to be sorted.
    Returns:
        list: A new list containing the sorted elements.
    """

    new_arr = []
    for i in range(len(arr)):
        smallest = find_smallest(arr)
        new_arr.append(arr.pop(smallest))
    return new_arr


print(selection_sort([5, 3, 6, 2, 10]))
