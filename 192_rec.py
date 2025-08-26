#wap to print 1 to 10 number using recursion
def number():
    global i
    print(i)
    i+=1
    if i<=10:
        number()

i=1
number()        