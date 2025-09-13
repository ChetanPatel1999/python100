from random import choice
print("<---- rock papper Sccissor Game--->")
print("enter your choise:")
print("1. rock")
print("2. papper")
print("3. sccissor")
num=int(input("pick your choise : ")) #2
dict1={1:"rock",2:"papper",3:"sccissor"}
user_choice=dict1[num]
choises=["rock","papper","sccissor"]
computer_choise=choice(choises)
print("your choise : ",user_choice)
print("computer choise : ",computer_choise)
if user_choice==computer_choise:
    print("match is draw!")
elif user_choice=="rock":
    if(computer_choise=="sccissor"):
        print("you win! ") 
    else:
        print("computer win! ")
elif user_choice=="papper":
    if(computer_choise=="rock"):
        print("you win! ") 
    else:
        print("computer win! ")
else:
     if(computer_choise=="papper"):
        print("you win! ") 
     else:
        print("computer win! ")               

