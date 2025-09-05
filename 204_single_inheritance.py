#single inheritance
class Student:
    def setStudent(self,name,rno,per):
        self.name=name
        self.rno=rno
        self.per=per
    def getStudent(self):
        print("student info : ")
        print("student name : ",self.name)
        print("student rno : ",self.rno)
        print("student per : ",self.per)

class Btech(Student):
    def setBtech(self,branch,no_of_lacture):
        self.branch=branch
        self.no_of_lacture=no_of_lacture
    def getBtech(self):
        print("student Branch : ",self.branch)             
        print("student no_of_lacture : ",self.no_of_lacture)      

s1=Btech()
s1.setStudent("ram",101,89)
s1.setBtech("CS",7)
s1.getStudent()
s1.getBtech()
