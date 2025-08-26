# python each method have a self parameter which  self parameter
# is used to store reference/address of current calling object. 
class Student:
    def setStudent(self,name,rno,per):
        self.name=name
        self.rno=rno
        self.per=per
    def getStudent(self):
        print("Student info : ")
        print(f"student name : {self.name}")    
        print(f"student rno : {self.rno}")    
        print(f"student per : {self.per}") 
    def hello(self):
        print("hello , hello ,hello")     

s1=Student() 
s1.setStudent("ram",101,89)
s1.getStudent()  
s1.hello()

s2=Student()
s2.setStudent("shyam",102,55)
s2.getStudent()


