#read a file
file=open("abc.txt","r")
data=file.read() #read whole file
# data=file.read(10) #read only 10 character from file
print(data)
file.close()