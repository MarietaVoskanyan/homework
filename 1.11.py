def fib(n):
    """ fib returns the sum of previous three numbers"""
    if n in (0, 1, 2):
        return n 
    return fib(n-1) + fib(n-2) + fib(n-3)
