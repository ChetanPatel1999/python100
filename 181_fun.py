#here function call by value
def fun(a):
   print(a)
   a=89
   print(a)


num=56
fun(num)  
print(num) 