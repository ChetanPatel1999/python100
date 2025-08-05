# Removing Items  
# There are several methods to remove items from a dictionary:  
# Example : The pop() method removes the item with the specified key name:  
dict1 = {   "brand": "Ford",  
  "model": "Mustang",  
  "year": 1964  
}  
dict1.pop("year")  
print(dict1) 

# popitem() method delete last item of dict
dict1.popitem()
print(dict1) 

dict1["color"]="red"
dict1["price"]=4352432
#  The del keyword removes the item with the specified key name: 
# del dict1   its delete dictonary

print(dict1) 

del dict1["price"]

print(dict1)

# The clear() method empties the dictionary: 
dict1.clear()

print(dict1)