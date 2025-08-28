class Student:
    def __init__(self,name,rno,per):
        self.name=name
        self.rno=rno
        self.per=per
    def setStudent(self,name,rno,per):
        self.name=name
        self.rno=rno
        self.per=per    
    def getStudent(self):
        print("Student info : ")
        print(f"student name : {self.name}")    
        print(f"student rno : {self.rno}")    
        print(f"student per : {self.per}") 
        return 67 

s1=Student("ram",101,89) 
s1.getStudent()  
s1.name="mohit"
s1.getStudent()
s1.setStudent("hariom",234,60)
s1.getStudent()
s2=Student("shyam",102,55)
s2.getStudent()

