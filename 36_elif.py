#Write a program to find greatest number among has given three numbers. 
num1=int(input("enter a num1 : "))
num2=int(input("enter a num2 : "))
num3=int(input("enter a num3 : "))
if num1>num2 and num1>num3:
    print(f"gretest num : {num1}")
elif num2>num3:
    print(f"gretest num : {num2}")
else:
    print(f"gretest num : {num3}")        