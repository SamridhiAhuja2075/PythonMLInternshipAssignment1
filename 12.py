#12. Write a python program that calculates the sum of the digits of a given number.
n=int(input("Please enter a number :"))
num_str=str(n)
res=0
for i in num_str:
    k=int(i)
    res=res+k
print("Sum of digits : ",res)