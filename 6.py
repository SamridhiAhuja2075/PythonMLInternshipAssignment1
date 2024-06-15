#6. Write a program that reads the content of a text file and prints it to theconsole.
f=open("Ques5.txt","r")
reader=f.readlines()
for i in reader:
    print(i)
f.close()
