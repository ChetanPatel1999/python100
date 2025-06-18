#wap to check given char is special symbol or not.
char=input("enter a character : ")
if not(ord(char) in range(48,58) or ord(char) in range(65,91) or ord(char) in range(97,123)):
    print("char is special symbol")
else:
    print("char is not special symbol") 