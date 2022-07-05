num = int(input("insert the number: "))
r_num = 0 
while num != 0:
    r_num *= 10
    r_num += num % 10
    num = num // 10
    
print(f'the reversed number is: {r_num}')
