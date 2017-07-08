"""Given two strings, write a method to decide if one is a permuataion of the other
>> "god   " not the same as "dog"
Case sensivie

first - check to see if same length
then - sort? similar to anagram
"""

def check_permutation(str1, str2):
    """returns true if they are permutations of each other."""

    if len(str1) != len(str2):
        return False

    # O(n log n) runtime due to the sort
    # memory: also linear due to creating new strings with sort
    return sorted(str1) == sorted(str2)


def check_permutation2(str1, str2):
    """with sets."""

    if len(str1) != len(str2):
        return False

    set1 = set(list(str1))
    set2 = set(list(str2))

    for char in set1:
        if char not in set2:
            return False
        set2.remove(char)

    if len(set2) > 0:
        return False

    return True
