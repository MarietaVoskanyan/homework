def join(data, sep, count):
    """ Join returns the string consisting of the members of data that are connected to each other with sep"""
    string = ''
    for ind in range(len(data) - 1):
        string += data[ind]
    return string
    
data = []
i = 0
count = int(input("insert the count: "))
while i < count:
    mem = input("insert the member of the list: ")
    data.append(mem)

    sep = input("insert the sep: ")
    data.append(sep)
    i += 1
print(join(data, sep, count))
