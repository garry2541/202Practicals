# Practical 01
# Program to accept text from user and write conent to a file

# Try this Online compiler for this program
# https://www.online-python.com/

import os
def makefile(fn):
    fyle = open(fn, "w")
    content = input("Enter some content:\n")
    fyle.write(content)
    fyle.close()

print("Program to accept content from user and write it in a file")
s = " "
fname = " "
while (s!= ".txt"):
    fname = input("Enter a file name: ")
    fextension = os.path.splitext(fname)
    s = fextension[1]
    if s == ".txt":
        break
    else:
        print("Enter a txt file: ")

makefile(fname)
print("File created")