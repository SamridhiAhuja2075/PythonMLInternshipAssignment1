'''19. Write a python program that removes all punctuation from a given string.'''
string= input("Please enter a string : ")
list1=list()
punc="""!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"""
for i in string:
    if i not in punc:
        list1.append(i)
new_string=''.join(list1)
print(new_string)
