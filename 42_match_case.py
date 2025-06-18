#wap to print state name according to state sort name.
state=input("enter short name of state : ")
match state:
    case "mp":
        print("madhya pradesh")
    case "rj":
        print("rajsthan")
    case "gj":
        print("gujrat") 
    case "mh":
        print("maharastra")  
    case _ :
        print("wrong short name")         