import random
def random_pass(n):
    passwd = ''
    i = 0
    while i < n:
        passwd = passwd + chr(random.randint(33, 126))
        i += 1 
    return passwd
  
n = input("Insert n: ")
print(random_pass(n))
