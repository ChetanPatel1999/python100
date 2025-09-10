#multiple inheritance
class addition:
    def add(self,a,b):
        print("sum = ",a+b)

class subtraction:
    def sub(self,a,b):
        print("sub = ",a-b)

class multiplication:
    def mul(self,a,b):
        print("mul = ",a*b)  

class calculator(addition,subtraction,multiplication):
    def all_operation(self,a,b):
        super().add(a,b)  # super keyword is used to call base class method from child class
        self.sub(a,b)
        self.mul(a,b)             

c1=calculator()
c1.add(12,56)
c1.sub(12,5)
c1.mul(12,3)
c1.all_operation(6,3)

