#wap to check given num is prime or not.
num=int(input("enter a num :"))#15
c=0
for i in range(1,num+1):
    print(i)
    if num%i==0:
        c+=1
    if c>2:
        break
if c==2:
    print("prime number")
else:
    print("not prime")      