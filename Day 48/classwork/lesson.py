# Check to see if a string has the same amount of 'x's and 'o's. The method must return a boolean and be case insensitive. The string can contain any char.
def xo(s):
    s = s.lower()
    if s.count("x") == s.count("o"):
        return True
    elif s.count("x") == 0 and s.count("o") == 0:
        return True
    else:
        return False
    
# Simple, given a string of words, return the length of the shortest word(s).

# String will never be empty and you do not need to account for different data types.

def find_short(s):
    words = s.split()  
    shortest = len(words[0])  
    for i in words:  
        if len(i) < shortest:  
            shortest = len(i)
    return shortest

# Complete the solution so that it returns true if the first argument(string) passed in ends with the 2nd argument (also a string).
def solution(text, ending):
    return text[-len(ending):] == ending