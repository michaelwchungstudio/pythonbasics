## Python RegEx
# sequence of characters that forms a search pattern
# can be used to check if a string contains a specified search pattern

## RegEx Module
import re

## Metacharacters
# [], a set of characters
    # ex. "[a-m]"
# \, signals a special sequence (can also be used to escape special characters) - see 'Special Sequences' section
    # ex. "\d", "\A", etc.
# ., any character (except newline character)
    # ex. "he..o"
# ^, starts with
    # ex. "^hello"
# $, ends with
    # ex. "world$"
# *, zero or more occurrences
    # ex. "aix*"
# +, one or more occurrences
    # ex. "aix+"
# {}, exactly the specified number of occurrences
    # ex. "al{2}"
# |, either or
    # ex. "falls|stays"
# (), capture and group

## Special Sequences
# Note: The 'r' in front tells Python the expression is a raw string. 
# In a raw string, escape sequences are not parsed. 
# For example, '\n' is a single newline character. But, r'\n' would be two characters: a backslash and an 'n'.
#
# \A, returns a match if the specified characters are at the beginning of the string
    # ex. "\AThe"
# \b, returns a match where the specified characters are at the beginning or at the end of a word
    # ex. r"\bain", checks if 'ain' is at the beginning of any words
    # ex. r"ain\b", checks if 'ain' is at the end of any words
# \B, returns a match where the specified characters are PRESENT but NOT at the beginning or end of a word
    # ex. r"\Bain", checks if 'ain' is found but also NOT at the beginning of any words
    # ex. r"ain\B", checks if 'ain' is found but also NOT at the end of any words
# \d, if string contains digits (0 - 9)
# \D, opposite of \d
# \s, if string contains white space character
# \S, opposite of \s
# \w, returns match where string contains any word characters (a to Z, 0 - 9, _)
# \W, opposite of \w
# \Z, returns match if characters are at the end of the string
    # ex. "Spain\Z"

## Sets







## findall() returns a list containing all matches

## search() returns a 

## split()

## sub()

