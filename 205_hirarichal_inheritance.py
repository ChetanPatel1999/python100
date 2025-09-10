class Student:
    def setStudent(self,rno,name):
        self.rno=rno
        self.name=name
    def getStudent(self):
        print("student info : ")
        print("student name : ",self.name)
        print("student rno : ",self.rno)


class MathStudent(Student):
    def setMarks(self,math,pysics,chemistry):
        self.math=math
        self.pysics=pysics
        self.chemistry=chemistry
    def getMarks(self):
        print("marks : ")
        print("math : ",self.math)    
        print("pysics : ",self.pysics)    
        print("chemistry : ",self.chemistry)   

class CommerseStudent(Student):
    def setMarks(self,account,ip,bussiness):
        self.account=account
        self.ip=ip
        self.bussiness=bussiness
    def getMarks(self):
        print("marks : ")
        print("account : ",self.account)    
        print("ip : ",self.ip)    
        print("bussiness : ",self.bussiness)   

s1=MathStudent()
s1.setStudent(101,"ram") 
s1.setMarks(50,90,70)
s1.getStudent()
s1.getMarks()  
print("-----------------------------")  

s2=CommerseStudent()
s2.setStudent(1234,"shyam")
s2.setMarks(67,89,23)
s2.getStudent()
s2.getMarks()   
