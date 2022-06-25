def sum_of_max_squares(a, b, c):
    
    """ sum_of_max finds out the biggest two numbers and prints the sum of their squares """
    if c < b < a or c < a < b:
        return (a**2 + b**2)
    elif b < c < a or b < a < c:
        return (a**2 + c**2)
    elif a < c < b or a < b < c:
        return (c**2 + b**2)
        
print(sum_of_max_squares(4, 2, 3))
