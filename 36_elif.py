#Write a program to find greatest number among has given three numbers. 
num1=int(input("enter a num1 : "))#457
num2=int(input("enter a num2 : "))#123
num3=int(input("enter a num3 : "))#89
if num1>num2 and num1>num3:
    print(f"gretest num : {num1}")
if num2>num3 and num2>num1:
    print(f"gretest num : {num2}")
if num3>num1 and num3>num2:
    print(f"gretest num : {num3}")      