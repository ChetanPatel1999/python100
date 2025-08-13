#here function call by reference
def fun(a):
   print(a)
   a[1]=900
   print(a)

num=[45,67,89]
fun(num)  
print(num) 