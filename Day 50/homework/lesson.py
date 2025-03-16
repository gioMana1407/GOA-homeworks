# Given an array of ones and zeroes, convert the equivalent binary value to an integer.

# Eg: [0, 0, 0, 1] is treated as 0001 which is the binary representation of 1.

def binary_array_to_number(arr):
    decimal_number = 0
    for i in arr:
        decimal_number = decimal_number * 2 + i
    return decimal_number 

# Timmy & Sarah think they are in love, but around where they live, they will only know once they pick a flower each. If one of the flowers has an even number of petals and the other has an odd number of petals it means they are in love.

# Write a function that will take the number of petals of each flower and return true if they are in love and false if they aren't.

def lovefunc( flower1, flower2 ):
    if flower1 % 2 == 0 and flower2 % 2 == 1:
        return True
    elif flower2 % 2 == 0 and flower1 % 2 == 1:
        return True
    else:
        return False
    
# Implement a function that accepts 3 integer values a, b, c. The function should return true if a triangle can be built with the sides of given length and false in any other case.

# (In this case, all triangles must have surface greater than 0 to be accepted).

def is_triangle(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        return False
    elif a + b > c and b + c > a and c + a > b:
        return True
    else:
        return False
    
# Take 2 strings s1 and s2 including only letters from a to z. Return a new sorted string (alphabetical ascending), the longest possible, containing distinct letters - each taken only once - coming from s1 or s2.

def longest(a1, a2):
    combined = a1 + a2
    result = []
    for i in combined:
        if i not in result:
            result.append(i)
    result.sort()
    return "".join(result)

# Given a set of numbers, return the additive inverse of each. Each positive becomes negatives, and the negatives become positives.

def invert(lst):
    result = []
    for i in lst:
        result.append(-i)
    return result

# Output will consist of a list of string values (in Haskell and C: Open or Senior) stating whether the respective member is to be placed in the senior or open category.

def open_or_senior(data):
    result = []
    for i in data:
        age = i[0]
        experience = i[1]
        if age >= 55 and experience > 7:
            result.append("Senior")
        else:
            result.append("Open")
    return result

# Given a non-empty array of integers, return the result of multiplying the values together in order. Example:

def grow(arr):
    result = 1
    for i in arr:
        result *= i
    return result

# In a factory a printer prints labels for boxes. For one kind of boxes the printer has to use colors which, for the sake of simplicity, are named with letters from a to m.

# The colors used by the printer are recorded in a control string. For example a "good" control string would be aaabbbbhaijjjm meaning that the printer used three times color a, four times color b, one time color h then one time color a...

# Sometimes there are problems: lack of colors, technical malfunction and a "bad" control string is produced e.g. aaaxbbbbyyhwawiwjjjwwm with letters not from a to m.

# You have to write a function printer_error which given a string will return the error rate of the printer as a string representing a rational whose numerator is the number of errors and the denominator the length of the control string. Don't reduce this fraction to a simpler expression.

# The string has a length greater or equal to one and contains only letters from ato z.

def printer_error(s):
    errors = 0
    for i in s:
        if i < 'a' or i > 'm':
            errors += 1
    return str(errors) + '/' + str(len(s))

# Deoxyribonucleic acid, DNA is the primary information storage molecule in biological systems. It is composed of four nucleic acid bases Guanine ('G'), Cytosine ('C'), Adenine ('A'), and Thymine ('T').

# Ribonucleic acid, RNA, is the primary messenger molecule in cells. RNA differs slightly from DNA its chemical structure and contains no Thymine. In RNA Thymine is replaced by another nucleic acid Uracil ('U').

# Create a function which translates a given DNA string into RNA.

def dna_to_rna(dna):
    return dna.replace('T', 'U')

# Write function bmi that calculates body mass index (bmi = weight / height2).
# if bmi <= 18.5 return "Underweight"
# if bmi <= 25.0 return "Normal"
# if bmi <= 30.0 return "Overweight"
# if bmi > 30 return "Obese"

def bmi(weight, height):
    bmi = weight / (height ** 2)
    if bmi <= 18.5:
        return "Underweight"
    elif  bmi <= 25.0:
        return "Normal"
    elif bmi <= 30.0:
        return "Overweight"
    elif bmi > 30:
        return "Obese"