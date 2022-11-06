def list_check(lst):
    """Are all items in lst a list?

        >>> list_check([[1], [2, 3]])
        True

        >>> list_check([[1], "nope"])
        False
    """
    second_list = [x for x in lst if type(x) == list]
    if len(lst) == len(second_list):
        return True
    else:
        return False



