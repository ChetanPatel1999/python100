#example of short hand if else

# age=int(input("enter you age : "))#6
# print("you can vote") if age>=18 else print("you cant vote") 


# num1=int(input("enter num1 : "))
# num2=int(input("enter num2 : "))
# print(f"gretates num :{num1}") if num1>num2 else print(f"gretates num :{num2}")


# num1 = int(input("enter num1 : "))
# num2 = int(input("enter num2 : "))
# ans = num1 if num1>num2 else num2
# print(f"gretates num :{ans}")


# age=int(input("enter you age : "))#6
# res = "you can vote" if age>=18 else "you cant vote" 
# print(res)


# num=int(input("enter a num :"))
# res= "positive" if num>0 else "nagative"
# print(res)

# num=int(input("enter a num :"))
# res= "positive" if num>0 else "nagative" if num<0 else "zero"
# print(res)


# num1=int(input("enter a num1 : "))#457
# num2=int(input("enter a num2 : "))#123
# num3=int(input("enter a num3 : "))#89
# res= num1 if num1>num2 and num1>num3 else num2 if num2>num3 else num3
# print(res)

num1=int(input("enter a num1 : "))#457
num2=int(input("enter a num2 : "))#123
num3=int(input("enter a num3 : "))#89
num4=int(input("enter a num4 : "))#89
res= num1 if num1>num2 and num1>num3 and num1>num4 else num2 if num2>num3 and num2>num4 else num3 if num3>num4 else num4
print(res)









