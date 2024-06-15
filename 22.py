'''22. Write a python program that returns the minimum and maximum values
in a list of numbers.'''
n=int(input("Enter the no. of elements in the list  : "))
input_list=list()
for i in range(0,n):
    val=int(input("Enter a number : "))
    input_list.append(val)
max_value=max(input_list)
min_value=min(input_list)
print("Max Value : ",max_value)
print("Min Value : ",min_value)
