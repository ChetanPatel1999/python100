#wap to find a digit in given number.
d=int(input("enter a digit : ")) # 7
num=int(input("enter a number : ")) #24
while num>0:
    rem=num%10
    if rem==d:
        print("found")
        break
    num=num//10    
else:
    print("not found")