#  Remove Specified Item : The remove() method removes the specified item.
list1=[45,67,89,12,67,35,89,45,34]
n=89
for i in range(len(list1)):
    find=False
    if n==list1[i]:
        print(i)
        for j in range(i+1,len(list1)):
           if list1[i]==list1[j]:
             find=True
    if find == False and n==list1[i]:
        list2=list1[:i]
        list3=list1[i:]
        list3.remove(n)
        list1=list2+list3
        break

print(list1)

