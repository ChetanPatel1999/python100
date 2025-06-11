#Write a program to check whether a character is an alphabet or not.
char=input("enter a char : ")# @
if ord(char)>=65 and ord(char)<=90 or ord(char)>=97 and ord(char)<=122:
    print("char is alphabet")
else:
    print("char is not alphabet")    