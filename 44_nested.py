#wap to check given number is even-positive or even-nagative or odd-positive or odd nagative.
num=int(input("enter a num : "))
if num%2==0:
    if num>0:
        print("even-positive")
    else:
        print("even-nagative")    
else:
    if num>0:
        print("odd-positive")
    else:
        print("odd-nagative")    