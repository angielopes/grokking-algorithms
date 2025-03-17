# %%
"""Write out the code for the earlier sum function."""


def sum(list):
    """
    Recursively calculates the sum of all elements in a list.
    Args:
        list (list) : A list of numerical values.
    Returns:
        int : The sum of all elements in the list. Returns 0 if the list is empty.
    """

    if list == []:
        return 0
    return list[0] + sum(list[1:])


my_sum = sum([2, 4, 6])
print(my_sum)

# %%
"""Write a recursive function to count the number of items in a list."""


def count_numbers_in_list(list):
    """
    Counts the number of elements in a list using recursion.
    Args:
        list (list): The list of elements to be counted.
    Returns:
        int: The number of elements in the list.
    """

    if list == []:
        return 0
    return 1 + count_numbers_in_list(list[1:])


my_count = count_numbers_in_list([1, 2, 3, 4, 5, 6, 7, 8, 9])
print(my_count)
# %%
