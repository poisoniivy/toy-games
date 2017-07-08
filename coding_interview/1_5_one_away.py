""" There are three types of edits that can be performed on strings:
insert a character, remove a character, or replace a character.
Given two strings, write a function to check if they are one edit
or zero edits away.

pale, ple -> true
pales, pale -> true
pale, bale -> true
pale, bake -> false

create dictionary
check letters in one dictionary



"""

def one_away(str1, str2):
    """
    >>> one_away('pale', 'ple')
    True
    >>> one_away('pales', 'pale')
    True
    >>> one_away('pale', 'bale')
    True
    >>> one_away('pale', 'bake')
    False
    """

    if abs(len(str1) - len(str1)) > 1:
        return False

    set1 = set(list(str1))
    diff_count = 0

    for ch in str2:
        if diff_count > 1:
            return False
        if ch in set1:
            set1.remove(ch)
        else:
            diff_count += 1

    # removed all similarities
    # checks if it is a replacement
    if diff_count == len(set1):
        return True
    else:
        diff_count += len(set1)
        return diff_count <= 1
