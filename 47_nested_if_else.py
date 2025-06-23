# club mini project
age=int(input("enter your age : "))#12
if age>=18:
    print("welcome to my club ....")
    print("club menue : ")
    print("1. noodles  : 60 ")
    print("2. sandwitch  : 120 ")
    print("3. cold coffe  : 80 ")
    order=int(input("please order : "))
    if order==1:
        print("your noodless is orderd please pay 60 rs")
    elif order==2:
        print("your sandwitch is orderd please pay 120 rs") 
    elif order==3:
        print("your cold coffe is orderd please pay 80 rs")  
    else:
        print("you enterd wrong number")      
else:
    print(f"you are not adult please try after {18-age} year")    
