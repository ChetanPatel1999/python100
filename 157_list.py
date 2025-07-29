# List Comprehension  
# List comprehension offers a shorter syntax when you want to create a new list based 
# on the values of an existing list. 

#wap to create new list using given list and new list contain squre element of previus list.
# l1=[4,6,2,8,5] 
# l2=[]
# for i in l1:
#     sqaure=i*i
#     l2.append(sqaure)
# print(l1)    
# print(l2)    

#change in same list
# l1=[4,6,2,8,5] 
# for i in range(len(l1)):
#     l1[i]=l1[i]*l1[i]    
# print(l1)    

#using list comprehension
l1=[4,6,2,8,5] 
l2=[i*i for i in l1]
print(l2)

