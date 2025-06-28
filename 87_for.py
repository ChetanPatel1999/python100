#wap to print factorial of given number.
# 5 --> 1*2*3*4*5 =  120
# 4 --> 1*2*3*4 =  24
n=int(input("enter a num : "))#5
fact=1
for i in range(1,n+1):
    fact=fact*i
print(f"fcatorial of {n} = {fact}")    