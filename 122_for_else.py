#wap to serach a given number in given table.
tab_num=int(input("enter a num for table :"))#6
search=int(input("enter a num for search :"))#55
for i in range(1,11):
    if tab_num*i==search:
        print("num is found")
        break     
else:
      print("num is not found")  
