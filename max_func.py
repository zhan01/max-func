def comparison (a,b):

    if a > b:
        return a
    else:
        return b

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print("-------------------")
print("\nThe Maximum Value is: " , max(a,b))