#wap to make new even element list from given list.
l1=[12,7,3,18,9]
l2=[i for i in l1 if i%2==0]
print(l2)

l3=[i for i in l1 if i%2==1]
print(l3)

l4=[i for i in l1 if i>10]
print(l4)
# [12,7,3,18,9]
l5=[i for i in l1 if i>5 and i<15]
print(l5)

l6=[i for i in l1 if i%6==0 or i%7==0]
print(l6)