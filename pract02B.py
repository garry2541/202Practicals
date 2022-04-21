# Practical 02
# Raise exception

try:
    a = int(input("Enter a positive integer: "))
    b = int(input("Enter a positive integer: "))
    if (a<=0) or (b<=0):
        raise ValueError("Enter positive integers only")
    else:
        print("A = ",a)
        print("B = ",b)
        if a > b:
            print("Largest value:",a)
        else:
            print("Largest value:",b)

except ValueError as ve:
    print(ve)

finally:
    print("Finally clause executes anyhow whether error occurs or not")