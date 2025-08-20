#Requires argument types function

def add(a,b,c):
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

add(12,5,10)   
fullname("patel","chetan") 
list1=[12,34,56,78,90]
search_element_list(list1,6)