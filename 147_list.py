#wap to change list 6 charcter items and each 6 charcter item char a replace with char o .
# fruits=["apple","banana", "mango","papaya"]
# for i in range(len(fruits)):
#     if(len(fruits[i])==6):
#         fruits[i]=fruits[i].replace('a','o')
# print(fruits)

fruits=["apple","banana", "mango","papaya"]
for i in range(len(fruits)):
    if(len(fruits[i])==6):
        str1=fruits[i]
        str2=""
        for j in range(len(str1)):
            if str1[j]=='a':
                str2=str2+'o'
            else:
                str2=str2+str1[j]  
        fruits[i]=str2
print(fruits)