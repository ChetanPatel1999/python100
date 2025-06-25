#wap to print even number serise 1 to given number.
n=int(input("enter a num :"))#20
i=1
print("even number serise : ",end="")
while i<=n:
    if i%2==0:
        print(i,end=" ")
    i+=1
# even number serise : 2 4 6 8 10