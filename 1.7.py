def pow(base, exp):
    """Pow finds the degree of the number no matter if degree is positive or negative """
    res = 1 
    count = 0
    if exp > 0:
        while count < exp:
            res = res * base
            count += 1 
        return res
    if exp < 0:
        if base != 0:
            while count < (-exp):
                res = res * base
                count += 1
            return 1 / res
        else:
            return "The phase is meaningless"
base = int(input("Insert base: "))
exp = int(input("Insert exp: "))
print(f"The degree is: {pow(base, exp)}")

