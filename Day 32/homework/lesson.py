# Write a function to split a string and convert it into an array of words.

def string_to_array(s):
    if s:
        return s.split()
    else:
        return [""]
    
# We need a function that can transform a string into a number. What ways of achieving this do you know?

def string_to_number(s):
    return int(s)

# We need a function that can transform a string into a number. What ways of achieving this do you know?

def string_to_number(s):
    return int(s)

# Given a string of digits, you should replace any digit below 5 with '0' and any digit 5 and above with '1'. Return the resulting string.

def fake_bin(x):
    stringg = ""
    for char in x:   
        if int(char) < 5:
            stringg += "0"
        else:
            stringg += "1"
    return stringg

# In this little assignment you are given a string of space separated numbers, and have to return the highest and lowest number.
def high_and_low(numbers):
    string_list = numbers.split()
    num_list = []
    for i in string_list:
        num_list.append(int(i))
    highest = max(num_list)
    lowest = min(num_list)
    highest_str = str(highest)
    lowest_str = str(lowest)
    result = highest_str + " " + lowest_str
    return result
    