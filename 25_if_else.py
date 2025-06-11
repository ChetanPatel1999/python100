#wap to check given fruit availabel in fruit shop or not.
shop=["banana","apple","orange","mango"]
fruit=input("enter fruit name : ")
if fruit in shop:
   print(f"{fruit} is available") 
else:
    print(f"{fruit} is not available")   