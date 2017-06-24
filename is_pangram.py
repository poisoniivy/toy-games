def is_pangram(sentence):
    """
    >>> is_pangram("The quick brown fox jumps over the lazy dog!")
    True

    >>> is_pangram("I like cats, but not mice")
    False
    """
    sentence = sentence.lower()

    alphabet_set = set(['a', 'b', 'c', 'd', 'e', 'f' , 'g', 'h', 'i', 'j', 'k', 'l',\
        'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'])

    sent_dedupe = set()

    for c in sentence:
        if c in alphabet_set:
            sent_dedupe.add(c)


    for char in sent_dedupe:
        if char in alphabet_set:
            alphabet_set.remove(char)

    if not alphabet_set:
        return True

    return False
