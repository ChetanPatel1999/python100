#wap to print sum 1 to n number.
n=int(input("enter a num : "))#12
sum=0
for i in range(1,n+1):
    sum=sum+i

print(f"sum of 1 to {n} : ",sum)   
print(f"average of 1 to {n} = {sum/n}")