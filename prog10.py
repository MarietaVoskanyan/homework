def same_parity(n, *args):
    lst = []
    num = 0
    for num in args:
        if num % n == 0:
            lst.append(num)
    return lst


n = int(input("Insert n: "))
args = input("Insert args: ")
print(same_parity(n, *args))




