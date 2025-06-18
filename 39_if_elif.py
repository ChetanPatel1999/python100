#  Write a program to check whether a character is an alphabet, digit or special 
# character. 
char=input("enter a character : ")
if char in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" or ord(char) in range(97,123):
    print("char is alpha")
elif ord(char)>=48 and ord(char)<=57 :
    print("char is digit")   
else:
    print("char is special symbol")  