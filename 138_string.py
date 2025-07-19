#write a programm to count character of each word of given string.
# hello raj how are youu
s=input("enter a string : ")
l1=s.split()
for i in l1:
    print(i," = ",len(i))