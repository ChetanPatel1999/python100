#wap to take students marks from user and display
#max marks.
marks=[]    
n=int(input("enter list length : "))
for i in range(n):
    mark=int(input(f"enter marks{i+1} :"))
    marks.append(mark)
print(f"marks list : {marks}")
#[56,89,300,40,80]
max=marks[0]
for mark in marks:
    if mark>max:
        max=mark
print(f'max marks = {max}')



