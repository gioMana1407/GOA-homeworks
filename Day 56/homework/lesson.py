# Nickname Generator

# Write a function, nicknameGenerator that takes a string name as an argument and returns the first 3 or 4 letters as a nickname.
# If the 3rd letter is a consonant, return the first 3 letters.

def nickname_generator(name):
    if len(name) < 4: return "Error: Name too short"
    if name[2] not in "aeiou":
        return name[0:3]
    return name[0:4]