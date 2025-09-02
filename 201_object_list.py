#how to make object list
class emp:
    def __init__(self):
        self.id=eval(input("enter emp id : "))
        self.sal=eval(input("enter emp sal : "))
    def getEmp(self):
        print("emp info : ")
        print("emp id : ",self.id)    
        print("emp sal : ",self.sal)  
        print("-------------------------") 

n=int(input("enter how many employ you want to store : "))
employs=[]
for i in range(n):
    e=emp()
    employs.append(e)

for e in employs:
    e.getEmp()



