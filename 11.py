#11. Write a python program that generates the first n numbers in theFibonacci sequence.
i=1
j=1
n=int(input("Enter the no. of fibonacci values to be presented :"))
print("The sequence of fibonacci till given value is :")
print(i)
print(j)
for m in range(1,n-1):
    k= i + j
    i=j
    j=k
    print(j)