def min_max(_str):
    res = _str.split() 
    arr = []
    for i in res:
        arr.append(int(i))  

    max_num = max(arr)
    min_num = min(arr)
    return f" {min_num}, {max_num}"

print(min_max("1 2 3 4 5"))