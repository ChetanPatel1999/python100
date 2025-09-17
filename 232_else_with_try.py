#exception handling program 
a=int(input("enter a value : "))
b=int(input("enter b value : "))
try:
    ans=a/b
except ZeroDivisionError as e:
    print("error :",e)
else:
    print("result : ",ans)
finally:
    print("file close succefully")    
print("programm run succefully")