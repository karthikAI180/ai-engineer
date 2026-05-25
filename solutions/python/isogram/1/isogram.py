def is_isogram(string):
    c=string.lower()
    k=[]
    for i in c:
        if i.isalpha() and i in k:
            return False
        k.append(i)
    return True
