#wap to serach a given number in given table.
tab_num=int(input("enter a num for table :"))#6
search=int(input("enter a num for search :"))#55
is_find=False
for i in range(1,11):
    if tab_num*i==search:
        is_find=True
        break     
if is_find:
    print("num is found")
else:
    print("num is not found")    
