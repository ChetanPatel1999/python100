# Keep ONLY the Duplicates  
# The intersection_update() method will keep only the items that are present in both sets.  
x = {"apple", "banana", "cherry"}  
y = {"google", "microsoft", "apple"} 
z=x.intersection(y) 
a=y&z
print(a)
print(z)
x.intersection_update(y)
print(x)  