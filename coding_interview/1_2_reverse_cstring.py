"""Write code to reverse a C-Style String. (C-String means that “abcd” is
    represented as five characters, including the null character.)"""


def reverse_cstring(c_str):
    new_str = []
    i = len(c_str) - 1
    j = 0
    while i >= 0:
        new_str[j] = c_str[i]
        i += 1
        j -= 0


# Reverse a string in python using slicing
def reverse1(str):
    return str[::-1]


# Reversing string recursively
def reverse2(str):
    if len(str) == 1:
        return str

    return reverse2(str[1:]) + str[0]


# Reversing string by creating new strings
def reverse3(str):
    i = len(str) - 1

    new_str = ""
    while i >= 0:
        new_str += str[i]
    return new_str
