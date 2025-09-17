#we can use multiple exception block
l1=[12,34,56,78,90]
try:
    a=int(input("enter a value : "))
    b=int(input("enter b value : "))
    index=int(input("enter index : "))
    ans=a/b
    print("result : ",ans)
    print("list element : ",l1[index])
except ZeroDivisionError:
    print("zero division error") 
except ValueError:
    print("input datatype error")
except IndexError:
    print("out of index error")     
except :
    print("some error is occured")       


print("programm run succefully1")
print("programm run succefully2")