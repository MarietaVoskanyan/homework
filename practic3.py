def is_ideal(num:int):
    i = 1 
    sum = 0 
    while i <= num // 2:
        if num % i == 0:
            sum += i
        i += 1
    return True if sum == num else False
        
n = int(input("insert number: "))
print(is_ideal(n))


def is_ideal(n):
        return sum([i for i in range(1, n) if n % i == 0]) == n

m = int(input("insert number: "))
print(is_ideal(m))
