import threading
import time

def file_download(file_name,second):
    print(f"{file_name} download start....")
    time.sleep(second)
    print(f"{file_name} download complete in {second} seconds")


# file_download("file1",2)    
# file_download("file2",5)    
# file_download("file3",3)    

#with multithreading
t1=threading.Thread(target=file_download,args=("file1",2))
t2=threading.Thread(target=file_download,args=("file2",5))
t3=threading.Thread(target=file_download,args=("file3",3))
t1.start()
t2.start()
t3.start()
#wait till 3 tread not complete
t1.join()
t2.join()
t3.join()
print("all file download compleate")