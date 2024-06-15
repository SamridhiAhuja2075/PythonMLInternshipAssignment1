'''17. Write a program in python that converts a given string to title case (first
letter of each word capitalized).'''
string = input("Please enter a string : ")
word_list = string.split()
new_list=list()
for i in range (0,len(word_list)):
    k = word_list[i][0].upper()
    n=len(word_list[i])
    m = word_list [i][1:n]
    new_word = k + m
    new_list.append(new_word)
new_string=str()
for k in new_list:
    new_string=new_string+" "+k
print(new_string)
