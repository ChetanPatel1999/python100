#example of function
def add():
    print("addition app is called")
    a=int(input("enter value of a : "))
    b=int(input("enter value of b : "))
    c=a+b
    print(f"addition of {a} and {b} = {c}")

def sub(): #without parameter
    print("subtraction app is called")
    a=int(input("enter value of a : "))
    b=int(input("enter value of b : "))
    c=a-b
    print(f"subtraction of {a} and {b} = {c}")

def cube(num):  # with parametr
    res=num*num*num
    print(f"cube of {num} = {res}")

def factorial(num):
    fact=1
    for i in range(1,num+1):
        fact=fact*i
    print(f"factorial of {num} = {fact}")        

#function calling
factorial(5)
factorial(4)
factorial(6)
print("---------------------")
for i in range(1,11):
    factorial(i)
