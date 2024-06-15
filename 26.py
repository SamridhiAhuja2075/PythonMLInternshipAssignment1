'''26. Write a program in python that checks if a string starts with a given prefix
or ends with a given suffix.'''
main_string = input("Enter main string : ")
check_string=input("Enter string to check suffix of prefix for : ")
checker=1
if len(main_string) > len(check_string):
    #checking for prefix
    for i in range(len(check_string)):
        if main_string[i] != check_string[i]:
            checker=0
    if checker == 0:
            print("Check string is not in prefix")
    else:
            print("Check string is in prefix")
    #checking for suffix
    for i in range(1, len(check_string) + 1):
        if main_string[-i] != check_string[-i]:
            checker = 0
    if checker == 0:
            print("Check string is not in suffix")
    else:
            print("Check string is in suffix")


