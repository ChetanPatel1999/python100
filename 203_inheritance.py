#example of inheritance
class A:
    def m1(self):
        print("class A m1 is called")
    def m2(self):
        print("class A m2 is called")    

class B(A):
    def m3(self):
        print("class B m3 is called")
    def m4(self):
        print("class B m4 is called")       

o1=A()  
o1.m1()
o1.m2()   
print("------------------------") 
o2=B()
o2.m1() 
o2.m2() 
o2.m3() 
o2.m4() 