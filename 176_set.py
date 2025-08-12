#difference() :- its return a set which different from another set if we 
# compare two set
s1={12,34,56,78}
s2={12,34,66,88}

s3=s1.difference(s2)
s4= s1-s2
print(s3)
print(s4)
s1.difference_update(s2)
print(s1)