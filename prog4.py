def even_id(lst):
    data = []
    ind = 0
    for ind in range(len(lst)):
        if lst[ind] % 2 == 0:
            data.append(ind)
    return data
      
lst = input("Insert list: ")
print(f'index is: {even_id(lst)}')
      

