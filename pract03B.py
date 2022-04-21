# Practical 03
# Regular Expression

from re import *
str = "Global Warming"
print(str)

print("Last 4 characters: ")
last4 = findall("\D\D\D\D$", str)
for ch in last4:
    print(ch)

print("Characters starting from index 4 and ending at index 8: ")
mid = findall("^....(.....)", str)
for ch in mid:
    print(ch)

print("String contains Alphanumeric character or not: ")
if match("^(0-9A-Za-z)*$", str):
    print("True")
else:
    print("False")

print("Trim Last 4 characters: ")
str1 = sub("\D\D\D\D$", " ", str)
print(str1)

print("Trim First 4 characters: ")
str2 = sub("^\D\D\D\D", " ", str)
print(str2)

print("Index of Wa in",str ,":")
i = str.index("Wa")
print(i)

print("change case to Title: ")
str3 = str.title()

# print("Check whether string is in Title case: ")
# if(match("^[A-Z][a-z]*\s[a-Z][a-z]*", str)):
#     print(str, "is in Title case")
# else:
#     print(str, "is not in Title case")

print("Replace all letter 'a' in the string with '*'")
str4 = sub("a","*",str)
print(str4)