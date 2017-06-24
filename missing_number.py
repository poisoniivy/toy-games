def missing_number(lst, max_num):
    """
    >>> missing_number([2, 1, 4, 3, 6, 5, 7, 10, 9], 10)
    8

    """

    total_sum = (max_num * (max_num + 1))/2
    lst_sum = sum(lst)

    return total_sum - lst_sum
