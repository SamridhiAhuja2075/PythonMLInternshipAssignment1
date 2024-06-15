'''14.  Write a program that reads multiple lines of input from the user until they
enter an empty line, then prints all the lines.'''
lines=list()
while True:
    line=input("Please enter a line :")
    if line == "":
        break
    else:
        lines.append(line)
for i in lines:
    print(i)
