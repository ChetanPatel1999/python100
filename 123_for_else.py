#wap to check given num is prime or not.
num=int(input("enter a num :"))#444
c=0
if num==0 or num==1:
    print("not prime")
else:    
  for i in range(1,num+1):
    if num%i==0:
        c+=1 #3
    if c>2:
        print("not prime")  
        break    
  else:
    print("prime")            
  