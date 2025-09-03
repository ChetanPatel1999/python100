#here we explain instance and class variable
class Student:
    totalpass=0                      #class variable
    totalfail=0                      #class variable
    totalstd=0                       #class variable
    collage="hello world institue"   #class variable
    def __init__(self ,name,rno,per):
        self.name=name   #instance variable
        self.rno=rno     #instance variable
        self.per=per     #instance variable
        Student.totalstd+=1
        if self.per>=33:
            Student.totalpass+=1
        else:
            Student.totalfail+=1    
    def resultCard(self):
        print("Student Result Card : ")
        print("collage name : ",Student.collage)
        print("name : ",self.name)
        print("rno : ",self.rno)
        print("per : ",self.per)
        if self.per>=33:
            print("student pass")
        else:
            print("student fail") 
        print("---------------------------") 
    def dispTotalResult():  #if we make a method which have insde only class varaible so that method not required self paramter or this type method is called by class name .
        print("Total Student : ",Student.totalstd)          
        print("Total Pass : ",Student.totalpass)          
        print("Total Fail : ",Student.totalfail)          

s1=Student("ram",101,23)
s2=Student("shyam",102,93)
s3=Student("ghanshyam",103,53)
s4=Student("hariom",104,80)

s1.resultCard()
s2.resultCard()
s3.resultCard()
s4.resultCard()

Student.dispTotalResult()
