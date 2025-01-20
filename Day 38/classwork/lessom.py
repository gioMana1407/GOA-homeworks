
# Description
# Your job is to create a simple password validation function, as seen on many websites.

# The rules for a valid password are as follows:

# There needs to be at least 1 uppercase letter.
# There needs to be at least 1 lowercase letter.
# There needs to be at least 1 number.
# The password needs to be at least 8 characters long.

def password(st):
    if len(st) < 8:
        return False 
    
    has_lower = 0
    has_upper = 0
    has_digit = 0
    
    for char in st:
        if char.islower():
            has_lower = 1
        if char.isupper():
            has_upper = 1
        if char.isdigit():
            has_digit = 1
    
    if has_lower and has_upper and has_digit:
        return True
    else:
        return False




# An isogram is a word that has no repeating letters, consecutive or non-consecutive. Implement a function that determines whether a string that contains only letters is an isogram. Assume the empty string is an isogram. Ignore letter case.

def is_isogram(string):
    for i in string.lower():
        if string.lower().count(i) > 1:
            return False
    return True

