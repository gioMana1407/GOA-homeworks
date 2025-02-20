# This kata is about multiplying a given number by eight if it is an even number and by nine otherwise.

def simple_multiplication(number) :
    if number % 2 == 0:
        return number * 8
    else:
        return number * 9
    

# Given a set of numbers, return the additive inverse of each. Each positive becomes negatives, and the negatives become positives.
def invert(lst):
    result = []
    for i in lst:
        result.append(-i)
    return result

# Given a string of digits, you should replace any digit below 5 with '0' and any digit 5 and above with '1'. Return the resulting string.

def fake_bin(x):
    stringg = ""
    for char in x:   
        if int(char) < 5:
            stringg += "0"
        else:
            stringg += "1"
    return stringg

# Write a function to split a string and convert it into an array of words.
def string_to_array(s):
    return s.split(" ")

# Let's play! You have to return which player won! In case of a draw return Draw!.
def rps(p1, p2):
    if p1 == p2:
        return "Draw!"
    elif p1 == "scissors" and p2 == "paper":
        return "Player 1 won!"
    elif p1 == "scissors" and p2 == "rock":
        return "Player 2 won!"
    elif p1 == "rock" and p2 == "scissors":
        return "Player 1 won!"
    elif p1 == "rock" and p2 == "paper":
        return "Player 2 won!"
    elif p1 == "paper" and p2 == "scissors":
        return "Player 2 won!"
    elif p1 == "paper" and p2 == "rock":
        return 'Player 1 won!'
    
# Create a function that gives a personalized greeting. This function takes two parameters: name and owner.
def greet(name, owner):
    if name == owner:
        return 'Hello boss'
    else:
        return 'Hello guest'
    
# You take your son to the forest to see the monkeys. You know that there are a certain number there (n), but your son is too young to just appreciate the full number, he has to start counting them from 1.

# As a good parent, you will sit and count with him. Given the number (n), populate an array with all numbers up to and including that number, but excluding zero.

def monkey_count(n):
    result = []
    for i in range(1,n + 1):
        result.append(i)
    return result
        
# I have a cat and a dog.

# I got them at the same time as kitten/puppy. That was humanYears years ago.

# Return their respective ages now as [humanYears,catYears,dogYears]

def human_years_cat_years_dog_years(humanYears):
    if humanYears == 1:
        catYears = 15
        dogYears = 15
    elif humanYears == 2:
        catYears = 24
        dogYears = 24
    else:
        catYears = 24 + (humanYears - 2) * 4
        dogYears = 24 + (humanYears - 2) * 5
    
    return [humanYears, catYears, dogYears]

# An isogram is a word that has no repeating letters, consecutive or non-consecutive. Implement a function that determines whether a string that contains only letters is an isogram. Assume the empty string is an isogram. Ignore letter case.
# ython

def is_isogram(string):
    for i in string.lower():
        if string.lower().count(i) > 1:
            return False
    return True

# Given an array of ones and zeroes, convert the equivalent binary value to an integer.

# Eg: [0, 0, 0, 1] is treated as 0001 which is the binary representation of 1.

def binary_array_to_number(arr):
    decimal_number = 0
    for i in arr:
        decimal_number = decimal_number * 2 + i
    return decimal_number 
