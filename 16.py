'''16. Write a program in python that counts the frequency of each character in
a string.'''
string = input("Please enter a string: ")
char_freq = {}
for char in string:
    if char in char_freq:
        char_freq[char] += 1
    else:
        char_freq[char] = 1
print(char_freq)


