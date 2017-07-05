"""Implement an algorithm to determine if a string has all unique characters.
What if you can not use additional data structures?
"""


def has_unique(str):
    """
    >>> has_unique("hello")
    False
    >>> has_unique("cat")
    True
    >>> has_unique("")
    False
    """

    i = 0
    if str == "":
        return False
    while i < len(str) - 1:
        if str[i] in str[i+1:]:
            return False
        i += 1
    return True
