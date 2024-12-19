# You get an array of numbers, return the sum of all of the positives ones.

def positive_sum(arr):
    nums = []
    for i in arr:
        if i >= 0:
            nums.append(i)
    return sum(nums)

# Complete the square sum function so that it squares each number passed into it and then sums the results together.

def square_sum(numbers):
    square = []
    for i in numbers:
        square.append(i * i)
    return sum(square)
            
# Write a function that takes an array of numbers and returns the sum of the numbers. The numbers can be negative or non-integer. If the array does not contain any numbers then you should return 0.

def sum_array(a):
    return sum(a)

# Write a function which calculates the average of the numbers in a given array.

def find_average(numbers):
    if numbers == []:
        return 0
    return sum(numbers) / len(numbers)

# Given an array of integers.

# Return an array, where the first element is the count of positives numbers and the second element is sum of negative numbers. 0 is neither positive nor negative.

# If the input is an empty array or is null, return an empty array.

def count_positives_sum_negatives(numbers):
    if numbers == []:
        return []
    positive = 0
    negative = 0
    for i in numbers:
        if i > 0:
            positive += 1
        elif i < 0:
            negative += i
    return [positive,negative]