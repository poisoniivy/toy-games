"""Write a method to decide if two strings are anagrams or not."""

def is_anagram(str1, str2):
    return sorted(str1) == sorted(str2)

# runtime O(n log n) -> sorted function
