#read a file
file=open("facto.txt","r")
data=file.readline() #read only one line
print(data)
file.close()