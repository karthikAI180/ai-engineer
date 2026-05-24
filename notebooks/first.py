# Q. Write a program to display unique vowels present in the given word?
vowels=['a','e','i','o','u']
word=input("Enter the word to search for vowels: ")
k=[]
for i in word:
    if i in vowels:
        if i not in k:
            k.append(i)
print(k)
