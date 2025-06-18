# Write a  program to check whether a character is uppercase alphabet or lowercase 
# alphabet or not alphabet. 
char=input("enter a character : ")
if char in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
    print("char is upercase alpha")
elif ord(char)>=97 and ord(char)<=122 :
    print("char is lowercase alpha")   
else:
    print("char is not an alpha")     
