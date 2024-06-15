'''21. Write a python program that counts the occurrences of a specific element
in a list.'''
input_string=input("Please enter a string : ")
element=input("Enter  the element you want to count for : ")
counter=0
for i in input_string:
    if i == element :
        counter=counter+1
print("No. of occurences : ",counter)
