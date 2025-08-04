# The keys() method will return a list of all the keys in the dictionary. 
# The values() method will return a list of all the values in the dictionary.  
# The items() method will return each item in a dictionary, as tuples in a list. 
student={"name":"ram","rno":2345,"per":78.90}
keys=student.keys()
print(keys)
for key in keys:
    print(key)
print("-------------------------")
for key in student.keys():
    print(key)
print("-------------------------")
for value in student.values():
    print(value)    
print("-------------------------")
for item in student.items():
    print(item)    
print("-------------------------")
for key in student:
    print(f"{key} : {student[key]}")    