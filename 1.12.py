def pascal(m, n):
   """ pascal finds the number of Pascal's triangle """
    if n in (m, 1):
        return 1 
    return pascal(m-1, n-1) + pascal(m-1, n)
   
m = int(input("insert m: ")
n = int(input("insert n: ")
print(f"The number is: {pascal(m, n)}")  
        
        
def pascal(m, n):
    return 1 if n in (1, m) else (pascal(m-1, n-1) + pascal(m-1, n))
   
m = int(input("insert m: ")
n = int(input("insert n: ")
print(f"The number is: {pascal(m, n)}") 
