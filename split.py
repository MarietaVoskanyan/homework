def split(source, sep, count):
	""" Split returns the list consisting of the subjects of source """
	lst = []
	i = 0
	j = 0
	while j <= len(source):
	    name = ''
	    for ind in range(len(source)):
	        if source[ind] == sep:
	            i = ind
	        else:
	            name += source[ind]
	    lst.append(name)
	    string = ''
	    for index in range(i + 1, len(source)):
	        string += source[index]
	    source = string
	    j += 1 
	return lst
	
string = input("insert string: ")
count = input("insert count: ")
print(f"the list consists of the string is: {split(string, ',')}")
