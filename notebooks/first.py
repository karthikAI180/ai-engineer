#1Q. Write a program to display unique vowels present in the given word?
# vowels=['a','e','i','o','u']
# word=input("Enter the word to search for vowels: ")
# k=[]
# for i in word:
#     if i in vowels:
#         if i not in k:
#             k.append(i)
# print(k)

#2Q. Write a Python Function to find factorial of given number with recursion.
def fact(n):
    if n<1:
        return 1
    else:
        return n*fact(n-1)
print(fact(5))
