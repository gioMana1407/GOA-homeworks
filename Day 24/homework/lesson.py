# 1) split() ფუნქიცია დაწერეთ split() ფუნქციის გარეშე
text = "giorgi manashvili "
result = []
result2 = ""

for char in text:
    if char == " ":
        if result2:
            result.append(result2)
            result2 = ""
    else:
        result2 += char
print(result)

if result2:
    result.append(result2)
# 2) join() ფუნქიცია დაწერეთ join() ფუნქციის გარეშე


join_func = ["a","b","c"]
string = ""
for i in join_func:
    string += i
print(string)

# replace() ფუნქიცია დაწერეთ replace() ფუნქციის გარეშე

replace = ["irakli","batoni","irakli1"]
replace[0] = "replaced"
print(replace)

# 4) mini function of calculator 
# num1 = int(input("raime ricxvi: "))
# num2 = int(input("raime ricxvi: "))
# operation = input("airchiet operacia: ")

# if operation == "+":
#     print(num1 + num2)
# elif operation == "-":
#     print(num1 - num2)
# elif operation == "*":
#     print(num1 * num2)
# elif operation == "/":
#     print(num1 / num2)


# 5) input ები გამოყენებით, დავამტოთ იმდენი სიტყვა რმადენიც მომხარებეს სურს და ეს სიტყვეი მოვაქციოთ array ში 
# დავაჯოინოთ და გამოვიტანოთ ტერმინალში 

name = input("dawere rame: ")
name1 = input("dawere rame: ")
arr = []

arr.append(name,)
arr.append(name1,)
print(arr)

