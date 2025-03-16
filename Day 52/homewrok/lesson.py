# Your goal is to return multiplication table for number that is always an integer from 1 to 10.

# For example, a multiplication table (string) for number == 5 looks like below:

# 1 * 5 = 5
# 2 * 5 = 10
# 3 * 5 = 15
# 4 * 5 = 20
# 5 * 5 = 25
# 6 * 5 = 30
# 7 * 5 = 35
# 8 * 5 = 40
# 9 * 5 = 45
# 10 * 5 = 50
# P. S. You can use \n in string to jump to the next line.

# Note: newlines should be added between rows, but there should be no trailing newline at the end. If you're unsure about the format, look at the sample tests.

def multi_table(number):
    table = ""
    for i in range(1, 11):
        table += f"{i} * {number} = {i * number}\n"
    return table.strip()

# Input: Array of elements

# ["h","o","l","a"]

# Output: String with comma delimited elements of the array in th same order.

# "h,o,l,a"

# Note: if this seems too simple for you try the next level

# Note2: the input data can be: boolean array, array of objects, array of string arrays, array of number arrays... 😕
def print_array(arr):
    result = ""
    for i in arr:
        result += str(i) + ","
    return result[:-1]


# String cleaning
def string_clean(s):
    result= ""
    for i in s:
        if not i.isdigit():
            result += i
    return result
        
# Remove consecutive duplicate words

def remove_consecutive_duplicates(s):
    words = s.split()  
    result = []  
    last_word = ""   
    for i in words:
        if i != last_word:  
            result.append(i)  
            last_word = i    
    return " ".join(result)  

# Between Extremes

def between_extremes(numbers):
    return max(numbers) - min(numbers)



