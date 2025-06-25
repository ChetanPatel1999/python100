#wap to print sum 1 to n .
n=int(input("enter a num : "))
i=1
sum=0
while i<=n:
    if i != n :
       print(i,end=" + ")
    else:
       print(i,end=" = ")  
    sum=sum+i  
    i=i+1 
print(sum)   

# 1+2+3+4+5 = 15
