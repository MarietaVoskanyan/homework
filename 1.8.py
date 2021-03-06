def sqrt(n):
    """ Sqrt counts the cubic of a number """
	root = 1
	while not guess_enough(root, n):
		root = improve(root, n)
	return root
	
def guess_enough(value, target):
	if abs(value**3 - target) < 0.0000001:
		return True
	else:
		return False
def abs(n):
	if n > 0:
		return n
	else:
		return -n
def improve(root, target):
	return ((target / (root ** 2)) + (2 * root)) / 3
	

n = int(input("Insert the number: "))
print(f"The cubic is: {sqrt(n)}")
