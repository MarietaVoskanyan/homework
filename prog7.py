def median(data:int):
    if len(data) % 2 == 0:
        return ((data[len(data) // 2] + (data[len(data) // 2 - 1])) // 2)
    else:
        return data[len(data) // 2]
    
    
data = input("Insert data: ")
print(median(data))
