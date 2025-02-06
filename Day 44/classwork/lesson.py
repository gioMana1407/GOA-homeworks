# Count by X

def count_by(x, n):
    result = []
    for i in range(1, n + 1):
        result.append(x * i)
    return result
    

# Get Planet Name By ID

def get_planet_name(id):
    name = ""
    if id == 1:
        name = "Mercury"
    elif id == 2:
        name = "Venus"
    elif id == 3:
        name = "Earth"
    elif id == 4:
        name = "Mars"
    elif id == 5:
        name = "Jupiter"
    elif id == 6:
        name = "Saturn"
    elif id == 7:
        name = "Uranus"
    elif id == 8:
        name = "Neptune"
    return name

# Cat years, Dog years

def human_years_cat_years_dog_years(humanYears):
    if humanYears == 1:
        catYears = 15
        dogYears = 15
    elif humanYears == 2:
        catYears = 24
        dogYears = 24
    else:
        catYears = 24 + (humanYears - 2) * 4
        dogYears = 24 + (humanYears - 2) * 5
    
    return [humanYears, catYears, dogYears]

# Twice as old

def twice_as_old(dad_years_old, son_years_old):
    result = 2 * son_years_old - dad_years_old
    if result < 0:
        return -result
    return result



