#read a file
file=open("facto.txt","r")
data=file.readlines() #read lines read all lines and store in list than return list
print(data)
for i in data:
    print(i)
file.close()