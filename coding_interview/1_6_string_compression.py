""" Implement a method to perform basic string compression using the counts 
repeated characters. If the "compressed" string would not become smaller
than the original string, your method should return the original string.
You can assume the string has only uppercase and lowercase letters a-z.

iterate through each character
variable to keep track of if char has changed
variable to keep track of count 
if char has changed, add out count and the previous char to newstring
return whichever string is smaller, newstring or the original

"""

def string_compression(str):
    """
    >>> string_compression('aabcccccaaa')
    a2b1c5a3
    >>> string_compression('abc')
    abc
    """

    # set up of all the variables
    current_char = str[0]
    char_count = 0
    newstring = ""

    for ch in str:
        # if the character of string is same is previous char
        if ch == current_char:
            char_count += 1
        else:
            # adding to new string and resetting variables
            newstring += ch
            newstring += str(char_count)
            char_count = 1
            current_char = ch

    if len(new_string) <= len(str):
        return new_string
    else:
        return str
