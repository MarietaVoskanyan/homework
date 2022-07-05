def is_polindrom(n):
   if n[::1] == n[::-1]:
       return True
   else:
        return False
    
sentence = input("insert the sentence: ")
print(f'is your sentence polindrom? {is_polindrom(sentence)}')
