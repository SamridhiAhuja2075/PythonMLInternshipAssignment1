#5. Write a program that takes a string input from the user and writes it to atext file.
val=input("Please enter a string : ")
f=open("Ques5.txt","w")
f.write(val)
f.close()