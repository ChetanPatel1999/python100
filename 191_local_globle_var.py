#global varible :- global variable declaire in main program and we can access them in every function using global keyword
#local variable :- local varible declared inside function and we can access them only same function.

def fun1():
    global b
    print(b)
    a=12  #local variable
    print(a)

def fun2():
    global b
    b=b+1
    print(b)

b=50 # global variable
fun1()    
print(b)
fun2()
print(b)