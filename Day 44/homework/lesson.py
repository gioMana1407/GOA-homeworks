# ATM machines allow 4 or 6 digit PIN codes and PIN codes cannot contain anything but exactly 4 digits or exactly 6 digits.

# If the function is passed a valid PIN string, return true, else return false.

def validate_pin(pin):
    if pin.isdigit() and (len(pin) == 4 or len(pin) == 6):
        return True
    return False

# Sum of odd numbers

def row_sum_odd_numbers(n):
    return n ** 3

# Eg: [0, 0, 0, 1] is treated as 0001 which is the binary representation of 1.

def binary_array_to_number(arr):
    decimal_number = 0
    for i in arr:
        decimal_number = decimal_number * 2 + i
    return decimal_number 

# Write a function that returns both the minimum and maximum number of the given list/array.

def min_max(lst):
    minimum_max = [min(lst), max(lst)]
    return minimum_max

# Create a function named divisors/Divisors that takes an integer n > 1 and returns an array with all of the integer's divisors(except for 1 and the number itself), from smallest to largest. If the number is prime return the string '(integer) is prime' (null in C#, empty table in COBOL) (use Either String a in Haskell and Result<Vec<u32>, String> in Rust).

def divisors(integer):
    result = [] 
    for i in range(2, integer):
        if integer % i == 0:
            result.append(i)
    if result:
        return result
    else:
        return f"{integer} is prime"