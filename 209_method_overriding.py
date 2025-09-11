#method overriding 
class parent:
    def display(self):
        print("parent display")
class child(parent):
    def display(self):   # method override
        print("child display")     


p1 = parent()
p1.display()

c1=child()
c1.display()
