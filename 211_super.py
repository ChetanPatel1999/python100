#using super function we call base class constructor and methods
class student:
    def __init__(self, name):
        self.name=name
    def display(self):
        print("name : ",self.name)

class btech(student):
    def __init__(self,name,branch):
        super().__init__(name)
        self.branch=branch
    def display(self):
        super().display()
        print("brach : ",self.branch)   

s1=btech("ram","cs")
s1.display()