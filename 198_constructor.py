#constructor example
class demo:
    def display(self):
        print("hi i am display")
    def __init__(self):  #constructor
        print("constructor1 is called")  
    def __init__(self,a,b):  #second constructor is override first constructor
        print("constructor2 is called")       

d1=demo(34,78)
d1.display()