def is_pangram(sentence):
    s=sentence.lower()
    k=[]
    for i in s:
        if i not in k and i.isalpha():
            k.append(i)
    if len(k)==26:
        return True
    return False
    pass
