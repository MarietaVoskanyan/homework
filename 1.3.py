def sum_of_max(a, b, c):
    if a>b>c or b>a>c:
        return (a**2 + b**2)
    elif a>c>b or c>a>b:
        return (a**2 + c**2)
    elif b>c>a or c>b>a:
        return (c**2 + b**2)
        
print(sum_of_max(4, 2, 3))
