#wap to print sum 1 to n .
n=int(input("enter a num : "))
i=1
sum=0
while i<=n:
    if i%2==0:
       sum=sum+i  
    i=i+1 
print(f"even number sum from 1 to {n} = {sum}")

