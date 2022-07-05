name = input("insert the name: ")
rev_name = [None] * len(name)
ind = 0
ind1 = len(name) - 1
while ind1 >= 0:
    rev_name[ind] = name[ind1]
    ind += 1 
    ind1 -= 1 
num2 =''
for num in rev_name:
    num2 = num2 + num 
    
print(f'reversed string is: {num2}')
