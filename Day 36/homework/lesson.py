# Simple, given a string of words, return the length of the shortest word(s).

# String will never be empty and you do not need to account for different data types.

def find_short(s):
    words = s.split()  
    shortest = len(words[0])  
    for i in words:  
        if len(i) < shortest:  
            shortest = len(i)
    return shortest

# In this kata you will create a function that takes a list of non-negative integers and strings and returns a new list with the strings filtered out.

def filter_list(l):
    list = []
    for i in l:
        if type(i) == int:
            list.append(i)
    return list
        

# Welcome. In this kata, you are asked to square every digit of a number and concatenate them.

def square_digits(num):
    result = ""
    for i in str(num):
        square = int(i) * int(i)
        result = result + str(square)
    return int(result)

# Complete the solution so that it returns true if the first argument(string) passed in ends with the 2nd argument (also a string).
def solution(text, ending):
    return text.endswith(ending)

# You are going to be given a non-empty string. Your job is to return the middle character(s) of the string.

def get_middle(s):   
    if len(s) <= 2:
        return s
    else:
        return get_middle(s[1:-1])