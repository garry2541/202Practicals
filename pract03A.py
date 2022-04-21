# Practical 03
# Regular Expression

import re
def find():
        str1 = "SitaRam"
        if re.search("ram$",str1):
            print("Ram Found in End of the string")
        else:
            print("Ram not found in End of the string")

        if re.search("^Sita",str1):
            print("Sita found in Start of the string")
        else:
            print("Sita not found in Start of the string")

def emailcheck(str):
                emailpattern="[a-zA-Z0-9(\.|\_)]+@(\w+\.)+(com|org|net|edu|co.in)"
                if (re.match(emailpattern,str)):
                    print("Email format is correct :)")
                else:
                    print("Email is incorrect!!")

def pincodecheck(str):
                pincodepattern="\d\d\d\d\d\d"
                if(re.match(pincodepattern,str) and len(str)==6):
                    print("pincode format is correct :)")
                else:
                    print("pincode is incorrect!!")

def phonenocheck(str):
                phonepattern="\+\d\d\-\d\d\d\d\d\d\d\d\d\d"
                if(re.match(phonepattern,str) and len(str)==14):
                   print("Phone number pattern is correct :)")
                else:
                    print("phone number is incorrect!!")

print("--Program to use regular expression--")
find()
emailcheck(input("Enter email id (abc@gmail.com): "))
pincodecheck(input("Enter pincode(401107): "))
phonenocheck(input("Enter phone number(+91-9842647541): "))