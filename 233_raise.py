#raise error
x=int(input("enter a value : "))
try:
 if x<0:
    raise Exception("nagative value error")
except Exception as e:
  print(e) 
else:
  print("value = ",x)
print("program run succefully")