# Default argument: 

def add(a,b,c=50):
    sum=a+b+c
    print("sum = ",sum)

def totalbill(quantity,price=10):
    totalbill=quantity*price
    print("total bill :",totalbill)

def fullname(name , sirname="sharma"):
    fullname=name+" "+sirname
    print("fullname : ",fullname)    

add(12,10)  
totalbill(10)  
fullname("ram","anjana")
fullname("shyam")
n=input("enter name : ")
s=input("enter sirname : ")
fullname(n,s)