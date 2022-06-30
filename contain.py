def is_contain(data, val):
    i = 0
    check = 'False'
    for i in range(len(data)):
        if data[i] == val:
            check = 'True'
    return check 
data = input("Insert data: ")
val = input("Insert val: ")
print(is_contain(data, val))
