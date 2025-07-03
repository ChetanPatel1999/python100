char=65
for i in range(65,70):
    for j in range(65,i+1): #(0,1,2,3,4) 
            print(chr(char),end=" ")
            char+=1    
    print()    