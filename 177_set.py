#wap to remove duplicate value for list.
l1=[12,34,56,12,56,78,90,12]
l3=set(l1)
l2=[]
for i in range(len(l1)):
    find=False
    for j in range(i+1,len(l1)):
        if l1[i]==l1[j]:
           find=True 
           break
    if find==False:
        l2.append(l1[i])   # 34 56 78 90 12 

l4=[] # 12 34 56  78 90

for i in l1:
    if i not in l4:
        l4.append(i)

print(l2)  
l3=list(l3)      
print(l3) 
print(l4)       

           