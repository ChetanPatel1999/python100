# when a function call itself is called recursion.
i=1  #global variable
def fun():
    global i  # its access globle variable i
    print("hello brother!")# 5
    i+=1 # 6
    if i<=5:
        fun()

#main program section    
fun()    