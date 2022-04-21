# Practical 01
# Program to count upperCase, lowerCase and digits in a file

# Try this Online compiler for this program
# https://www.online-python.com/

import os
f = open("01Bcontent.txt", "r")
data = f.read()
ucase = 0
lcase = 0
digits = 0

for ch in data:
    if ch.islower():
        lcase += 1
    if ch.isupper():
        ucase += 1
    if ch.isdigit():
        digits += 1

print("lowerCase: ",lcase)
print("uperCase: ",ucase)
print("digits: ",digits)