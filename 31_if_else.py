#Write a program to check whether a character is an alphabet or not.
char=input("enter a char : ")# @
if ord(char) in range(65,91) or ord(char) in range(97,123):
    print("char is alphabet")
else:
    print("char is not alphabet")    