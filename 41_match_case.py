#wap to print day name according to number.
num=int(input("enter a number for day : "))
match num:
    case 1:
        print("monday")
    case 2:
        print("tuesday")
    case 3:
        print("wednusday")
    case 4:
        print("thursday")
    case 5:
        print("friday")
    case 6:
        print("saturday")
    case 7:
       print("sunday")  
    case _:
        print("please enter 1 to 7 number")                                

    
