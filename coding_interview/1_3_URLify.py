"""Write a method to replace all spaces in a string with ‘%20’."""


# def replace_space(str):
#     s = '%20'
#     word_list = str.split(" ")
#     new_word = s.join(word_list)
#     return new_word

def URLify(str):

    space = '%20'

    word_list = str.split(" ")
    new_string = space.join(word_list)
    return new_string
