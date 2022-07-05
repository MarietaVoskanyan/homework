def divisiors(num:int):
    i = 1
    div = []
    while i <= num:
        if num % i ==0:
            div.append(i)
        i += 1 
    return div
    
n = int(input("insert number"))
print(f'divisors of your number are: {divisiors(n)}')





