#wap to find greatest num between three number without using logical and operator.print  
num1=int(input("enter a num1 : "))#457
num2=int(input("enter a num2 : "))#123
num3=int(input("enter a num3 : "))#89
if num1>num2:
    if num1>num3:
        print(f"gretest num : {num1}")
    else:
        print(f"gretest num : {num3}")
else:
    if num2>num3:
        print(f"gretest num : {num2}")
    else:
        print(f"gretest num : {num3}")    