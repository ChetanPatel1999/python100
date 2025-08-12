# There are several ways to join two or more sets in Python.  
# You can use the union () method that returns a new set containing all items from both 
# sets, and the update () method that inserts all the items from one set into another:  

s1={12,34,56,78}
s2={12,34,66,88}
s3=s1.union(s2)
print(s3)

s4= s1|s2
print(s4)

s1.update(s2)

print(s1)
