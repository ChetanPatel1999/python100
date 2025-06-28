#wap to print factors of given number.
n=int(input("enter a num : "))#15
print(f"factors of {n} = ",end="")
for i in range(1,n+1):
    if n%i==0:
        print(i,end=" ")