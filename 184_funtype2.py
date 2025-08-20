#keyword argument types function calling

def add(a,b,c):
    print("a = ",a)
    print("b = ",b)
    print("c = ",c)
    sum=a+b+c
    print("sum = ",sum)  

def fullname(name,sirname):
    fullname=name+" "+sirname
    print(f"fullname = {fullname}")

def search_element_list(l1,ele): #12 34 56 78 90
    for i in l1:
        if i==ele:
            print("element is find")
            break
    else:
        print("element is not found")    

def printinfo(name,age,profession):
    print("name : ",name)
    print("age : ",age)
    print("profession : ",profession)
    print("----------------------------")

printinfo(age=34,name="ram",profession="doctor")   

add(b=12,c=5,a=10)   
fullname(sirname="patel",name="chetan") 
list1=[12,34,56,78,90]
search_element_list(ele=6,l1=list1)