#wap to generate factorial of given numbers and write into a file.
n=int(input("enter a num : ")) # 5
file1=open("facto.txt","a")
fact=1
for i in range(1,n+1):
    fact=fact*i
print(f"factorial of {n} = {fact}")   
file1.write(f"factorial of {n} = {fact}\n") 
file1.close()
