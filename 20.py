'''20. Write a python program that takes a list of numbers and returns their sum'''
n=int(input("Enter the no. of elements in the list  : "))
input_list=list()
for i in range(0,n):
    val=int(input("Enter a number : "))
    input_list.append(val)
sum = 0
for i in input_list:
    sum = sum + i
print("Sum : ",sum)
