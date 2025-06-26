#wap to count digit in given number.
num=int(input("enter a num : "))#464
print(f"digit count in number : {len(str(num))}") 
i=0
while num>0:
    i=i+1 #3
    num=num//10
print(f"digit count in number : {i}")    
  
