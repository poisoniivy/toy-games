"""Given a string, write a function to check if it is a permutation of a
palindrome.

input: Tact Coa
output: true (taco cat or atco cta)

add all characters into a dictionary and count occurances as values
don't add spaces
check values, if there are more than 1 odd value, not a palindrome

"""


def palindrome_permutation(str):
    """
    >>> palindrome_permutation("Tact Coa")
    True
    """
    char_dict = {}

    for c in str.lower():
        if c != " ":
            char_dict[c] = char_dict.get(c, 0) + 1

    has_odd = False
    for count in char_dict.values():
        if count % 2 == 1:
            if has_odd == True:
                return False
            has_odd = True
    return True
