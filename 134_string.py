#write a program to take a string from user
# and convert in upper case string.
name="moHI123t"
uppername=""
for i in name: 
      if ord(i) in range(97,123):
            uppername=uppername+chr(ord(i)-32)
      else:
            uppername=uppername+i      
print(f"upper name :{uppername}")