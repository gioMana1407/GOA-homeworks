# Your task is to remove all duplicate words from a string, leaving only single (first) words entries.

def remove_duplicate_words(s):
    result = []
    words = s.split(" ")
    for i in words:
        if i not in result:
            result.append(i)
    return " " .join(result)

# You are given an odd-length array of integers, in which all of them are the same, except for one single number.

# Complete the method which accepts such an array, and returns that single different number.

def stray(arr):
    for i in arr:
        if arr.count(i) == 1:
            return i
        
# Finish the solution so that it sorts the passed in array of numbers. If the function passes in an empty array or null/nil value then it should return an empty array.

def solution(nums):
    if not nums:
        return []
    else:
        return sorted(nums)
    
# Write a function that takes a single non-empty string of only lowercase and uppercase ascii letters (word) as its argument, and returns an ordered list containing the indices of all capital (uppercase) letters in the string.

def capitals(word):
    capital = []
    for i,char in enumerate(word):
        if char.isupper():
            capital.append(i)
    return capital

# Your task is to write function factorial.

def factorial(n):
    if n <= 0:
        return 1 
    else:
        return n * factorial(n-1)
    