'''15. Write a program that reads data from a CSV file and prints it to the
console.'''
import csv
file=open("Ques15.csv","r")
rd=csv.reader(file)
for i in rd:
    print(i)
