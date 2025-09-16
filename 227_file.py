#copy image form one folder to another folder
file=open("C:\\Users\\WIN\\Desktop\\myfolder\\hello.png","rb")
data=file.read()
print(data)
file.close()
file= open("C:\\Users\\WIN\\Desktop\\mohit\\hello.png","wb")
file.write(data)
file.close()