def summ(a:float, b:float):
    """ summ returns the number of integers between a and b"""
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
    
print(summ(5.76, 8.5))
