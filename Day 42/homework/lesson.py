# Given an array of integers as strings and numbers, return the sum of the array values as if all were numbers.

# Return your answer as a number.

def sum_mix(arr):
    num = []
    for i in arr:
        if type(i) == str:
            num.append(int(i))
        else:
            num.append(i)
    return sum(num)

# Given a string, you have to return a string in which each character (case-sensitive) is repeated once.

def double_char(s):
    double = ""
    for i in s:
        double += i * 2
    return double

# I'm new to coding and now I want to get the sum of two arrays... Actually the sum of all their elements. I'll appreciate for your help.

# P.S. Each array includes only integer numbers. Output is a number too.

def array_plus_array(arr1,arr2):
    double_sum = 0
    for i in arr1:
        double_sum += i
    for i in arr2:
        double_sum += i
    return double_sum

# Complete the solution so that it reverses all of the words within the string passed in.

# Words are separated by exactly one space and there are no leading or trailing spaces.

def reverse_words(s):
    words = s.split()
    reversed_words = []
    for word in words:  
        reversed_words.insert(0, word)
    return ' '.join(reversed_words)

# Create a function that takes 2 integers in form of a string as an input, and outputs the sum (also as a string):

def sum_str(a, b):
    if a == "":  
        a = "0"
    if b == "":  
        b = "0"
    return str(int(a) + int(b))