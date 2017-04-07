#!/bin/python3

# Write a function to find the longest common prefix string amongst an array of strings. Leetcode #14.

def longest_common_prefix(strs):
    """
    :type strs: List[str]
    :rtype: str
    """
    if len(strs) < 1:
        return ""
    elif len(strs) == 1:
        return strs[0]
    index = 0
    prefix = strs[0]
    found = False
    for i in range(1, len(strs)):
        temp = ""
        for j, c in enumerate(zip(prefix, strs[i])):
            if c[0] == c[1]:
                found = True
                temp += c[0]
                continue
            else:
                break
        prefix = temp
    return prefix if found else ""
