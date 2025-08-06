# #  To add one item to a set use the add() method. 
# s1={34,567,78,23}
# print(s1)
# s1.add("pen")
# print(s1)


# The object in the update() method does not have to be a set, it can be any iterable object 
# (tuples, lists, dictionaries etc.). 

s1={23,45,67,89}
s2={4,78,89}
s1.update(s2)
print(s1)
print(s2)
s1.update([34,56,23])
print(s1)
s1.update({"pen":90,"c":12})
print(s1)