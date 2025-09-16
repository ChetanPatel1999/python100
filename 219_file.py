# append mode :- append data inside file
file1=open("C:\\Users\\WIN\\Desktop\\mohit\\xyz.txt","a")
s="hi i am string variable"
file1.write("hello i am chetan\n")
file1.write("and i am teacher\n")
file1.write(s+"\n")
file1.close()
