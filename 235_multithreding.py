import time
import threading
def tableprint1():
    for i in range(1,11):
        print(f"{3} * {i} = {3*i}")
        time.sleep(1)

def tableprint2():
    for i in range(1,11):
        print(f"{4} * {i} = {4*i}")


#example without multithreading
# tableprint1()        
# tableprint2()  

#example with multithreading 
t1 = threading.Thread(target=tableprint1)
t2 = threading.Thread(target=tableprint2)

t1.start()
t2.start()
   