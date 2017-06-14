def anagram_of_palindome(word):
    """Returns boolean if anagram of argument is also a palindrome.
    >>> is_anagram_of_palindrome("a")
    True

    >>> is_anagram_of_palindrome("ab")
    False

    >>> is_anagram_of_palindrome("aab")
    True

    >>> is_anagram_of_palindrome("arceace")
    True

    >>> is_anagram_of_palindrome("arceaceb")
    False
    """
    count_dict = {}
    for c in word:
        count_dict[c] = count_dict.get(c, 0) + 1

    single_char = False
    for count in count_dict.values():
        if count % 2 == 1:
            if single_char:
                return False
            single_char = True
    return True
