# Update Dictionary  
# • The update() method will update the dictionary with the items from the given 
# argument.  
# • The argument must be a dictionary, or an iterable object with key:value pairs.  
dict1 = {   "brand": "Ford",  
"model": "Mustang",  
"year": 1964  
}  
dict1.update({"year": 2020}) 
print(dict1)
dict1.update({"color":"red"})
print(dict1)
dict1.update({"color":"blue","price":1200056})
print(dict1)