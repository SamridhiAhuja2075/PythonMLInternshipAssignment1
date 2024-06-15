'''25. Write a program that copies the contents of one text file to another.'''
'''For this program I am making use of text fill made  in Q5 and copying its contents to a new file'''
f1=open("Ques5.txt","r")
reader=f1.read()
f2=open("Ques25.txt","w")
f2.write(reader)
f1.close()
f2.close()
