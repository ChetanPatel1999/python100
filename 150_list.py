#how to take list element from user.
marks=[]    #create empty list
n=int(input("enter list length : "))
for i in range(n):
    mark=int(input(f"enter marks{i+1} :"))
    marks.append(mark)
print(f"marks list : {marks}")