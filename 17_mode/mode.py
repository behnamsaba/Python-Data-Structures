
def mode(nums):
    """Return most-common number in list.

    For this function, there will always be a single-most-common value;
    you do not need to worry about handling cases where more than one item
    occurs the same number of times.

        >>> mode([1, 2, 1])
        1

        >>> mode([2, 2, 3, 3, 2])
        2
    """
    my_dict = {}
    for num in nums:
        my_dict[num] = my_dict.get(num, 0) + 1
    
    key_list = list(my_dict.keys())
    value_list = list(my_dict.values())
    findmax = max(value_list)
    return [i for i in my_dict if my_dict[i] == findmax]

print(*mode([1, 2, 1]))


