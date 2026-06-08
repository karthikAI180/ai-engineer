
"""1Q. Write a program to display unique vowels present in the given word?
vowels=['a','e','i','o','u']
word=input("Enter the word to search for vowels: ")
k=[]
for i in word:
    if i in vowels:
        if i not in k:
            k.append(i)
print(k)

2Q. Write a Python Function to find factorial of given number with recursion.
def fact(n):
    if n<1:
        return 1
    else:
        return n*fact(n-1)
print(fact(5))

3Q.Write a program to dispaly *'s in Right angled triangled form
*
* *
* * *
* * * *
* * * * *
* * * * * *
* * * * * * *
n=int(input("enter number of lines of pattern"))
for i in range(n+1):
    print("* "*i)



4Q.Write a program to display *'s in pyramid style(also known as equivalent triangle)
1) *
2) * *
3) * * *
4) * * * *
5) * * * * *
6) * * * * * *
7) * * * * * * *
n=int(input("enter number of lines of pattern"))
for i  in range(1,n+1):
    print(" "*(n-i),end="")
    print("* "*i)
"""