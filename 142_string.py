#Searches the string for a specified value and 
# returns the position of where it was found
str1="hello how are you"
sub= input("enter a sub string : ")
#print(str1.find("hom"))
f=str1.find(sub)
if f != -1:
    print(f"{sub} is find index {f}")
else:
    print("sub string is not find")

# Searches the string for a specified value and 
# returns the position of where it was found 
#if string was not found so that time show error index method
print(str1.index(sub))