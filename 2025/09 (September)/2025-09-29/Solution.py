import re

def get_longest_word(sentence):
    words = re.split('[. ]', sentence)
    return max(words, key=len)