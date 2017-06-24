
# very slow solution
def add_to_zero(nums):
    """Returns True if any two numbers adds to zero.
    >>> add_to_zero([])
    False
    >>> add_to_zero([1])
    False

    >>> add_to_zero([1, 2, 3])
    False

    >>> add_to_zero([1, 2, 3, -2])
    True

    >>> add_to_zero([0, 1, 2])
    True

    """

    if 0 in nums:
        return True

    for num in nums:
        if -num in nums:
            return True
    return False


# Using set, faster because lookups in sets are O(1)
def add_to_zero2(nums):
    """Returns True if any two numbers adds to zero.
    >>> add_to_zero2([])
    False
    >>> add_to_zero2([1])
    False

    >>> add_to_zero2([1, 2, 3])
    False

    >>> add_to_zero2([1, 2, 3, -2])
    True

    >>> add_to_zero2([0, 1, 2])
    True

    """
    set_nums = set(nums)

    for num in nums:
        if -num in set_nums:
            return True
    return False


# Super fancy answer using the any() function
def add_to_zero3(nums):
    """Returns True if any two numbers adds to zero.
    >>> add_to_zero3([])
    False
    >>> add_to_zero3([1])
    False

    >>> add_to_zero3([1, 2, 3])
    False

    >>> add_to_zero3([1, 2, 3, -2])
    True

    >>> add_to_zero3([0, 1, 2])
    True

    """
    return any(-num in set(nums) for num in nums)
