"""Design an algorithm and write code to remove the duplicate characters in a
string without using any additional buffer. NOTE: One or two additional
variables are fine. An extra copy of the array is not.
FOLLOW UP
Write the test cases for this method.
"""

def dedupe(str):
    """
    >>> dedupe("mississippi")
    'misp'
    >>> dedupe("hello")
    'helo'
    >>> dedupe("cat")
    'cat'
    >>> dedupe("")
    ''
    """
    used_chars = set() # hash table of used characters. fixed size.
    new_word = "" # new word is instantiated

    for c in str:
        if c not in used_chars:
            new_word += c
            used_chars.add(c)
    return new_word

    # runtime O(n^2), in statement within a forloop
    # memory(constant)? set is constant as can only store fixed number of chars
    # new_word will be equal or smaller than current str
