#nested dictionary
std1={"name":"ram","rno":101}
std2={"name":"shyam","rno":102}
std3={"name":"raj","rno":103}

student={'s1':std1,'s2':std2,'s3':std3}
# print(student)

# print(student['s1'])
# print(student['s1']["name"])
student['s2']['name']="hariom"
student['s2']['per']=78
del student['s3']['rno']
print(student)