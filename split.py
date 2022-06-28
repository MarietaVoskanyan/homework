def split(source, sep):
        i = 0  
        lst = []
        str = ''
        for i in range(len(source)):
            if source[i] != sep:
                str += source[i]
            else:
                lst.append(str)
                str = ''
        return lst
    
sep = input("insert the sep: ") 
source = input("insert the source: ")
print(f"the new source is: {split(source, sep)}")
