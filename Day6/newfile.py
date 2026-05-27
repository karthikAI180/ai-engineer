# Program to print the Number of Lines, Words and Characters present in the given file
import os,sys
file_name=input("enter the name of the file")
if os.path.isfile(file_name):
    f=open(file_name,"r")
else:
    print("no file exist")
    sys.exit(0)
content=f.readlines()
characters=0
wordcount=0
for i in content:
    characters+=len(i)
    words=i.split(" ")
    wordcount+=len(words)
print("number of lines in the file are {}".format(len(content)))
print("number of characters in the file are {}".format(characters))
print("number of words in the file are {}".format(wordcount))
f.close()