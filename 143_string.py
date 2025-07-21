#wap to check given string is only digit or
# only alphbet or alphabet-digit type string.
str1=input("enter a string : ")
print("string : ",str1)
if str1.isalpha():
    print("string is alphbet type")
elif str1.isdigit():
    print("string is digit  type")
elif str1.isalnum():
     print("string is alphbet-digit type")
else:
    print("string is alpha-digit-special")          