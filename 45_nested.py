#wap to check voter is casting vote in india or not.
country=input("enter your country :")
if country=="india":
    age=int(input("enter you age : "))
    if age>=18:
        print("you can vote in india")
    else:
        print("you are not eligible")    
else:
    print("you are not indian")