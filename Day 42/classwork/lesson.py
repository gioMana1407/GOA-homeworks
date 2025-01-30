# Our football team has finished the championship.

# Our team's match results are recorded in a collection of strings. Each match is represented by a string in the format "x:y", where x is our team's score and y is our opponents score.

# For example: ["3:1", "2:2", "0:1", ...]

# Points are awarded for each match as follows:

# if x > y: 3 points (win)
# if x < y: 0 points (loss)
# if x = y: 1 point (tie)
# We need to write a function that takes this collection and returns the number of points our team (x) got in the championship by the rules given above.

def points(games):
    result = 0
    for i in games:
        goal = i.split(":")
        x = int(goal[0])
        y = int(goal[1])
        if x > y:
            result += 3
        elif x == y:
            result += 1
    return result

# Given a string of digits, you should replace any digit below 5 with '0' and any digit 5 and above with '1'. Return the resulting string.

def fake_bin(x):
    final = ""
    for i in x:
        if int(i) >= 5:
            final += "1"
        else:
            final += "0"
    return final

# Deoxyribonucleic acid, DNA is the primary information storage molecule in biological systems. It is composed of four nucleic acid bases Guanine ('G'), Cytosine ('C'), Adenine ('A'), and Thymine ('T').

# Ribonucleic acid, RNA, is the primary messenger molecule in cells. RNA differs slightly from DNA its chemical structure and contains no Thymine. In RNA Thymine is replaced by another nucleic acid Uracil ('U').

# Create a function which translates a given DNA string into RNA.

def dna_to_rna(dna):
    return dna.replace('T', 'U')

# Messi is a soccer player with goals in three leagues:

# LaLiga
# Copa del Rey
# Champions
# Complete the function to return his total number of goals in all three leagues.

def goals(laLiga, copaDelRey, championsLeague):
    return laLiga + copaDelRey + championsLeague

