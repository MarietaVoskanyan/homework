def sum_of_min_max(data):
     
    max = data[0]
    min = data[0]
   for num in data:
       if num > max:
           max = num
        if num < min:
            min = num
    sum = max + min
    return sum
    
data = (input("the data: "))
print(f'The sum of data is {sum_of_min_max(data)}')
