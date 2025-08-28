class emp:
    def __init__(self):
        self.id=eval(input("enter emp id : "))
        self.sal=eval(input("enter emp sal : "))
    def getEmp(self):
        print("emp info : ")
        print("emp id : ",self.id)    
        print("emp sal : ",self.sal)    

e1=emp()
e1.getEmp()

e2=emp()
e2.getEmp()