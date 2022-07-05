def func(tpl):
    m = len(tpl) - 1 
    number = 0
    for num in tpl:
        number += (num * (10 ** m))
        m -= 1 
    return number

tpl1 = input("insert the number: ")
print(f'number is: {func(tpl1)}')
