#3. Write a python program that calculates the factorial of a given number.
a=int(input("Please enter a number : "))
res=1
for i in range(1,a+1):
    res=res*i
print("Factorial of",a,":",res)