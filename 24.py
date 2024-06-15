'''24. Write a program that acts as a simple calculator. It should take two
numbers and an operator (+, -, *, /) as input and print the result.'''
n1=float(input("Enter number 1 : "))
n2=float(input("Enter number 2 : "))
op=input("Enter operator : ")
if op == "+":
    res = n1 + n2
    print("Result : ",res)
elif op == "-":
    res = n1 - n2
    print("Result : ",res)
elif op == "*":
    res = n1 * n2
    print("Result : ",res)
elif op == "/":
    res = n1 / n2
    print("Result : ",res)
else:
    print("Enter a valid operator!")

