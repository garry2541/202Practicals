# Practical 02
# Exception handling using try, except, else, finally

try:
    x = int(input("Enter a dividend: "))
    y = int(input("Enter a divisor: "))
except:
    print("Enter an integer number")

def divide(x,y):    
    try:
        result = x/y
    except ZeroDivisionError:
        print("Cannot divide a number by 0")
    else:
        print("Result: ",result)
    finally:
        print("Finally clause executes anyhow whether error occurs or not")

divide(x,y)