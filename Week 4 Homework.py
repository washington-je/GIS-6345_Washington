#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Converted from Jupyter Notebook: notebook.ipynb
Conversion Date: 2025-10-13T02:54:22.338Z
"""

word = 'banana'
count = 0
for letter in word:
    if letter == 'a':
        count = count + 1
print(count)

string = 'racecar'
def is_palindrome(word):
    return word[::-1]
print(is_palindrome(string))