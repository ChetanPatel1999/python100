# Variable-Length Arguments 
# We can use special characters in Python functions to pass as many arguments as we want 
# in a function. There are two types of characters that we can use for this purpose:  
# 1. *args -These are Non-Keyword Arguments  
# 2. **kwargs - These are Keyword Arguments.   

def add(*b):
   sum=0
   for i in b:
      sum=sum+i
   print("sum = ",sum)

def fun(x,**a):
   print(x)
   print(a)


fun(12,name="ram",age=45,profession="doctor") 

add(12,5,9,4)  

add(12,20)

add(10,20,30,40,10)