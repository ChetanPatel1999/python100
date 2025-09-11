#super function
class parent:
    def display(self):
        print("parent display")
class child(parent):
    def display(self):
        print("child display") 
        super().display()     

c1=child()
c1.display()
