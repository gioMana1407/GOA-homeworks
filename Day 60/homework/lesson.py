# Write a function, nicknameGenerator that takes a string name as an argument and returns the first 3 or 4 letters as a nickname.

# If the 3rd letter is a consonant, return the first 3 letters.

def nickname_generator(name):
    if len(name) < 4: return "Error: Name too short"
    if name[2] not in "aeiou":
        return name[0:3]
    return name[0:4]

# In this kata you have to correctly return who is the "survivor", ie: the last element of a Josephus permutation.

# Basically you have to assume that n people are put into a circle and that they are eliminated in steps of k elements, like this:

def josephus_survivor(n,k):
    n_list = list(range(1,n +1))
    index = (k - 1)
    while len(n_list) > 1:
        while index >= len(n_list):
            index = index - len(n_list)
        del n_list[index % n]
        index += k - 1
    return n_list[0]

