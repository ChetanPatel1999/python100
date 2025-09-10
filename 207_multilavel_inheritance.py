#multilavel inheritance
class emp:
    def setemp(self,id,sal):
        self.id=id
        self.sal=sal

class programmer(emp):
    def setprgm(self,lang):
        self.lang=lang 

class Prgm_manager(programmer):
    def setprgm_manager(self,no_emp):
        self.no_emp=no_emp 
    def getmanager(self):
       print("programmer manager info :")
       print("id : ",self.id)   
       print("sal : ",self.sal)   
       print("lang : ",self.lang)   
       print("no_emp : ",self.no_emp)   

m1=Prgm_manager()
m1.setemp(101,40000)
m1.setprgm("python")
m1.setprgm_manager(5)
m1.getmanager()
