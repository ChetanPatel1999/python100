class A:
    def greet(self):
        print("good morning")

class B:
    def greet(self):
        print("good after noon")

class C(B,A): 
    pass

o1=C()
o1.greet()  # its call greet method of class B bacause at time of inheritance frist class is B

