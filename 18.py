'''18.Write a python program that checks if two strings are anagrams of each
other.'''
string1=input("Enter string 1 : ")
string2=input("Enter string 2 : ")
list1=list()
list2=list()
for i in string1:
    list1.append(i)
for k in string2:
    list2.append(k)
list1.sort()
list2.sort()
if list1 == list2:
    print("Strings are anagrams")
else:
    print("Strings are not anagrams")


