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

# ATM machines allow 4 or 6 digit PIN codes and PIN codes cannot contain anything but exactly 4 digits or exactly 6 digits.

# If the function is passed a valid PIN string, return true, else return false.

def validate_pin(pin):
    if pin.isdigit() and (len(pin) == 4 or len(pin) == 6):
        return True
    return False

# Given a list of integers, determine whether the sum of its elements is odd or even.

# Give your answer as a string matching "odd" or "even".

# If the input array is empty consider it as: [0] (array with a zero).

def odd_or_even(arr):
    for i in arr:
        if sum(arr) % 2 == 0:
            return "even"
        else:
            return "odd"
        

# Finish the solution so that it sorts the passed in array of numbers. If the function passes in an empty array or null/nil value then it should return an empty array.

def solution(nums):
    if not nums:
        return []
    else:
        return sorted(nums)
    
# Write a method that takes one argument as name and then greets that name, capitalized and ends with an exclamation point.

def greet(name): 
    return "Hello" + " " + name.capitalize() + "!"