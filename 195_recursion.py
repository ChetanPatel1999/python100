#wap to print number 10 to 1 using recursion.

def number(num):
    print(num)
    if num>1:
        number(num-1)

number(10)
