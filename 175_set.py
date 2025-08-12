# Keep All, But NOT the Duplicates  
# The symmetric_difference_update() method will keep only the elements that are NOT 
# present in both sets.  
x = {"apple", "banana", "cherry"}  
y = {"google", "microsoft", "apple"} 
z = x.symmetric_difference(y)  
a=x^y
print(a)
print(z)
x.symmetric_difference_update(y)  
print(x)  