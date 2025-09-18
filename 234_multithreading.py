import time
import threading
def tableprint(num):
    for i in range(1,11):
        print(f"{num} * {i} = {num*i}")
        time.sleep(0.5)

#example without multithreading
# tableprint(3)        
# tableprint(4)  

#example with multithreading 
t1 = threading.Thread(target=tableprint,args=[3])
t2 = threading.Thread(target=tableprint,args=[4])

t1.start()
t2.start()
   