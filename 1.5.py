def summ(a, b):
    """ summ returns the sum of numbers of integers between a and b"""
    c = 0
    d = 0
    while a > c:
        c += 1 
    m = c 
    while b > d:
        d += 1
    n = d - 1 
   
    k = 0
    sum = 0
    while (k + m) <= n:
        sum += (m + k)
        k += 1 
    return sum
a = float(input("Insert a: ")) 
b = float(input("Insert b: ")) 

print(f" The number is: {summ(a, b)}")
