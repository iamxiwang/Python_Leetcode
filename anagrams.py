# Write a function, anagrams, that takes in two strings as arguments. The function should return a boolean indicating whether or not the strings are anagrams. Anagrams are strings that contain the same characters, but in any order.

def anagrams(s1, s2):
    return sorted(list(s1)) == sorted(list(s2))

print(anagrams('cats', 'tocs'))