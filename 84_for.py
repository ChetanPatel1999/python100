#wap to print sum 1 to n only even number.
n=int(input("enter a num : "))#12
sum=0
for i in range(1,n+1):
    if i%2==0:
        sum=sum+i
print(f"sum of 1 to {n} only even number = {sum}")        