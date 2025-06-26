#wap to print sum of individual digit of given number.
num=int(input("enter a num : "))#345
sum=0
while num>0:
    rem=num%10
    sum=sum+rem
    num=num//10
print(f"sum of individula digit of given num : {sum}")    

