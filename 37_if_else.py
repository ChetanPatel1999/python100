# Write a  program to check whether a character is uppercase alphabet or lowercase 
# alphabet or not alphabet. 
char=input("enter a character : ")
if ord(char) in range(65 ,91):
    print("char is upercase alpha")
elif ord(char) in range(97,123):
    print("char is lowercase alpha")   
else:
    print("char is not an alpha")     
