#wap to print 1 to 20 even number using recursion
def number():
    global i
    if i%2==0:
         print(i,end=" ")
    i+=1
    if i<=20:
        number()

i=1
number()        