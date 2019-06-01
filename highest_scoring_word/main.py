"""
Given a string of words, you need to find the highest scoring word.

Each letter of a word scores points according to its position in the alphabet: a = 1, b = 2, c = 3 etc.

You need to return the highest scoring word as a string.

If two words score the same, return the word that appears earliest in the original string.

All letters will be lowercase and all inputs will be valid.
"""
import string

def execute(x):
    col = x.split(' ')
    d = {}
    
    for word in col:
        d[word] = 0
        for letter in word:
            d[word] += int(string.ascii_lowercase.index(letter)) + 1
    r = ''
    count = 0
    for word,cnt in d.items():
        if cnt > count:
            r = word
            count = cnt
    return r 
