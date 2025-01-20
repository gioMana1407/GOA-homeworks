# Implement a function which convert the given boolean value into its string representation.

def boolean_to_string(b):
    return str(b)

# Your task is to create a function that does four basic mathematical operations.

# The function should take three arguments - operation(string/char), value1(number), value2(number).
# The function should return result of numbers after applying the chosen operation.

def basic_op(operator, value1, value2):
    if operator == "+":
        return (value1 + value2)
    if operator == "-":
        return (value1 - value2)
    if operator == "*":
        return (value1 * value2)
    if operator == "/":
        return (value1 / value2)
    

# Given an array of integers, return a new array with each value doubled.

def maps(a):
    result = []
    for i in a:
        result.append(i * 2)
    return result
    
# Given a random non-negative number, you have to return the digits of this number within an array in reverse orde
def digitize(n):
    array = []
    for i in str(n):
        array.append(int(i))
    return array[::-1]

# Write a function to convert a name into initials. This kata strictly takes two words with one space in between them.

# The output should be two capital letters with a dot separating them.

def abbrev_name(name):
    name_list = name.split()
    name_0 = name_list[0][0].upper()
    surname_0 = name_list[1][0].upper()
    return name_0 + "." + surname_0