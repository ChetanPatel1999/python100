#write a program to take a string from user
# and increase each charcter of string by one.
# "mohiz"----> "npija"
name="mohiz"
uppername=""
for i in name:
    if i=='z':
        uppername=uppername+'a'
    else:    
      uppername=uppername+chr(ord(i)+1)
print(f"upper name :{uppername}")