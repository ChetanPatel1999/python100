#we can iterate dictionary using for loop
student={"name":"ram","rno":2345,"per":78.90}
print("dictionary key :- ")
for key in student:
    print(key)

print("dictionary value :- ")
for key in student:
    print(student[key])

print("dictionary key = value :- ")
for key in student:
    print(key,"=",student[key])    