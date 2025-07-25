#how to take list element from user.
fruits=[]    #create empty list
n=int(input("enter list length : "))
for i in range(n):
    fruit=input(f"enter fruit{i+1} :")
    fruits.append(fruit)
print(f"fruits list : {fruits}")