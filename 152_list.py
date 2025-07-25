#wap to take students marks from user and display
#class avrage marks.
marks=[]    
n=int(input("enter list length : "))
for i in range(n):
    mark=int(input(f"enter marks{i+1} :"))
    marks.append(mark)
print(f"marks list : {marks}")

sum=0
for mark in marks:
    sum=sum+mark
print(f"total sum of marks = {sum}")    
print(f"class average marks  = {sum/n}")    