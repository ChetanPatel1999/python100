#wap to print table of given number using recursion
def table(n):
    global i
    print(f"{n} x {i} = {n*i}")
    i+=1
    if i<=10:
        table(n)

i=1
table(8)        