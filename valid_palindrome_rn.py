#!/bin/python3

# Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.
#
# For example,
# "A man, a plan, a canal: Panama" is a palindrome.
# "race a car" is not a palindrome.
# Leetcode #125

import string

def is_palindrome(s):
    """
    :type s: str
    :rtype: bool
    """
    if len(s) <= 1:
      return True
    s_no_punctuation = "".join(ch.lower() for ch in s if ch not in string.punctuation and ch != " ")
    i, j = 0, len(s_no_punctuation)-1
    palindrome = True
    while i<j:
        if s_no_punctuation[i] != s_no_punctuation[j]:
            palindrome = False
            break
        i += 1
        j -= 1
    return palindrome
