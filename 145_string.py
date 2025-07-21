#Joins the elements of an iterable to the end 
# of the string 
str1="welcome"
str2= (" "+chr(1)+" ").join(str1)
print(str2)
n=int(input("enter a num : "))#10
sum=0
st=""
for i in range(1,n+1):
    sum=sum+i
    if i!= n :
        st=st+(str(i)+"+")
    else :
        st=st+(str(i))    
print(f"{st} = {sum}")