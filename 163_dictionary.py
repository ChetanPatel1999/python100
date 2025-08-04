# Dictionary is a collection of keys values, used to store data values like a map, which, 
# unlike other data types which hold only a single value as an element.  
# • Dictionaries are used to store data values in key:value pairs.  
# • A dictionary is a collection which is ordered*, changeable and do not allow 
# duplicates. 

student={"ram":5634,"shyam":2345,"rohan":6789}

stationary={"pen":5,"book":50,"color":20}

factors={12:[1,2,3,4,6,12],15:[1,3,5,15]}

word={1:"one",2:"two",3:"three"}

print(student)
print(stationary)
print(factors)
print(word)

print("we can print dictonary value using dictionary key")
print(student["ram"])
print(stationary["book"])

print("we can change value using key ")

stationary["book"]=100

print(stationary)
